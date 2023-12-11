from tkinter import *
import tkinter as tk
import psycopg2

dbname = "students"
user = "postgres"
password = "1234"
host = "localhost"
port = "5432"
CONN = None

def connection():
    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def insert_data():
    n = input_name.get()
    add = input_address.get()
    print(n , add)
    CONN = connection()
    cur = CONN.cursor()
    query = """INSERT INTO student (name, address) VALUES (%s , %s); """
    cur.execute(query, (n, add))
    CONN.commit()
    input_address.delete(0,END)
    input_name.delete(0,END)
    print("inserted data")
    CONN.close()
    
def get_data():
    CONN = connection()
    cur = CONN.cursor()
    query = """SELECT * FROM student; """
    cur.execute(query)
    CONN.commit()
    rows = cur.fetchall()
    
     # Clear existing labels
    for widget in frame.winfo_children():
        widget.destroy()

    # Create new labels
    row = 6
    col = 1
    Label(frame, text="All Data Of Students",font=("serif" , 20 ,"bold")).grid(row=row-1, column=col)
    Label(frame, text="name").grid(row=row, column=col)
    Label(frame, text="address").grid(row=row, column=col+1)

    for r, row in enumerate(rows, start=1):
        lbl = Label(frame, text=row[0])
        lbl.grid(row=6+r, column=col)
        lbl2 = Label(frame, text=row[1])
        lbl2.grid(row=6+r, column=col+1)
        
        
    CONN.close()
      
      
      

root = Tk()
root.title("insert data")
canvas = Canvas(root , height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)


LBL_FONT = ("arial" , 15 , "bold")

title = Label(frame , text="Add Data")
title.config(font=("normal" , 20 , "bold"),padx=25,pady=5)
title.grid(row=0, column=1)


#create input name
lbl_name = Label(frame , text="usrname: " , font=LBL_FONT)
lbl_name.grid(row=1,column=0)

input_name = Entry(frame)
input_name.grid(row=1,column=1)

#create input address
lbl_address = Label(frame , text="address: ", font=LBL_FONT)
lbl_address.grid(row=2,column=0)

input_address = Entry(frame)
input_address.grid(row=2,column=1)


# button to insert data
btn_insert_data = tk.Button(frame , text="Enter" , command=insert_data)
btn_insert_data.grid(row=4,column=1)


# button to get data
btn_get_data = tk.Button(frame , text="get data" , command=get_data)
btn_get_data.grid(row=5,column=1)

"""
we have two field of data in a student table (name , address),
so we hav create two inputs
"""

      
      

root.mainloop()















# #create input name
# lbl_name = Label(root , text="usrname")
# lbl_name.pack()
# input_name = Entry(root , text ="Enter name...")
# input_name.pack()

# #create input address
# lbl_address = Label(root , text="address")
# lbl_address.pack()
# input_address = Entry(root , text ="Enter address...")
# input_address.pack()



