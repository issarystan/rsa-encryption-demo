# RSA Encryption & Decryption Demo

Бұл жоба RSA көмегімен хабарламаны шифрлау және дешифрлау процесін көрсетеді.  
Кілттер генерацияланады, хабарлама шифрланады және қайтадан оқылады.  
`pycryptodome` кітапханасына негізделген.

---

## Жоба құрылымы

```
rsa-encryption-demo/
├── Generation_keys_forRSA.py
├── encryptingRSA.py
├── decryptingRSA.py
├── keys/
│   ├── private.pem              # Жабық кілт
│   └── public.pem               # Ашық кілт
├── messages/
│   ├── message.txt              # Шифрланатын хабарлама
│   ├── encrypted_message.txt    # Шифрланған файл
│   └── decrypted_message.txt    # Шешілген файл
├── README.md
└── requirements.txt
```

---

## Шектеу

RSA тек **қысқа хабарламаларды** (шамамен 200 символға дейін) шифрлай алады.  
Егер ұзақ мәтін болса – `Plaintext is too long` қатесі шығады.  
Оны шешу үшін гибридті схема (RSA + AES) қолданылады.

---

## Орнату
```bash
pip install pycryptodome
```

---

## Қолдану

### 1. Кілт генерациялау:
```bash
python Generation_keys_forRSA.py
```

➡️ Нәтиже: `keys/private.pem`, `keys/public.pem`

---

### 2. Хабарламаны шифрлау:
```bash
python encryptingRSA.py
```

➡️ Терминалдан теруге немесе `messages/message.txt` ішінен оқуға болады  
➡️ Нәтиже: `messages/encrypted_message.txt`

---

### 3. Хабарламаны шешу:
```bash
python decryptingRSA.py
```

➡️ Нәтиже: `messages/decrypted_message.txt`

---

## Автор

**Arystan Issatayev**  
📧 issatayev4@gmail.com  
💬 [@issarystan](https://t.me/issarystan)

---

> Ашық/жабық кілттермен қауіпсіз шифрлау моделін көрсетуге арналған оқу жобасы.
