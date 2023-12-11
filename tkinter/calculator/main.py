from tkinter import *
from tkinter import ttk
import ast
root = Tk()
root.title("Calculator")
root.config(pady=20,padx=20)

def clear_all():
    display.delete(0,END) 

def undo():
    entry_string = display.get()
    if len(entry_string):
        new_string = entry_string[:-1]
        clear_all()
        display.insert(0 , new_string)
    else:
        display.insert(0,"")
i = 0

def handelCalc(operation):
    global i
    if operation == "CE" or operation == "C" or  operation == "Error parsing":
        clear_all()
    elif operation == "=":
        calculate()
    elif operation == "x":
        undo()
    else:
        display.insert(i , operation)
        i += 1
def calculate():
    entry_string = display.get()
    if entry_string == "Error parsing":
        clear_all()
        return
    try:
        node = ast.parse(entry_string , mode="eval")
        res = eval(compile(node ,"<string>" ,"eval"))
        clear_all()
        display.insert(0 , res)
    except Exception:
        clear_all()
        display.insert(0 , "Error parsing")
        display.config(foreground="red")
        
f = ('Helvetica', 16)
display = ttk.Entry(root)
display.config(foreground="#000",font=f, justify='right',width=30)
display.grid(row=1,columnspan=6)
frm = ttk.Frame(root, padding=10)
frm.grid()



style = ttk.Style()
style.configure("TButton" , font=("Helvetica",12))

operations = ["%","CE","C","x","1/x","**2","**","/",7,8,9,"*",4,5,6,"-",1,2,3,"+","+/-",0,".","="]
counter = 0
for x in range(6):
    for y in range(4):
        btn = ttk.Button(frm,text=operations[counter] , command=lambda x=operations[counter]: handelCalc(x) , style="TButton")
        btn.grid(row=x+2,column=y)
        counter += 1
    

        
root.mainloop()

