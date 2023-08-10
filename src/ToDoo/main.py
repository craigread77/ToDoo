import gui
import lib
import tkinter as tk
import argparse
import logging

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='ToDoo',
        description='Command-based ToDo list (optional GUI but not recommended)'
    )
    parser.add_argument('--add', nargs='+')
    parser.add_argument('--delete', type=int, nargs=1)
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--gui', action='store_true')
    parser.add_argument('--loadfile')
    parser.add_argument('--update', nargs='+')
    parser.add_argument('--get', type=int, nargs='+')

    args = parser.parse_args()

    if args.update and len(args.update) < 2:
        parser.error("--update takes at least 2 arguments. Usage --update [index] [text]")

    return args

def main(args):
    if args.gui:
        gui_app = gui.ToDoAppGUI(args)
        gui_app.mainloop()
    else:
        app = lib.ToDoList()

        if args.loadfile:
            app.set_filename(args.loadfile)
        
        app.load_from_json()

        if args.delete:
            app.delete_item(args.delete[0])
        
        if args.add:
            app.add_item(" ".join(args.add))
        
        if args.update:
            app.update_item(int(args.update[0]), " ".join(args.update[1:]))
        
        if args.list:
            print(app.print_list())

        if args.get:
            print(app.get_properties(*args.get))
    
    

if __name__ == '__main__':
    logging.getLogger(__name__)
    arguments = parse_arguments()
    main(arguments)