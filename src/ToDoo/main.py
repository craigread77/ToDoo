import gui
import tkinter as tk

def main():
    root = tk.Tk()
    app = gui.ToDoAppGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()