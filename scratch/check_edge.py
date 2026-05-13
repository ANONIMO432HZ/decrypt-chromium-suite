import os
import sqlite3
import shutil
from pathlib import Path

def check_edge_prefixes():
    local = os.environ.get('LOCALAPPDATA', '')
    edge_path = Path(local) / "Microsoft/Edge/User Data/Default/Login Data"
    
    if not edge_path.exists():
        print(f"No se encontró Login Data en: {edge_path}")
        return

    print(f"Analizando Edge: {edge_path}")
    temp_db = "temp_edge_data.db"
    shutil.copy2(edge_path, temp_db)
    
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT password_value FROM logins LIMIT 10")
        rows = cursor.fetchall()
        
        if not rows:
            print("No se encontraron contraseñas en Edge.")
            return

        for i, row in enumerate(rows):
            blob = row[0]
            if not blob: continue
            
            prefix = blob[:3]
            print(f"[{i}] Prefijo detectado: {prefix}")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
        if os.path.exists(temp_db):
            os.remove(temp_db)

if __name__ == "__main__":
    check_edge_prefixes()
