import matplotlib.pyplot as plt

# Sample data (tum real bhi le sakte ho)
algorithms = ["RSA", "AES (Your System)"]

encryption_time = [0.25, 0.02]
decryption_time = [0.30, 0.01]

x = range(len(algorithms))

plt.bar(x, encryption_time, width=0.4, label="Encryption")
plt.bar(x, decryption_time, width=0.4, bottom=encryption_time, label="Decryption")

plt.xticks(x, algorithms)
plt.xlabel("Algorithms")
plt.ylabel("Time (seconds)")
plt.title("RSA vs PQC-Based System Comparison")
plt.legend()

plt.show()