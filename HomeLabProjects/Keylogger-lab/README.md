# 🔐 Keylogger Socket Project (For Educational Purposes Only)

This project is a basic **Python-based keylogger** that I created to demonstrate how keystrokes can be captured and sent across a network using socket communication. It’s designed strictly for ethical, educational use as part of my cybersecurity portfolio.

---

## ⚙️ What I Built

The project includes two Python scripts:

### 1. `keylogger_client.py`  
This script runs on the target machine. It:
- Uses `pynput` to listen for keyboard input
- Captures each key the user types
- Sends the captured input to a remote server every time the **Enter key** is pressed

### 2. `keylogger_server.py`  
This script acts as a listener/server. It:
- Listens on a specified port for incoming TCP connections
- Prints out any data (keystrokes) it receives from the client

---

## 🧪 How I Tested It (Step by Step)

1. **Created both Python scripts** for the client and server
2. **Ran the server script** first to start listening for connections
3. **Updated the client script** to use `127.0.0.1` for local testing
4. **Ran the client script in a second terminal**
5. Typed text like `hello world`, pressed **Enter**, and verified the server printed the message
6. Also tested across a local network using the IP of the host machine
7. Made sure to handle errors and socket cleanup properly

---

## 🛠️ Libraries and Tools Used
- Python 3
- `pynput` (keyboard input tracking)
- `socket` (network communication)
- Terminal or command line

---

## 📁 Project Structure

