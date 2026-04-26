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

```
Quantum-Safe-Communication/
│
├── client/           # Client-side communication
├── server/           # Server-side communication
├── crypto/           # Encryption & HMAC logic
├── file_security/    # Secure file handling modules
├── analysis/         # Logs & performance graphs
├── gui/              # GUI (optional extension)
├── images/           # Screenshots & outputs
├── README.md
└── requirements.txt

---

🚀 How to Run
🔹 Step 1: Navigate to Project Directory
cd "D:\Final year project\Quantum-Safe-Communication"
🔹 Step 2: Start Secure Server
python -m server.server
🔹 Step 3: Start Client (New Terminal)
python -m client.client

---
🔐 Encryption Workflow
Client → Encrypt → HMAC → Send → Verify → Decrypt → Server

---
🔄 Process Flow
🔑 Session key generated securely
🔒 Message encrypted using AES (Fernet)
🛡️ HMAC created for integrity verification
🌐 Data transmitted via socket
✅ Server verifies HMAC (tamper detection)
🔓 Message decrypted securely

---
📊 Performance Analysis
🔹 RSA vs AES Comparison
Metric	RSA	AES (System)
Encryption Time	High	Very Low
Decryption Time	High	Very Low
Efficiency	Low	High

👉 AES is significantly faster than RSA
👉 Hybrid model ensures both performance & security
---
🔹 Message Size Distribution
📈 Shows randomness of encrypted data
🔐 Confirms strong encryption behavior
⚡ Demonstrates scalability with increasing data size
🔹 Logging System
🧾 Real-time data stored in log.csv
📊 Used for performance graphs
🔍 Enables statistical analysis
---
🛡️ Security Architecture
✔ End-to-End Encryption
✔ HMAC-SHA256 Integrity Verification
✔ Tamper Detection Mechanism
✔ Secure Session Key Exchange
✔ Protection against Data Manipulation

---
📈 Results
⚡ AES is significantly faster than RSA
🛡️ System successfully detects tampered messages
📁 Secure file transfer without data corruption
📊 Graphs validate system performance
🎯 Applications
🔐 Secure Messaging Systems
🪖 Military & Defense Communication
🌐 IoT Security
☁️ Cloud Data Protection
🔬 Post-Quantum Cryptography Research
📚 Tech Stack
---
Technology	Purpose
Python	Core Development
Socket	Network Communication
Fernet	AES Encryption
HMAC	Integrity Verification
Matplotlib	Data Visualization

---
🚀 Future Scope
🔹 Integration with Real PQC (Kyber, FrodoKEM)
🔹 GUI-based Chat Application
🔹 Multi-client Communication
🔹 TLS/SSL Secure Channel
🔹 Blockchain-based Logging

---
👨‍💻 Author

Arun
🎓 B.Tech CSE
🏫 Rajkiya Engineering College Kannauj


