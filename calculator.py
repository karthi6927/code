import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        n1=float(entry1.get())
        n2=float(entry2.get())
        op=operation.get()
        if op=='+':
            result=n1+n2
        elif op=='-':
            result=n1-n2
        elif op=='*':
            result=n1*n2
        elif op=='/':
            result=n1/n2 if n2!=0 else "can't divide by zero "
        else:
            result="invalid operation"
        result_label.config(text=f"Result:{result}")
    except ValueError:
         messagebox.showerror("input error","please enter valid numbers")
root=tk.Tk()
root.title("simple calculator")
tk.Label(root,text="First Number:").grid(row=0,column=0)
entry1=tk.Entry(root)
entry1.grid(row=0,column=1)

tk.Label(root,text="Second Number:").grid(row=1,column=0)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1)
tk.Label(root,text="Operation(+,-,*,/):").grid(row=2,column=0)
operation=tk.Entry(root)
operation.grid(row=2,column=1)
tk.Button(root,text="calculate",command=calculate).grid(row=3,columnspan=2)
result_label=tk.Label(root,text="Result:")
result_label.grid(row=4,columnspan=2)
root.mainloop()




        











                              
