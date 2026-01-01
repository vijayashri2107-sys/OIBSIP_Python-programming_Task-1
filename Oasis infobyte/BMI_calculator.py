import tkinter as tk
from tkinter import messagebox
import datetime

# ------------------ BMI FUNCTIONS ------------------

def calculate_bmi():
    try:
        name = entry_name.get()
        age = entry_age.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive")
            return

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "orange"
        elif bmi < 25:
            category = "Normal"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "blue"
        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"BMI : {bmi}\nCategory : {category}",
            fg=color
        )

        save_record(name, age, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


def save_record(name, age, weight, height, bmi, category):
    with open("bmi_app_records.txt", "a") as file:
        file.write(f"Date: {datetime.datetime.now()}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Weight: {weight} kg\n")
        file.write(f"Height: {height} m\n")
        file.write(f"BMI: {bmi}\n")
        file.write(f"Category: {category}\n")
        file.write("-" * 30 + "\n")


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="")


# ------------------ APP WINDOW ------------------

app = tk.Tk()
app.title("BMI Calculator App")
app.geometry("420x520")
app.config(bg="#1e1e2f")

# ------------------ HEADING ------------------

tk.Label(
    app,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
).pack(pady=15)

# ------------------ INPUT FRAME ------------------

frame = tk.Frame(app, bg="#2d2d44")
frame.pack(pady=10, padx=20, fill="both")

def create_label(text):
    tk.Label(
        frame,
        text=text,
        font=("Arial", 11),
        fg="white",
        bg="#2d2d44"
    ).pack(pady=5)

def create_entry():
    e = tk.Entry(frame, font=("Arial", 11))
    e.pack(pady=5)
    return e

create_label("Name")
entry_name = create_entry()

create_label("Age")
entry_age = create_entry()

create_label("Weight (kg)")
entry_weight = create_entry()

create_label("Height (meters)")
entry_height = create_entry()

# ------------------ BUTTONS ------------------

tk.Button(
    app,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#00adb5",
    fg="white",
    width=18,
    command=calculate_bmi
).pack(pady=15)

tk.Button(
    app,
    text="Clear",
    font=("Arial", 11),
    bg="#ff5722",
    fg="white",
    width=10,
    command=clear_fields
).pack()

# ------------------ RESULT ------------------

result_label = tk.Label(
    app,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=20)

# ------------------ RUN APP ------------------

app.mainloop()

