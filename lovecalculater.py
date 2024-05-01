import random
import tkinter as tk

def calculate_result():
    yn = name_entry.get()
    pn = partner_entry.get()
    result = random.randint(0, 100)

    if result < 20:
        result_text.set("Kuchh Nahi Ho Sakta!!!!")
    elif 20 <= result <= 40:
        result_text.set("Try Karte Raho!!!!")
    elif 40 < result <= 60:
        result_text.set("Chance Hai!!!")
    elif 60 < result <= 80:
        result_text.set("Bas Ab Wait Khtm Hone Wala Hai!!!")
    elif result > 80:
        result_text.set("Congratulation!!!!! Made For Each Other")
    else:
        result_text.set("Ye To Us Moment Ho gya Bro!!")
    result_label.config(fg="Red")


root = tk.Tk()
root.title("Love Calculator")


name_label = tk.Label(root, text="Enter Your Name", font=("Arial", 14))
name_label.pack()
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack()

partner_label = tk.Label(root, text="Enter Your Partner's Name", font=("Arial", 14))
partner_label.pack()
partner_entry = tk.Entry(root, font=("Arial", 14))
partner_entry.pack()


calculate_button = tk.Button(root, text="Show Result", command=calculate_result, font=("Arial", 14))
calculate_button.pack()


result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 16))
result_label.pack()


root.mainloop()