# ToDoo

Simple command-line based 'To-Do' list application

Added GUI support with tkinter for fun but the main intention is to be used in the terminal

<b>Usage</b>
<code>main.py [options]</code>

<code>main.py [-h] 
[--add ADD [ADD ...]] 
[--delete <INDEX>] 
[--list] 
[--gui] 
[--loadfile <PATH_TO_JSON>] 
[--update <INDEX> <STRING>] 
[--get <INDEX>]
</code>

<b>Examples</b>
 - <code>main.py --add 'Pay water bill'</code>
 - <code>main.py --add 'Run server updates'</code>
 - <code>main.py --list</code>
 
 <code> \________________________________________________________________
| "index"              =>    "0"                                  |
| "title"              =>    "Pay water bill"                     |
| "text"               =>    "Pay water bill"                     |
| "create_dt"          =>    "2023-08-19 01:31:54"                |
| "last_modified_dt"   =>    "2023-08-19 01:31:54"                |
| "due_date"           =>    ""                                   |
| "overdue"            =>    "False"                              |
 \________________________________________________________________
 \________________________________________________________________
| "index"              =>    "1"                                  |
| "title"              =>    "Run server upda"                    |
| "text"               =>    "Run server updates"                 |
| "create_dt"          =>    "2023-08-19 01:35:26"                |
| "last_modified_dt"   =>    "2023-08-19 01:35:26"                |
| "due_date"           =>    ""                                   |
| "overdue"            =>    "False"                              |
 \________________________________________________________________</code>

----
 - <code>main.py --get 0</code>

 <code> \________________________________________________________________
| "index"              =>    "0"                                  |
| "title"              =>    "Pay water bill"                     |
| "text"               =>    "Pay water bill"                     |
| "create_dt"          =>    "2023-08-19 01:31:54"                |
| "last_modified_dt"   =>    "2023-08-19 01:31:54"                |
| "due_date"           =>    ""                                   |
| "overdue"            =>    "False"                              |
 \________________________________________________________________
</code>

---
- <code>main.py --delete 0  # delete item at index</code>
- <code>main.py --update 0 'Pay insurance'</code>
- <code>main.py --loadfile myList.json'</code>

```json
{
  "items": [
      {
        "index": 0,
        "title": "Pay water bill",
        "text": "Pay water bill",
        "create_dt": "2023-08-19 01:31:54",
        "last_modified_dt": "2023-08-19 01:41:50",
        "due_date": "",
        "overdue": false
    },
    {
        "index": 1,
        "title": "Run server upda",
        "text": "Run server updates",
        "create_dt": "2023-08-19 01:35:26",
        "last_modified_dt": "2023-08-19 01:35:26",
        "due_date": "",
        "overdue": false
    }
  ]
}
```

- <code>main.py --gui</code>

![image](https://github.com/craigread77/ToDoo/assets/27896820/350a47a7-b01e-4079-b190-e02e6a4f5406)


