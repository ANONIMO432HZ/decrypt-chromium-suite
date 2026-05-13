import os
import sqlite3
import shutil
from pathlib import Path

def check_prefixes():
    local = os.environ.get('LOCALAPPDATA', '')
    chrome_path = Path(local) / "Google/Chrome/User Data/Default/Login Data"
    
    if not chrome_path.exists():
        print(f"No se encontró Login Data en: {chrome_path}")
        return

    print(f"Analizando: {chrome_path}")
    temp_db = "temp_login_data.db"
    shutil.copy2(chrome_path, temp_db)
    
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT password_value FROM logins LIMIT 10")
        rows = cursor.fetchall()
        
        if not rows:
            print("No se encontraron contraseñas en la base de datos.")
            return

        for i, row in enumerate(rows):
            blob = row[0]
            if not blob:
                print(f"[{i}] Blob vacío")
                continue
            
            prefix = blob[:3]
            print(f"[{i}] Prefijo detectado: {prefix} (Raw: {blob[:10].hex()})")
            
            if prefix == b"v20":
                print("    -> ¡CONFIRMADO!: Es App-Bound Encryption (v20).")
            elif prefix == b"v10" or prefix == b"v11":
                print("    -> Es AES-GCM estándar (v10/v11).")
            else:
                print("    -> Es un formato legacy o desconocido.")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
        if os.path.exists(temp_db):
            os.remove(temp_db)

if __name__ == "__main__":
    check_prefixes()
