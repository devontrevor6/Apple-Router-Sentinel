import socket, threading, time, os
def handle(c, a):
    with open("SUCCESS_INGRESS.log", "a") as f:
        f.write(f"SUCCESS: {a[0]} | VIOLATION: PMIC_PROBE | {time.ctime()}\n")
    c.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind(('0.0.0.0', 4444))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle, args=(conn, addr)).start()
except: pass
