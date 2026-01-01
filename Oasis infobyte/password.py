import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- APP FUNCTIONS ----------------

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Warning", "Password length must be at least 6")
            return
    except:
        messagebox.showerror("Error", "Enter valid password length")
        return

    chars = ""

    if letters_var.get():
        chars += string.ascii_letters
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Warning", "Select at least one option")
        return

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    for i in range(length - 4):
        password.append(random.choice(chars))

    random.shuffle(password)
    final_password = "".join(password)

    output_entry.delete(0, tk.END)
    output_entry.insert(0, final_password)


def copy_password():
    app.clipboard_clear()
    app.clipboard_append(output_entry.get())
    messagebox.showinfo("Copied", "Password copied successfully")


# ---------------- APP WINDOW ----------------

app = tk.Tk()
app.title("Password Generator App")
app.geometry("400x350")
app.resizable(False, False)

# ---------------- UI DESIGN ----------------

title = tk.Label(app, text=" Password Generator", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame1 = tk.Frame(app)
frame1.pack(pady=10)

tk.Label(frame1, text="Password Length", font=("Arial", 12)).pack(side=tk.LEFT)
length_entry = tk.Entry(frame1, width=8)
length_entry.pack(side=tk.LEFT, padx=5)

letters_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

frame2 = tk.Frame(app)
frame2.pack(pady=10)

tk.Checkbutton(frame2, text="Letters", variable=letters_var).grid(row=0, column=0, padx=10)
tk.Checkbutton(frame2, text="Numbers", variable=numbers_var).grid(row=0, column=1, padx=10)
tk.Checkbutton(frame2, text="Symbols", variable=symbols_var).grid(row=0, column=2, padx=10)

generate_btn = tk.Button(
    app, text="Generate Password",
    command=generate_password,
    bg="green", fg="white",
    width=20
)
generate_btn.pack(pady=15)

output_entry = tk.Entry(app, font=("Arial", 14), justify="center", width=28)
output_entry.pack(pady=10)

copy_btn = tk.Button(app, text="Copy Password", command=copy_password, width=18)
copy_btn.pack(pady=5)

footer = tk.Label(app, text="Python Mini Project - Tkinter App", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

app.mainloop()

