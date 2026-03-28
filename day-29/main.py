from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# password generator
def password_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# window
window = Tk()
window.title("Password Manager")
window.minsize(475, 450)

# func for searching saved passwords, usernames
def find_password():
    try:
        with open("password.json", "r") as file:
            data = json.load(fp=file)
            website = website_input.get()
            if website in data:
                messagebox.showinfo(title=website, message=
                f"Username: {data[website]["email"]}\n"
                f"Password: {data[website]["password"]}")
            else:
                messagebox.showerror(title=f"{website} Error", message=f"No username and password made for this website.")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="You did not create any passwords.\n"
                                                      "Please create some.")


# func for creating password.json
def save():
    website = website_input.get()
    name = name_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": name,
        "password": password
        }
    }

    if len(website) == 0 or len(name) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("password.json", "r") as file:
                # Reading old data
                data = json.load(fp=file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                # Writing updated data
                json.dump(new_data, file, indent=4)
        else:
            with open("password.json", "w") as file:
                # Writing updated data
                json.dump(data, file, indent=4)

        website_input.delete(0, END)
        name_input.delete(0, END)
        password_input.delete(0, END)
        name_input.insert(0, "martin.zapletal26@gmail.com")

# lock picture
lock_canvas = Canvas()
image = PhotoImage(file="lock.png")
lock_canvas.create_image(100, 100, image=image)
lock_canvas.place(x=152, y=50)

# labels
website_label = Label(text="Website:")
website_label.place(x=50, y=275)

name_label = Label(text="Email/Username:")
name_label.place(x=50, y=295)

password_label = Label(text="Password:")
password_label.place(x=50, y=315)

# inputs
website_input = Entry(width=25)
website_input.place(x=160, y=275)
website_input.focus()

name_input = Entry(width=35)
name_input.place(x=160, y=300)
name_input.insert(0, "martin.zapletal26@gmail.com")

password_input = Entry(width=25)
password_input.place(x=160, y=325)

# buttons
password_button = Button(text="Generate Password", width=14, command=password_generator)
password_button.place(x=320, y=322)

add_button = Button(text="Add", width=37, command=save)
add_button.place(x=160, y=352)

search_button = Button(text="Search", width=14, command=find_password)
search_button.place(x=320, y=272)


window.mainloop()
