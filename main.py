import tkinter as tk
import random
import string

def random_password():
    password_length = int(textbox.get())
    password = "Result: "
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(password_length):
         password += random.choice(characters)

    result.config(text=str(password))

window = tk.Tk()
window.geometry("250x200")
window.title("Password_generator")

generate_button = tk.Button(window, text="Generate a password: ", command=random_password)
generate_button.place(x=10,y=10)

result = tk.Label(window, text="Result: ")
result.place(x=10, y=50 )

textbox_label = tk.Label(window, text="Password length: ")
textbox_label.place(x=10, y=100)

textbox = tk.Entry(window)
textbox.place(x=10, y =120)

window.mainloop()


