import os
from Crypto.PublicKey import RSA

def generate_keys(bits=2048, private_file="keys/private.pem", public_file="keys/public.pem"):
    if os.path.exists(private_file) or os.path.exists(public_file):
        print("❗ Кілт файлдары бар. Генерацияны тоқтатамыз.")
        return

    key = RSA.generate(bits)

    with open(private_file, "wb") as f:
        f.write(key.export_key())
    with open(public_file, "wb") as f:
        f.write(key.publickey().export_key())

    print("✅ RSA кілттер генерацияланды.")

if __name__ == "__main__":
    generate_keys()
