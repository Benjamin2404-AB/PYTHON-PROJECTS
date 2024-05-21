from tkinter import *
from tkinter.ttk import * 
import tkinter as tk
from tkcalendar import Calendar

root = Tk()
root.geometry("600x400")
#changing the window icon from default tkinter to custom image
photo = tk.PhotoImage(file = "todo.png")
root.wm_iconphoto(False,photo)

# declaring string variable
# for storing title
title_var=tk.StringVar()
edit_title_var = tk.StringVar()
#id init
id=0
# Function to generate an increasing ID
def generate_id():
    global id
    id += 1
    return id


# #for date
# date_var=tk.StringVar()

#putting  list in a dictionary
To_do = {

}

def display_nested_dict(parent, To_do, row=6, column=0):
    for key, value in To_do.items():
        if isinstance(value, dict):
            tasks = tk.Label(parent, text="TASKS")
            label = tk.Label(parent, text=key)
            tasks.grid(row=5, column=0)
            label.grid(row=row, column=column, sticky="w", padx=5, pady=2)

             #adding delete button
            delete_btn = tk.Button(parent, text="Delete", command=lambda key=key: delete_task(key))
            delete_btn.grid(row=row + 2, column=column + 5, padx=5, pady=2)
      
            #adding edit button
            delete_btn = tk.Button(parent, text="Edit", command=lambda key=key: Edit_task(key))
            delete_btn.grid(row=row + 2, column=column + 6, padx=5, pady=2)

             # Add checkbox for marking as complete
            complete_var = tk.BooleanVar()
            complete_checkbox = tk.Checkbutton(parent, text="Mark as Complete", variable=complete_var,
                                                 command=lambda key=key: mark_as_complete(key, complete_var.get()))
            complete_checkbox.grid(row=row, column=column + 1, padx=5, pady=2)
            row += 1


            row += 1
            row = display_nested_dict(parent, value, row, column + 1)
        else:
            label_key = tk.Label(parent, text=key)
            label_key.grid(row=row, column=column, sticky="w", padx=5, pady=2)
            label_value = tk.Label(parent, text=value)
            label_value.grid(row=row, column=column + 1, sticky="w", padx=5, pady=2)
            
            row += 1

           

    return row

def Edit_task(key):
    edit_window = tk.Toplevel(root)
    edit_window.geometry("500x400")
    edit_window.title("Edit Task")

    def save_changes():
        new_title = edit_title_var.get()
        new_date = cal.get_date()
        To_do[key]['Task:'] = new_title
        To_do[key]['Date:'] = new_date
        edit_window.destroy()
        display_tasks()
    
    task_label = tk.Label(edit_window, text="New Title:")
    task_label.grid(row=0, column=0, padx=5, pady=5)
    edit_title_entry = tk.Entry(edit_window, textvariable=edit_title_var)
    edit_title_entry.grid(row=0, column=1, padx=5, pady=5)

    Date_label = tk.Label(edit_window, text="New Date:")
    Date_label.grid(row=1, column=0, padx=5, pady=5)
    cal = Calendar(edit_window, selectmode='day', year=2022, month=8, day=4)
    cal.grid(row=1, column=1, padx=5, pady=5)

    save_btn = tk.Button(edit_window, text="Save Changes", command=save_changes)
    save_btn.grid(row=2, columnspan=2, padx=5, pady=5)
    edit_title_var.set("")










def delete_task(key):
    del To_do[key]
    display_tasks()


def submit():

    for _ in range(1):
        id=generate_id()

    
    name=title_var.get()
    Date=cal.get_date()
    
    temp = {
        
        'Task:': name,
        'Date:': Date,
        'Status:': 'Incomplete'
        
    }
  
    To_do.update({id: temp})
    print(To_do)

     
    title_var.set("")
    display_nested_dict(root, To_do)
    # cal.selection_clear("")

def mark_as_complete(key, is_complete):
    if is_complete:
        To_do[key]['Status:'] = 'Complete'
        display_tasks()
    else:
        To_do[key]['Status:'] = 'Incomplete'


#creating label and inputs 
#title
Title = tk.Label(root, text = 'Title:', font=('calibre',10, 'bold'))
title_entry = tk.Entry(root,textvariable = title_var, font=('calibre',10,'normal'))

#date
Date_label = tk.Label(root, text = 'Due Date:', font=('calibre',10, 'bold'))
cal = Calendar(root, selectmode='day', year=2022, month=8, day=4)

#button
sub_btn=tk.Button(root,text = 'Submit', command = submit)






# placing the label and entry in
# the required position using grid
# method
# Title.grid(row=0,column=0)
# title_entry.grid(row=0,column=1)

# Date_label.grid(row=1,column=0)
# cal.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# sub_btn.grid(row=4,column=0)

def display_tasks():
    for widget in root.winfo_children():
        widget.destroy()
    Title = tk.Label(root, text='Title:', font=('calibre', 10, 'bold'))
    title_entry = tk.Entry(root, textvariable=title_var, font=('calibre', 10, 'normal'))

    # date
    Date_label = tk.Label(root, text='Date:', font=('calibre', 10, 'bold'))
    cal = Calendar(root, selectmode="day", year=2024, month=8, day=4)

    # button
    sub_btn = tk.Button(root, text='Submit', command=submit)

    Title.grid(row=0, column=0)
    title_entry.grid(row=0, column=1)

    Date_label.grid(row=1, column=0)
    cal.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    sub_btn.grid(row=4, column=0)

    display_nested_dict(root, To_do)





display_tasks()
root.title("to-do list")
root.mainloop()
