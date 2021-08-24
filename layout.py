from tkinter import *

from wx.core import Left
class MYjira():
    def __init__(self, root):
        background= Frame(root, bg="#38BEA6")#green background
        background.place(relheight=1, relwidth=1)
        frame = Frame(background, bg="white")#white sheet where we work on
        frame.place(relheight=0.8,relwidth=0.8, relx=0.1, rely=0.1)

        ToDo_frame = Frame(frame, bg="#F4AFAF")
        ToDo_frame.place(relheight=0.8,relwidth=0.2, relx=0.1, rely=0.1)
        ToDo_label = Label(ToDo_frame, text="To Do",bg="#F4AFAF")
        ToDo_label.config(font=(44))
        ToDo_label.pack()

        InProgress_frame = Frame(frame, bg="#AFF4EC")
        InProgress_frame.place(relheight=0.8,relwidth=0.2, relx=0.4, rely=0.1)
        InProgress_label = Label(InProgress_frame, text="In Progress",bg="#AFF4EC")
        InProgress_label.config(font=(44))
        InProgress_label.pack()

        done_frame = Frame(frame, bg="#AFF4B4")
        done_frame.place(relheight=0.8,relwidth=0.2, relx=0.7, rely=0.1)
        done_label = Label(done_frame, text="Done", bg="#AFF4B4")
        done_label.config(font=(44))
        done_label.pack()

        newTask = Button(frame, text="New Task", padx=20, pady=10)
        newTask.place(x=248, y=775)

        clearTasks = Button(frame, text="Clear", padx = 20, pady=10)
        clearTasks.place(x=1152, y=775)


        