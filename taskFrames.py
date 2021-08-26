#toDo_frame, inProgress_frame, done_frame
from tkinter import *

class toDo():
    def __init__(self, frame):
        ToDo_frame = Frame(frame, bg="#F4AFAF")
        ToDo_frame.place(relheight=0.8,relwidth=0.2, relx=0.1, rely=0.1)
        ToDo_label = Label(ToDo_frame, text="To Do",bg="#F4AFAF")
        ToDo_label.config(font=(44))
        ToDo_label.pack()

class inProgress():
    def __init__(self, frame):
        InProgress_frame = Frame(frame, bg="#AFF4EC")
        InProgress_frame.place(relheight=0.8,relwidth=0.2, relx=0.4, rely=0.1)
        InProgress_label = Label(InProgress_frame, text="In Progress",bg="#AFF4EC")
        InProgress_label.config(font=(44))
        InProgress_label.pack()
        

class done():
    def __init__(self, frame):
        done_frame = Frame(frame, bg="#AFF4B4")
        done_frame.place(relheight=0.8,relwidth=0.2, relx=0.7, rely=0.1)
        done_label = Label(done_frame, text="Done", bg="#AFF4B4")
        done_label.config(font=(44))
        done_label.pack()

class stickNotes():
    def __init__(self,frame):
        stickNote = Frame(frame, bg="white")
        stickNote.grid(ipadx=10, ipady=10)
        