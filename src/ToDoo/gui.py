import tkinter as tk
from tkinter import messagebox
from lib import ToDoList

# TODO - GUI

class ToDoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = ToDoList()

        self.greeting = tk.Label(text="WOWOWOWWOWOOWOWOWWOOWOWWWOWOWOW HEYYYYYY")
        self.greeting.pack()



