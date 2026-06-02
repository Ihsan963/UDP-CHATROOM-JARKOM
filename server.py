

import socket
import threading

SERVER_IP = '0.0.0.0'
SERVER_PORT = 9973

clients = {} 

def broadcast(message, sender_addr):
    for addr in list(clients.keys()):
        if addr != sender_addr:
            try:
                server_socket.sendto(message.encode(), addr)
            except Exception as e:
                print(f"[ERROR] Gagal kirim ke {addr}: {e}")

def handle_messages():
    print(f"[SERVER] Berjalan di {SERVER_IP}:{SERVER_PORT}")
    print("[SERVER] Menunggu koneksi client...\n")

    while True:
        try:
            data, addr = server_socket.recvfrom(4096)
            message = data.decode().strip()

            if message.startswith("/join:"):
                nickname = message.split(":", 1)[1]
                clients[addr] = nickname
                print(f"[JOIN] {nickname} ({addr[0]}:{addr[1]}) bergabung")
                server_socket.sendto(
                    f"[SERVER] Selamat Datang di Chatroom, {nickname}!".encode(), addr
                )
                broadcast(f"[SERVER] {nickname} telah bergabung ke chatroom.", addr)

            elif message == "/quit":
                if addr in clients:
                    nickname = clients.pop(addr)
                    print(f"[QUIT] {nickname} ({addr[0]}:{addr[1]}) keluar")
                    broadcast(f"[SERVER] {nickname} telah keluar dari chatroom.", addr)

            else:
                if addr in clients:
                    nickname = clients[addr]
                    formatted = f"{addr[0]}:{addr[1]}> {message}"
                    print(f"[MSG] {nickname}: {message}")
                    broadcast(formatted, addr)
                else:
                    server_socket.sendto(
                        "[SERVER] Silakan join dulu dengan /join:<nama>".encode(), addr
                    )

        except Exception as e:
            print(f"[ERROR] {e}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, SERVER_PORT))

if __name__ == "__main__":
    handle_messages()
