import tkinter as tk
from tkinter import messagebox
import requests

def add_customer():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    income = entry_income.get()
    credit_score = entry_credit.get()

    data = {
        "name": name,
        "age": age,
        "gender": gender,
        "income": income,
        "credit_score": credit_score
    }

    response = requests.post("http://127.0.0.1:5000/add_customer", json=data)

    if response.status_code == 200:
        messagebox.showinfo("Success", "Customer added successfully!")
    else:
        messagebox.showerror("Error", "Failed to add customer")

app = tk.Tk()
app.title("Bank Loan System")
app.geometry("400x300")

tk.Label(app, text="Name:").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Age:").pack()
entry_age = tk.Entry(app)
entry_age.pack()

tk.Label(app, text="Gender:").pack()
entry_gender = tk.Entry(app)
entry_gender.pack()

tk.Label(app, text="Income:").pack()
entry_income = tk.Entry(app)
entry_income.pack()

tk.Label(app, text="Credit Score:").pack()
entry_credit = tk.Entry(app)
entry_credit.pack()

tk.Button(app, text="Add Customer", command=add_customer).pack()

app.mainloop()
