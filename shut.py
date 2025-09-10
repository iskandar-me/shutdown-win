import os
import time
import threading
from datetime import datetime, timedelta
import tkinter as tk

cancelled = False
target = None

def format_time_input(event=None):
    """Auto-insert ':' if user types 4 digits like 1324 → 13:24"""
    text = entry.get().strip()
    if len(text) == 4 and ":" not in text:
        entry.delete(0, tk.END)
        entry.insert(0, text[:2] + ":" + text[2:])

def schedule_shutdown():
    global target, cancelled
    cancelled = False
    user_time = entry.get().strip()

    try:
        target_time = datetime.strptime(user_time, "%H:%M").time()
    except Exception:
        countdown_label.config(text="❌ Invalid time! Use 24h format, e.g. 1324")
        return

    now = datetime.now()
    target = now.replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)

    display_time = target.strftime("%I:%M %p")
    countdown_label.config(text=f"✅ Shutdown scheduled at {display_time}")

    update_countdown()
    threading.Thread(target=shutdown_task, daemon=True).start()

def update_countdown():
    if target and not cancelled:
        remaining = int((target - datetime.now()).total_seconds())
        if remaining > 0:
            mins, secs = divmod(remaining, 60)
            hrs, mins = divmod(mins, 60)
            countdown_label.config(text=f"Time left: {hrs:02}:{mins:02}:{secs:02}")
            root.after(1000, update_countdown)
        else:
            countdown_label.config(text="💀 Shutting down...")

def shutdown_task():
    global cancelled
    while not cancelled:
        remaining = (target - datetime.now()).total_seconds()
        if remaining <= 0:
            os.system("shutdown /s /t 1")
            return
        time.sleep(1)

def cancel_shutdown():
    global cancelled
    cancelled = True
    countdown_label.config(text="❌ Shutdown cancelled. Closing app...")
    root.after(1500, root.destroy)  # close after 1.5s

# GUI setup
root = tk.Tk()
root.title("Shutdown Timer (24-hour Input)")
root.geometry("640x400")

tk.Label(root, text="Enter shutdown time (24h, e.g. 1324 → 13:24):").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<KeyRelease>", format_time_input)

tk.Button(root, text="Set", command=schedule_shutdown, bg="green", fg="white").pack(pady=5)

countdown_label = tk.Label(root, text="⌛ No shutdown scheduled", font=("Arial", 12))
countdown_label.pack(pady=10)

tk.Button(root, text="Cancel", command=cancel_shutdown, bg="red", fg="white").pack(pady=5)

root.mainloop()
