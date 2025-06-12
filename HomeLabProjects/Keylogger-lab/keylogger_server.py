import socket

# ---------- CONFIG ----------
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345
BUFFER_SIZE = 1024
# ---------------------------

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Listening for connections on {HOST}:{PORT}...")

try:
    conn, addr = server.accept()
    print(f"[+] Connection established from {addr[0]}")

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print("[*] Client disconnected.")
            break
        print(f"[DATA RECEIVED]: {data.decode('utf-8')}")

except Exception as e:
    print(f"[!] Server error: {e}")

finally:
    conn.close()
    server.close()
    print("[+] Server shutdown.")

