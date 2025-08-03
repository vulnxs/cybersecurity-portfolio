# 간단한 포트 스캐너 예제 (학습용)
import socket

target = "scanme.nmap.org"
for port in range(20, 25):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
    s.close()
