from tkinter import messagebox
from tkinter import *
from random import *
import json
import pyperclip
from numpy.ma.extras import count_masked


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)#embaralhar password

    password = "".join(password_list)#concatena toda a lista em uma string usica
    entry_password.insert(5, password)
    pyperclip.copy(password)#copia direto sem precisar de ctrl c, pode fazer ctrl v direto

def save_txt():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

def find_password():
    website = entry_website.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Data Not Found")
    else:
        if website in data:
            password = data[website].get("password")
            messagebox.showinfo(title=website, message=f"Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"{website} not found")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
window = Tk()
window.title("Password Manage")
window.config(padx=50, pady=50)
canvas = Canvas(height = 200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image( 100, 100, image=logo_img)
canvas.pack()
canvas.grid(row=0, column = 1)
# description website
label_website = Label( text= "Website:")
label_website.grid(row = 1, column =0)

# entry of datas
entry_website = Entry(window, width=21)
entry_website.grid(row=1, column= 1)
entry_website.focus()
label_email = Label(window, text="Email/Username:")
label_email.grid(row=2, column=0, )
# entry of datas
entry_email = Entry(window, width=35)
entry_email.grid(row=2, column= 1, columnspan = 2)
entry_email.insert(0,"lennie@gmail.com")

label_password = Label(window, text="Password:")
label_password.grid(row=3, column=0)
entry_password = Entry(window, width=21)
entry_password.grid(row=3, column=1)
# entry_password.insert(0, "lennie123")
button_password = Button( text="Generate Password", command = generate_password)
button_password.grid(row=3, column = 2)
button_add = Button(text="Add", width=36, command = save_txt)
button_add.grid(row=4, column = 1,columnspan = 2)


button_search = Button(text="Search", width=13, command=find_password)
button_search.grid(row=1, column=2)






window.mainloop()
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

