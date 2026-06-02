

import socket
import threading
import sys

SERVER_IP = input("Masukkan IP Server : ").strip() or '127.0.0.1'
SERVER_PORT = 9973

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', 0)) 

def receive_messages():
    while True:
        try:
            data, _ = client_socket.recvfrom(4096)
            message = data.decode().strip()
            print(f"\n{message}")
            print(">> ", end='', flush=True)
        except:
            break

def main():
    nickname = input("Masukkan nama kamu: ").strip()
    if not nickname:
        nickname = "Anonymous"

  
    client_socket.sendto(f"/join:{nickname}".encode(), (SERVER_IP, SERVER_PORT))

   
    local_addr = client_socket.getsockname()
    print(f"\n[INFO] Terhubung ke server {SERVER_IP}:{SERVER_PORT}")
    print(f"[INFO] Port lokal kamu: {local_addr[1]}")
    print("[INFO] Ketik pesan dan tekan Enter untuk kirim")
    print("[INFO] Ketik /quit untuk keluar\n")

  
    recv_thread = threading.Thread(target=receive_messages, daemon=True)
    recv_thread.start()

   
    while True:
        try:
            msg = input(">> ").strip()
            if not msg:
                continue
            if msg == "/quit":
                client_socket.sendto("/quit".encode(), (SERVER_IP, SERVER_PORT))
                print("[INFO] Kamu telah keluar dari chatroom.")
                break
            client_socket.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))
        except (KeyboardInterrupt, EOFError):
            client_socket.sendto("/quit".encode(), (SERVER_IP, SERVER_PORT))
            print("\n[INFO] Keluar...")
            break

    client_socket.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
