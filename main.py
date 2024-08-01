from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=50, pady=50)

canvas = Canvas()
canvas = Canvas(width=200, height=200, highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website field
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')

# Email/Username field
username_label = Label(text='Email/Username')
username_label.grid(row=2, column=0)
# Username entry
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, sticky='w', columnspan=2)

# Password and entry field
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')
# Generate Password Button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
