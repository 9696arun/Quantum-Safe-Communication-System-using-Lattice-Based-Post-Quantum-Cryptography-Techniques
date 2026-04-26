# 🔐 Quantum-Safe Communication System using Lattice-Based Post-Quantum Cryptography

🚀 A secure communication system designed to resist future quantum attacks using hybrid cryptographic techniques (PQC + AES + HMAC).

---

## 📌 Overview

This project implements a **Quantum-Safe Secure Communication System** using:

- 🔐 Symmetric Encryption (AES - Fernet)
- 🧠 Post-Quantum Concepts (Simulated PQC)
- 🛡️ Integrity Verification (HMAC-SHA256)
- 🌐 Socket-based Secure Communication
- 📁 Secure File Transfer Support
- 📊 Performance Analysis & Visualization

---

## ⚙️ Features

✔ Secure real-time client-server communication  
✔ End-to-end encrypted messaging  
✔ File transfer with encryption + integrity check  
✔ HMAC-based tamper detection  
✔ Message size logging for analysis  
✔ Performance comparison (RSA vs AES)  
✔ Data visualization using matplotlib  

---

## 🏗️ Project Structure


Quantum-Safe-Communication/
├── client/
├── server/
├── crypto/
├── analysis/
├── file_security/
├── gui/
├── images/
├── main.tex
└── README.md


---

## 🚀 How to Run

### Step 1: Navigate to project folder
```bash
cd "D:\Final year project\Quantum-Safe-Communication"
Step 2: Start Server
python -m server.server
Step 3: Start Client (New Terminal)
python -m client.client
🔐 Encryption Workflow
Session key generated using AES
Message encrypted using Fernet
HMAC generated for integrity
Data transmitted via socket
Server verifies HMAC
Message decrypted securely
📊 Performance Analysis
🔹 RSA vs AES Comparison

👉 AES significantly outperforms RSA in speed and efficiency
👉 RSA is used for secure key exchange

🔹 Message Size Distribution

👉 Shows distribution of encrypted message sizes
👉 Demonstrates randomness and scalability

🔹 Dataset Logging

👉 CSV logs used for statistical analysis
👉 Captures message sizes during communication

🔹 Secure Communication Output

👉 Shows encryption, HMAC verification, and decryption
👉 Demonstrates system reliability and security

🛡️ Security Features
✔ End-to-End Encryption
✔ HMAC-based Integrity Check
✔ Tamper Detection
✔ Secure Session Key Exchange
✔ Protection against replay & modification attacks
📈 Results
AES provides faster encryption/decryption than RSA
System detects tampered messages successfully
Secure file transfer works without data corruption
Message size distribution confirms encryption randomness
🎯 Applications
Secure Messaging Systems
Military Communication
IoT Security
Cloud Data Protection
Post-Quantum Cryptography Research
📚 Technologies Used
Python 3
Socket Programming
Cryptography (Fernet)
HMAC (SHA-256)
Matplotlib
🧠 Future Improvements
🔹 Real PQC (Kyber / FrodoKEM integration)
🔹 TLS-based secure communication
🔹 GUI Chat Interface
🔹 Multi-client support
🔹 Blockchain-based logging
👨‍💻 Author

Arun
B.Tech CSE Final Year
Rajkiya Engineering College Kannauj

⭐ Support

If you like this project:

⭐ Star this repository
🍴 Fork it
📢 Share with others

📌 License

This project is for academic and research purposes.


---

# 🚀 FINAL STEP (IMPORTANT)