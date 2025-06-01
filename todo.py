import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("To-Do List")
tasks=[]
def update_listbox():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)
def add_task():
    task=entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("input Error","enter a task!")
def delete_task():
    selected=listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("select task","no task selected")
entry=tk.Entry(root,width=40)
entry.pack(pady=5)
tk.Button(root,text="add task",width=20,command=add_task).pack()
tk.Button(root,text="Delete task",width=20,command=delete_task).pack()
listbox=tk.Listbox(root,width=50)
listbox.pack(pady=10)
root.mainloop()


        







        
