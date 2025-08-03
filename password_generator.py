# 보안용 랜덤 비밀번호 생성기
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

print("생성된 비밀번호:", generate_password())
