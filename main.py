import tkinter
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password_txt=password_entry.get()
    with open("data.txt","a") as data_file:
        data_file.write(f"{website} | {email} | {password_txt}\n")
        website_entry.delete(0,tkinter.END)
        email_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)






# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.insert(0,"shoaibalt27@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=3)

# Buttons
generate_password = tkinter.Button(text="Generate Password",command=generate)
generate_password.grid(row=3,column=2)

add_button = tkinter.Button(text="Add", width=30,command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
