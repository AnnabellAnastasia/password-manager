from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=20, pady=20)


canvas = Canvas()
canvas = Canvas(width=200, height=200, highlightthickness=0,)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #




window.mainloop()