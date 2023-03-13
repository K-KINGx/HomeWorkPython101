import tkinter as tk
import csv
from datetime import datetime

def writecsv(datalist):
    with open('datatodolish.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def readcsv():
    with open('datatodolish.csv',encoding='utf-8',newline='') as file :
        fr = csv.reader(file)
        data = list(fr)
    return data

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry('260x300')

        # create a LabelFrame to group the to-do list widgets
        self.list_frame = tk.LabelFrame(master, text="To-Do List")
        self.list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=tk.YES)

        # create a Frame to hold the task entry and add button
        self.task_frame = tk.Frame(self.list_frame)
        self.task_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=tk.YES)

        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.task_frame, textvariable=self.task_var)
        self.task_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task,)
        self.add_button.pack(side=tk.RIGHT, padx=10)
        

        self.task_list = tk.Listbox(self.list_frame)
        self.task_list.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.list_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=10)


    def add_task(self):
        task = self.task_var.get()
        t = datetime.now().strftime('%d %m %Y  %H:%M')
        data = self.task_var.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
        text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
        writecsv(text)
        self.tasks.append(task)
        self.task_list.insert(tk.END, task)
        self.task_var.set("")

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_list.get(selected_task[0])
            self.tasks.remove(task)
            self.task_list.delete(selected_task)

root = tk.Tk()
todo_list = TodoList(root)
root.mainloop()
