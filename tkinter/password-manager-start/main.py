from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_inp.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    w = website_inp.get()
    e = email_inp.get()
    p = pass_inp.get()
    if len(w) == 0 or len(e) == 0 or len(p) ==0:
        messagebox.showinfo(title="Oops",message="Please don`t leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=w,message=f"These are thr details entered: \nEmail:{e}\nPassword: {p}\nIs it ok to save")
        if is_ok:
            with open("user_data.txt" , "a") as file:
                file.write(w + " | " + e + " | " + p + "\n")

                website_inp.delete(0,END)
                email_inp.delete(0,END)
                pass_inp.delete(0,END)
       
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Generate Password")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website = Label(text="website:")
website.grid(row=1,column=0)

website_inp = Entry(width=35)
website_inp.focus()
website_inp.grid(row=1,column=1,columnspan=2)


email = Label(text="Email/Username:")
email.grid(row=2,column=0)

email_inp = Entry(width=35)
email_inp.insert(0 , "omar@gmail.com")
email_inp.grid(row=2,column=1,columnspan=2)

password = Label(text="Password:")
password.grid(row=3,column=0)

gen_pass = Button(text="generate password",command=generate_password)
gen_pass.grid(row=3,column=2)

pass_inp = Entry(width=21)
pass_inp.grid(row=3,column=1)



btn_add = Button(text="Add",width=30,command=save_data)
btn_add.grid(row=4,column=1,columnspan=2)


window.mainloop()
