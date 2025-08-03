import socket

target = input("🔍 스캔할 IP 주소를 입력하세요: ")
ports = [21, 22, 80, 443, 8080]

print(f"[+] {target}의 열린 포트를 확인 중입니다...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ 포트 {port} 열림")
    else:
        print(f"❌ 포트 {port} 닫힘")
    sock.close()
