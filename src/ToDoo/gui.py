import tkinter as tk
from tkinter import ttk
from lib import ToDoList
import constants as C

#TODO - Clean up bugs where notes can overwrite each other with rapid clicking
# Add Save/Load button to utilize JSON files

class ToDoAppGUI(tk.Tk):
    def __init__(self, args):
        super().__init__()

        self.title("To-Do List")
        self.geometry("800x800")

        self.todo_list = ToDoList()
        if args.loadfile:
            self.todo_list.set_filename(args.loadfile)
        self.todo_list.load_from_json()

        # Split window left/right
        l_frm =ttk.Frame(self, width=200)
        l_frm.pack(expand=False, fill='both', side='left')
        l_frm.pack_propagate(0)

        r_frm = ttk.Frame(self, width=300)
        r_frm.pack(expand=True, fill='both', side='right')
        r_frm.pack_propagate(0)

        self.r_txt = tk.Text(r_frm, bg="gray55", font=C.FONT_ARIEL)
        self.r_txt.pack(expand=True, fill='both', side='top')
        self.r_txt.bind("<FocusOut>", self.update_text)
        self.r_txt.bind("<Leave>", self.update_text)

        menubar = tk.Menu(self)        
        menubar.add_command(label='+', command=self.add_item)
        menubar.add_command(label='-', command=self.delete_item)

        self.config(menu=menubar)   

        self.item_lbox = tk.Listbox(l_frm, bg="gray30", font=C.FONT_ARIEL)
        self.item_lbox.pack(expand=True, fill='both')
        self.item_lbox.bind("<Double-Button-1>", self.edit_item)
        self.item_lbox.bind("<Button-1>", self.load_contents)

        self.load_items_to_listbox()
        self.load_contents

    def add_item(self, text=""):
        self.todo_list.add_item(text)
        self.todo_list.items[-1].set_title("New Note")
        self.load_items_to_listbox()
        self.load_contents
    
    def delete_item(self):
        selected_index = self.item_lbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.todo_list.delete_item(selected_index)
            self.load_items_to_listbox()
            self.load_contents

    def load_items_to_listbox(self):
        self.item_lbox.delete(0, tk.END)
        for item in self.todo_list.items:
            self.item_lbox.insert(tk.END, item.title)

    def edit_item(self, event):
        selected_index = self.item_lbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.item_txt = tk.Text(self.item_lbox, bg="gray55", height=1, width=30, font=C.FONT_ARIEL)
            self.item_txt.pack(expand=False, fill='none', side='left', anchor='n', pady=(20 * selected_index,0))
            self.item_txt.bind("<Return>", lambda _: self.update_item(selected_index, self.item_txt.get(1.0, tk.END)))
            self.item_txt.bind("<FocusOut>", lambda _: self.update_item(selected_index, self.item_txt.get(1.0, tk.END)))
            
            self.load_items_to_listbox()
            self.load_contents

    def update_item(self, index, text):
        self.todo_list.items[index].set_title(text)
        self.load_items_to_listbox()
        self.load_contents
        self.item_txt.destroy()
    
    def load_contents(self, event):
        selected_index = self.item_lbox.curselection()
        self.r_txt.delete(1.0, tk.END)
        if selected_index:
            selected_index = selected_index[0]
            item = self.todo_list.items[selected_index]
            self.r_txt.insert(tk.END, item.text)

    def update_text(self, event):
        selected_index = self.item_lbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            item = self.todo_list.items[selected_index]
            item.set_text(self.r_txt.get(1.0, tk.END))
            self.load_contents













        

        



