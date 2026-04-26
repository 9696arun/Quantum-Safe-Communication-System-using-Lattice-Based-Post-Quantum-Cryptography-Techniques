# 🔐 Quantum-Safe Communication System using Lattice-Based Post-Quantum Cryptography

🚀 A next-generation secure communication system designed to resist future quantum attacks using hybrid cryptographic techniques (PQC + AES + HMAC).

---

## 📌 Overview

This project implements a **Quantum-Safe Secure Communication System** combining:

- 🔐 AES-based Encryption (Fernet)
- 🧠 Post-Quantum Cryptography (Simulated PQC)
- 🛡️ HMAC-SHA256 Integrity Verification
- 🌐 Secure Socket Communication
- 📁 Encrypted File Transfer
- 📊 Performance Analysis & Visualization

---

## ⚙️ Key Features

✔ Secure real-time client-server communication  
✔ End-to-end encrypted messaging  
✔ Secure file transfer with encryption + integrity check  
✔ HMAC-based tamper detection  
✔ Attack simulation (tampered data detection)  
✔ Session-based encryption (optimized performance)  
✔ Logging system for data analysis  
✔ RSA vs AES performance comparison  
✔ Graph-based visualization (matplotlib)

---

## 🏗️ Project Structure


Quantum-Safe-Communication/
│
├── client/ # Client-side communication
├── server/ # Server-side communication
├── crypto/ # Encryption & HMAC logic
├── file_security/ # File handling modules
├── analysis/ # Graphs & performance analysis
├── gui/ # GUI (optional extension)
├── README.md
└── requirements.txt


---

## 🚀 How to Run

### 🔹 Step 1: Open Project Folder

```bash
cd "D:\Final year project\Quantum-Safe-Communication"
🔹 Step 2: Start Server
python -m server.server
🔹 Step 3: Start Client (New Terminal)
python -m client.client
🔐 Encryption Workflow
Client → Encrypt → HMAC → Send → Verify → Decrypt → Server
🔄 Steps:
🔑 Session key generated (AES)
🔒 Message encrypted using Fernet
🛡️ HMAC generated for integrity
🌐 Sent over socket
✅ Server verifies HMAC
🔓 Message decrypted
📊 Performance Analysis
🔹 RSA vs AES Comparison
Metric	RSA	AES (System)
Encryption Time	High	Very Low
Decryption Time	High	Very Low
Efficiency	Low	High

📌 Conclusion:

AES is faster and suitable for real-time systems
RSA/PQC is used for secure key exchange
Hybrid approach ensures best performance + security
🔹 Message Size Distribution

📌 Insights:

Encrypted sizes vary due to padding/randomization
Shows unpredictability (strong security)
System scales well with large data
🔹 Log-Based Analysis
Real-time message sizes stored in log.csv
Used for statistical and graphical analysis
Helps validate system performance
🛡️ Security Architecture

✔ End-to-End Encryption
✔ HMAC-SHA256 Integrity Verification
✔ Tamper Detection
✔ Secure Session Key Exchange
✔ Protection against Data Manipulation
✔ Attack Simulation Support

📈 Experimental Results
AES encryption significantly faster than RSA
System detects tampering successfully
File transfer is secure and verified
Performance improves with session-based encryption
🎯 Applications

🔹 Secure Messaging Systems
🔹 Military Communication
🔹 IoT Security
🔹 Cloud Encryption
🔹 Quantum-Safe Cybersecurity

🧠 Technologies Used
Technology	Purpose
Python 3	Core Development
Socket Programming	Network Communication
Cryptography (Fernet)	AES Encryption
HMAC (SHA-256)	Integrity Verification
Matplotlib	Data Visualization
🚀 Future Scope

🚀 Real PQC Algorithms (Kyber, FrodoKEM)
🚀 GUI Chat Application
🚀 Multi-user Chat System
🚀 TLS/SSL Integration
🚀 Blockchain-based Logging
🚀 Cloud Deployment

👨‍💻 Author

Arun
🎓 B.Tech CSE Final Year
🏫 Rajkiya Engineering College Kannauj

⭐ Support

If you like this project:

⭐ Star this repository
🍴 Fork and improve
📢 Share with others

📌 License

This project is for academic and research purposes only.
