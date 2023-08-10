import constants as C
from datetime import datetime
import os
import logging
import json

# To-do list containing ListItem objects
# Later add tkinter GUI
class ToDoList:
    def __init__(self):
        self.items = []
        self.filename = C.SAVE_PATH
    
    def add_item(self, text=""):
        new_item = ListItem(text)
        self.items.append(new_item)
        self.save_to_json()

    def delete_item(self, index):
        try:
            self.items.pop(index)
            self.save_to_json()
        except IndexError as e:
            logging.critical(f'delete item index error: {e}')
            exit()

    def update_item(self, index, text=""):
        try:
            self.items[index].set_text(text)
            self.save_to_json()
        except IndexError as e:
            logging.critical(f'update item index error: {e}')
            exit()

    def set_due_date(self, index, date=""):
        self.items[index].set_due_date(date)
        self.save_to_json()
    
    def get_properties(self, *index):
        try:
            return f'\n'.join(map(lambda x: box(str(self.items[x])), index))
        except IndexError as e:
            logging.critical(f'get item index error: {e}')
            exit()

    def print_list(self):
        return f'\n'.join(map(lambda x: box(str(x)), self.items))

    def set_filename(self, filename):
        self.filename = get_loadfile(filename)

    def save_to_json(self):
        data = {
            "items": [item.serialize() for item in self.items]
        }
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
        self.update_indexes()

    def load_from_json(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.items = [ListItem.deserialize(item_data) for item_data in data["items"]]
                    self.update_indexes()
                    return self
            except json.decoder.JSONDecodeError as e:
                pass
    
    def update_indexes(self):
        for ix, item in enumerate(self.items):
            item.index = ix
    

class ListItem:
    def __init__(self, text="", due_date=""):
        current_time = get_time() # Ensure original modifiedDT = createDT
        self.text = text
        self.title = self.text[:15]
        self.create_dt = current_time
        self.last_modified_dt = current_time
        self.due_date = due_date
        self.overdue = self.due_date != "" and self.due_date <= get_time()
        self.index = None

    def __str__(self):
        lines = []
        for key, value in self.serialize().items():
            lines.append(f'"{key}" {" " * (18 - len(key))}=>    "{value}"')
        return "\n".join(lines)
    
    def serialize(self):
        return {
            "index": self.index,
            "title": self.title,
            "text": self.text,
            "create_dt": self.create_dt,
            "last_modified_dt": self.last_modified_dt,
            "due_date": self.due_date,
            "overdue": self.overdue
        }

    @classmethod
    def deserialize(cls, data):
        item = cls()
        item.index = data["index"]
        item.title = data["title"]
        item.text = data["text"]
        item.create_dt = data["create_dt"]
        item.last_modified_dt = data["last_modified_dt"]
        item.due_date = data["due_date"]
        item.overdue = data["overdue"]
        return item

    def set_title(self, title=""):
        self.title = title
        self.set_lmdate()

    def set_text(self, text=""):
        self.text = text
        self.set_lmdate()

    def set_lmdate(self):
        self.last_modified_dt = get_time()

    def set_due_date(self, date):
        self.due_date = date
        self.set_lmdate()
        self.set_overdue()
    
    def set_overdue(self):
        self.overdue = self.due_date <= get_time()

def get_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_loadfile(path="list.json"):
    if os.path.exists(path):
        return path
    else:
        logging.critical(f'{path} - is not accessible')
        exit()

def box(string, width=64, lpad=1, rpad=1, hor_char='_', ver_char='|'):
    outstr = ''
    outstr += f' {hor_char * width}\n'
    for line in string.split("\n"):
        outstr += f'{ver_char}{lpad * " "}{line}{(width - len(line) + rpad - lpad) * " "}{ver_char}\n'
    outstr += f' {hor_char * width}'
    return outstr
