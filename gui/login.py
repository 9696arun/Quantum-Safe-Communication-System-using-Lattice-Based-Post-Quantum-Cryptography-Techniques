import tkinter as tk
from tkinter import messagebox

def login():
    if username.get() == "admin" and password.get() == "1234":
        messagebox.showinfo("Login", "Success")
    else:
        messagebox.showerror("Login", "Invalid")

root = tk.Tk()
root.title("Login")

username = tk.Entry(root)
password = tk.Entry(root, show="*")

tk.Label(root, text="Username").pack()
username.pack()

tk.Label(root, text="Password").pack()
password.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()