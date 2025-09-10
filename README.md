# 🖥️ Shutdown Timer App

A simple **Windows desktop app** that automatically shuts down your computer at a set time.
Built with **Python** and **Tkinter**.

---

## ✨ Features
- ⏰ Enter shutdown time in **24-hour format** (e.g. `1324` → auto converts to `13:24`)
- 🔄 Displays **real-time countdown** until shutdown
- 🕑 Confirms scheduled time in **12-hour format**
- ❌ **Cancel button** to stop shutdown and close the app
- ⚡ Lightweight, no background noise or annoying popups
- 🪟 Works on **Windows only** (uses `shutdown /s /t 1` command)

---

## 🚀 Usage
1. Run the app (`python shut.py` or the compiled `shut.exe`).
2. Enter the time you want your laptop/PC to shut down:
   - Example: `1324` → auto-formats → `13:24`.
3. Click **Set** → countdown begins.
4. Your computer will shut down automatically when the countdown reaches 0.
5. If you change your mind → click **Cancel**, shutdown will be aborted and the app will close.

---

## 🛠️ Build to EXE
To create a standalone `.exe` file:
```bash
pyinstaller --onefile --noconsole shut.py
