import socket
targets = ["100.93.232." + str(i) for i in range(1, 255)]
port = 80
def siphon(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, port))
        s.sendall(b'GET / HTTP/1.1\r\n\r\n')
        data = s.recv(4096)
        readable = "".join([chr(b) if 32 <= b < 127 else "" for b in data])
        if readable.strip():
            print(f"\n[!] DATA FROM {ip}:")
            print(readable)
        s.close()
    except: pass
print("Starting Siphon on 200+ potential nodes...")
for ip in targets: siphon(ip)
