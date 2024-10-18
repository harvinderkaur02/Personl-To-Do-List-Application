#Personal to-do List Application using Python

import tkinter as tk
from tkinter import messagebox, ttk
import json

# Task class definition
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✔️" if self.completed else "❌"
        return f"{self.title} [{self.category}] - {status}"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Function to update the listbox display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, str(task))

# Function to add a new task
def add_task():
    title = title_entry.get()
    description = description_entry.get()
    category = category_var.get()

    if not title or not category:
        messagebox.showwarning("Input Error", "Title and category are required.")
        return
    
    task = Task(title, description, category)
    tasks.append(task)
    update_task_list()
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added successfully!")

# Function to mark the selected task as completed
def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index].mark_completed()
        update_task_list()
        messagebox.showinfo("Success", "Task marked as completed!")
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to delete the selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        update_task_list()
        messagebox.showinfo("Success", "Task deleted successfully!")
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to save tasks and exit the application
def exit_app():
    save_tasks(tasks)
    root.quit()

# Load existing tasks
tasks = load_tasks()

# Tkinter GUI setup
root = tk.Tk()
root.title("Interactive To-Do List Application")
root.geometry("500x400")
root.resizable(False, False)

# Frames to organize layout
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

# Task title input
title_label = tk.Label(top_frame, text="Task Title:")
title_label.grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(top_frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

# Task description input
description_label = tk.Label(top_frame, text="Description:")
description_label.grid(row=1, column=0, padx=5, pady=5)
description_entry = tk.Entry(top_frame, width=30)
description_entry.grid(row=1, column=1, padx=5, pady=5)

# Task category input (Dropdown)
category_label = tk.Label(top_frame, text="Category:")
category_label.grid(row=2, column=0, padx=5, pady=5)
category_var = tk.StringVar()
category_options = ["Work", "Personal", "Urgent", "Other"]
category_menu = tk.OptionMenu(top_frame, category_var, *category_options)
category_menu.grid(row=2, column=1, padx=5, pady=5)
category_var.set(category_options[0])  # Set default category

# Listbox to display tasks
task_listbox = tk.Listbox(middle_frame, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(side="left", padx=10, pady=10)

# Scrollbar for Listbox
scrollbar = tk.Scrollbar(middle_frame)
scrollbar.pack(side="right", fill="y")

# Connect scrollbar to the listbox
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons for task actions
add_button = tk.Button(bottom_frame, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=0, padx=10, pady=5)

complete_button = tk.Button(bottom_frame, text="Mark Completed", width=15, command=mark_completed)
complete_button.grid(row=0, column=1, padx=10, pady=5)

delete_button = tk.Button(bottom_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=0, column=2, padx=10, pady=5)

exit_button = tk.Button(bottom_frame, text="Save and Exit", width=15, command=exit_app)
exit_button.grid(row=0, column=3, padx=10, pady=5)

# Populate the listbox with tasks
update_task_list()

# Start the Tkinter main loop
root.mainloop()
