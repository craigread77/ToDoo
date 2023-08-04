from datetime import datetime

# ToDo list containing ListItem objects
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
        print("\n".join(map(lambda x: str(x), self.items)))

class ListItem:
    def __init__(self, text=""):
        current_time = get_time() # Ensure original modifiedDT = createDT
        self.text = text
        self.create_dt = current_time
        self.last_modified_dt = current_time
        self.due_date = ""
        self.due_warning = "GREEN" # RED if overdue

    def __str__(self):
        return f'{self.text}\t|\t{self.create_dt}\t|\t{self.due_date}\t|\t{self.due_warning}'

    def set_text(self, text=""):
        self.text = text
        self.set_lmdate()

    def set_lmdate(self):
        self.last_modified_dt = get_time()

    def set_due_date(self, date):
        self.due_date = date
        self.set_lmdate()
        self.check_due()
    
    def check_due(self):
        self.due_warning = "RED" if self.due_date <= get_time() else "GREEN"

def get_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
