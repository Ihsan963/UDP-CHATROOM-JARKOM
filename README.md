NAMA: Ihsan Maulana Harjanto
NRP: 5024241090

# UDP CHATROOM JARKOM 

Simulasi komunikasi antar client melalui server menggunakan protokol **UDP (User Datagram Protocol)**, berbeda dengan TCP yang perlu accept dahulu, UDP bisa kirim langsung tanpa perlu accept koneksi dulu.

---

## Arsitektur

```
Client 1 ──┐
Client 2 ──┼──► SERVER (port 9973) ──► broadcast ke semua client lain
```

Server berperan sebagai **perantara** — menerima pesan dari satu client lalu meneruskannya ke semua client lain.

---

## Cara Menjalankan

**Minimal butuh 3 terminal.**

**Terminal 1 — Server:**
```bash
python server.py
```

**Terminal 2 & 3 — Client:**
```bash
python client.py
```
Masukkan IP server dan nama, lalu mulai chat.

---

## Perintah

| Perintah | Fungsi |
|---|---|
| `/join:nama` | Bergabung ke chatroom (otomatis saat run) |
| `/quit` | Keluar dari chatroom |

---

## Teknologi

- **Python 3**
- **Socket UDP** — `SOCK_DGRAM`
- **Threading** — agar client bisa kirim & terima pesan bersamaan# UDP-CHATROOM-JARKOM
