import lib

def main():
    list = lib.ToDoList()
    list.add_item("this is a test")
    list.add_item("this is also test")
    list.add_item("this is another test")
    list.add_item()
    list.update_item(2, "blaahhhhh")
    list.set_due_date(2, "2022-01-01 00:00:00")
    list.delete_item(0)
    list.print_list()

if __name__ == '__main__':
    main()