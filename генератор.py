import tkinter as tk
import random
import string

def generate_password():

    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()


    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase  
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%"


    if not characters:
        result_label.config(text="Выберите хотя бы один тип символов.")
        return


    password_length = 12
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text=f"Сгенерированный пароль: {password}")


root = tk.Tk()
root.title("Генератор паролей")


lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()


lowercase_checkbox = tk.Checkbutton(root, text="Включить алфавит нижнего регистра [a-z]", variable=lowercase_var)
lowercase_checkbox.pack(anchor=tk.W)

digits_checkbox = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=digits_var)
digits_checkbox.pack(anchor=tk.W)

special_checkbox = tk.Checkbutton(root, text="Включить спецсимволы [!@#$%]", variable=special_var)
special_checkbox.pack(anchor=tk.W)


generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()


