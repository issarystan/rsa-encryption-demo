from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

try:
    with open("keys/public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    use_file = input("📁 Файлдан оқимыз ба? (y/n): ").lower()

    if use_file.startswith("y"):
        if not os.path.exists("messages/message.txt"):
            print("❌ message.txt табылмады.")
            exit()
        with open("messages/message.txt", "r", encoding="utf-8") as f:
            message = f.read()
    else:
        message = input("✉️  Хабарлама енгізіңіз: ")

    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted = cipher_rsa.encrypt(message.encode("utf-8"))

    with open("messages/encrypted_message.txt", "wb") as f:
        f.write(encrypted)

    print("✅ Хабарлама шифрланды.")
except Exception as e:
    print("⚠️ Қате:", e)
