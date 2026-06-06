from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
      letters = [
      'a','b','c','d','e','f','g','h','i','j','k','l','m',
      'n','o','p','q','r','s','t','u','v','w','x','y','z'
      ]
      numbers = ['0','1','2','3','4','5','6','7','8','9']
      symbols = ['!','#','$','%','&','(',')','*','+']

      password_letters = [choice(letters) for _ in range(randint(8,10))]
      password_numbers = [choice(numbers) for _ in range(randint(2,4))]
      password_symbols = [choice(symbols) for _ in range(randint(2,4))]

      password_list = password_letters + password_numbers + password_symbols
      shuffle(password_list)

      password = "".join(password_list)
      password_entry.insert(0,password)
      pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title="Confirm",
        message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nSave?"
    )

    if is_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            data = {}

        except json.JSONDecodeError:
            data = {}

        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

# ---------------------------- Search Method ------------------------------- #

def search():
    website = website_entry.get()

    try:
        with open("Password Manager/data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is empty.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showerror(
                title="Not Found",
                message=f"No details for {website} exist."
            )

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width = 200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(window)
website_entry.config(width=35)
website_entry.grid(row=1, column=1, columnspan=2) 
website_entry.focus()

email_username_entry = Entry(window)
email_username_entry.config(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(window)
password_entry.config(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(window, text="Add", command=save)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)




window.mainloop()