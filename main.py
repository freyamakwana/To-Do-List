#import modules
import tkinter as tk
from tkinter import messagebox

# Configure and create main window
dp = tk.Tk()
dp.geometry('500x450+500+200')
dp.title('To-Do List')
dp.config(bg='#EEE8AA')

# Create widgets
frame = tk.Frame(dp)
frame.pack(pady=10)

# Create Listbox Widgets
lb = tk.Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 15),
    bd=3,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#464646',
    activestyle='none',
)
lb.pack(side=tk.LEFT, fill=tk.BOTH)

# Initializes TaskBox with default tasks
task_list = (
    'Post on LinkedIn',
    'Visit shop',
    'Buy cookies'
)
for item in task_list:
    lb.insert(tk.END, item)


# Create a ScrollBar
sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Widget for user Input
my_entry = tk.Entry(
    dp,
    font=('Times', 18)
)
my_entry.pack(pady=20)

#This creates another frame inside the main window dp for holding buttons and packs it with some padding.
button_frame = tk.Frame(dp)
button_frame.pack(pady=20)

# Defines newTask() and inserts new tasks to the listbox
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(tk.END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task!")

#This defines a function deleteTask() to delete a selected task from the listbox
def deleteTask():
    try:
        selected_task = lb.curselection()[0]
        lb.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create button widgets for adding and deleting tasks
addTask_btn = tk.Button(
    button_frame,
    text='Add Task',
    font=('times', 14),
    bg='#8B8378',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

delTask_btn = tk.Button(
    button_frame,
    text='Delete Task',
    font=('times', 14),
    bg='#8B8378',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Starting tkinter event loop
dp.mainloop()
