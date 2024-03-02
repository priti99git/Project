import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql


def add_task():
    task_string=task_field.get()
    if len(task_string)==0:
        messagebox.showinfo('error',"Field is Empty")
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values(?)',(task_string,))    
        list_update()
        task_field.delete(0,'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end',task)

def delete_task():
    try:
        the_value=task_listbox.get(task_listbox.curselection()) 
        if the_value in tasks:
            tasks.remove(the_value)    
            list_update()
            the_cursor.execute('delete from tasks where title=?',(the_value,))
    except:
        messagebox.showinfo('error','no task selected.Cannot delete')   

def delete_all_tasks():
    message_box=messagebox.askyesno('Delete ALL','are you sure?')
    if messagebox==True:
        while(len(tasks)!=0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()   

def clear_list():
    task_listbox.delete(0,'end')

def close():
    print(tasks)
    guiWindow.destroy()
 
def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks)!= 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from tasks'): 
        # using the append() method to insert the titles from the table in the list  
       tasks.append(row[0])      



if __name__=="__main__":
    guiWindow=tk.Tk()
    guiWindow.title("To-Do List Manager-PRITI")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#FAEBD7")

the_connection=sql.connect('listOfTasks.db')
the_cursor=the_connection.cursor()
the_cursor.execute('create table if not exists task (title text)')

tasks=[]
header_frame=tk.Frame(guiWindow,bg='#5BA0D0')
function_frame=tk.Frame(guiWindow,bg='#5BA0D0')
listbox_frame=tk.Frame(guiWindow,bg='#5BA0D0')

header_frame.pack(fill='both')
function_frame.pack(side="left",expand=True,fill="both")
listbox_frame.pack(side="right",expand=True,fill="both")

header_label=ttk.Label(
    header_frame,
    text="To-Do List",
    font=("Ink Free","30",'bold'),
    background="#5BA0D0",
    foreground="#000000"
)

header_label.pack(padx=20,pady=20)
task_label = ttk.Label(  
        function_frame,  
        text = "Enter the Task:",  
        font = ("Ink Free", "11", "bold"),  
        background = "#5BA0D0",  
        foreground = "#000000"  
    )  
task_label.place(x=30,y=40)

task_field=ttk.Entry(
    function_frame,
    font=("Ink Free","12"),
    width=18,
    background="#FFF8DC",
    foreground="#000000"

)
task_field.place(x=30,y=80)
add_button=ttk.Button(
    function_frame,
    text="Add Task",
    width=24,
    command=add_task

)
del_button=ttk.Button(
    function_frame,
    text="Delete Task",
    width=24,
    command=delete_task
)
exit_button=ttk.Button(
    function_frame,
    text="Exit",
    width=24,
    command=close
)
del_all_button = ttk.Button(  
    function_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all_tasks  
)  
add_button.place(x=30,y=120)
del_button.place(x=30,y=160)
del_all_button.place(x=30,y=200)
exit_button.place(x=30,y=240)

task_listbox=tk.Listbox(
    listbox_frame,
    width = 26, 
    font=('Ink Free','12'),
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#4E6590",  
    selectforeground = "#FFFFFF" 
)
task_listbox.place(x = 9, y = 20)  

retrieve_database()
list_update()
guiWindow.mainloop()
the_connection.commit()
the_cursor.close()












