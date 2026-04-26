import tkinter as tk
from crypto.pqc_utils import encrypt_message, decrypt_message, generate_keys

key, _, _ = generate_keys()

def send():
    msg = entry.get()
    if msg == "":
        return

    ciphertext, _ = encrypt_message(key, msg.encode())
    decrypted, _ = decrypt_message(key, ciphertext)

    # User message (right side)
    chat.insert(tk.END, "You: " + msg + "\n", "user")

    # Receiver message (left side)
    chat.insert(tk.END, "Friend: " + decrypted.decode() + "\n\n", "other")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Quantum Secure Chat")

chat = tk.Text(root, bg="white", fg="black", font=("Arial", 12))
chat.tag_config("user", foreground="blue", justify="right")
chat.tag_config("other", foreground="green", justify="left")
chat.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill=tk.X)

tk.Button(root, text="Send", command=send, bg="green", fg="white").pack()

root.mainloop()