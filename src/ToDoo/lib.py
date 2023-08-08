import constants as C
from datetime import datetime
import json

# To-do list containing ListItem objects
# Later add tkinter GUI
class ToDoList:
    def __init__(self):
        self.items = []
    
    def add_item(self, text=""):
        new_item = ListItem(text)
        self.items.append(new_item)

    def delete_item(self, index):
        self.items.pop(index)

    def update_item(self, index, text=""):
        self.items[index].set_text(text)

    def set_due_date(self, index, date=""):
        self.items[index].set_due_date(date)

    def print_list(self):
        print(f'\n{"-" * 48}\n'.join(map(lambda x: str(x), self.items)))

    def save_to_json(self, filename=C.SAVE_PATH):
        data = {
            "items": [item.serialize() for item in self.items]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename=C.SAVE_PATH):
        with open(filename, "r") as file:
            data = json.load(file)
            self.items = [ListItem.deserialize(item_data) for item_data in data["items"]]
            return self
    

class ListItem:
    def __init__(self, text="", due_date=""):
        current_time = get_time() # Ensure original modifiedDT = createDT
        self.text = text
        self.title = self.text[:10]
        self.create_dt = current_time
        self.last_modified_dt = current_time
        self.due_date = due_date
        self.overdue = self.due_date != "" and self.due_date <= get_time()

    def __str__(self):
        lines = []
        for key, value in self.serialize().items():
            lines.append(f'"{key}" {" " * (18 - len(key))}=>    "{value}"')
        return "\n".join(lines)
    
    def serialize(self):
        return {
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
