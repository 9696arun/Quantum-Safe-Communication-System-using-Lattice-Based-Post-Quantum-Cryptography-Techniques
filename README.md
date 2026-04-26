# 🔐 Quantum-Safe Communication System  
### 🚀 Hybrid Cryptography using AES + HMAC + Post-Quantum Concepts

![Python](https://img.shields.io/badge/Python-3-blue)
![Security](https://img.shields.io/badge/Security-High-green)
![Status](https://img.shields.io/badge/Project-Final%20Year-orange)

---

## 📌 Overview

This project presents a **Quantum-Safe Secure Communication System** designed to withstand future quantum attacks using hybrid cryptographic techniques.

It combines:

- 🔐 AES Encryption (Fernet)
- 🧠 Post-Quantum Cryptography Concepts (Simulated)
- 🛡️ HMAC-SHA256 Integrity Verification
- 🌐 Secure Socket Communication
- 📁 Encrypted File Transfer
- 📊 Performance Analysis & Visualization

---

## ⚙️ Key Features

✔ Secure real-time client-server communication  
✔ End-to-end encrypted messaging  
✔ Encrypted file transfer with integrity check  
✔ HMAC-based tamper detection  
✔ Attack simulation support  
✔ Session-based encryption  
✔ Logging & data analysis (CSV)  
✔ RSA vs AES performance comparison  
✔ Graph visualization (matplotlib)

---

## 🏗️ Project Structure


Quantum-Safe-Communication/
│
├── client/ # Client communication
├── server/ # Server communication
├── crypto/ # Encryption & HMAC logic
├── file_security/ # File handling
├── analysis/ # Graphs & logs
├── gui/ # GUI (optional)
├── images/ # Screenshots
├── README.md
└── requirements.txt


---

## 🚀 How to Run

### 1️⃣ Open Project Folder

```bash
cd "D:\Final year project\Quantum-Safe-Communication"
2️⃣ Start Server
python -m server.server
3️⃣ Start Client (New Terminal)
python -m client.client
🔐 Encryption Workflow
Client → Encrypt → HMAC → Send → Verify → Decrypt → Server
Steps:
🔑 Session key generated
🔒 Message encrypted (AES)
🛡️ HMAC generated
🌐 Sent via socket
✅ Verified on server
🔓 Decrypted securely
📊 Performance Analysis
🔹 RSA vs AES Comparison
Metric	RSA	AES (System)
Encryption Time	High	Very Low
Decryption Time	High	Very Low
Efficiency	Low	High

👉 AES is significantly faster than RSA
👉 Hybrid approach ensures security + performance

🔹 Message Size Distribution
Shows randomness of encrypted data
Confirms strong encryption behavior
Demonstrates scalability
🔹 Logging System
Real-time data stored in log.csv
Used for performance graphs
Helps in research analysis
🛡️ Security Architecture

✔ End-to-End Encryption
✔ HMAC Integrity Verification
✔ Tamper Detection
✔ Session Key Security
✔ Protection against Data Manipulation

📈 Results
AES is faster than RSA
System detects tampered messages
Secure file transfer works correctly
Graphs validate system performance
🎯 Applications

🔹 Secure Messaging Systems
🔹 Military Communication
🔹 IoT Security
🔹 Cloud Encryption
🔹 Post-Quantum Research

📚 Tech Stack
Technology	Use
Python	Core
Socket	Communication
Fernet	AES Encryption
HMAC	Integrity
Matplotlib	Graphs
🚀 Future Scope
Real PQC (Kyber, FrodoKEM)
GUI Chat Application
Multi-user support
TLS/SSL integration
Blockchain logging
👨‍💻 Author

Arun
🎓 B.Tech CSE
🏫 Rajkiya Engineering College Kannauj

⭐ Support

If you like this project:

⭐ Star this repo
🍴 Fork it
📢 Share
