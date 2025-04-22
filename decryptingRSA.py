from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

try:
    if not os.path.exists("messages/encrypted_message.txt"):
        raise FileNotFoundError("❌ encrypted_message.txt табылмады.")

    with open("keys/private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
    with open("messages/encrypted_message.txt", "rb") as f:
        encrypted = f.read()

    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = cipher_rsa.decrypt(encrypted)

    with open("messages/decrypted_message.txt", "w", encoding="utf-8") as f:
        f.write(decrypted.decode("utf-8"))

    print("✅ Хабарлама расшифрланды.")
except Exception as e:
    print("⚠️ Қате:", e)
