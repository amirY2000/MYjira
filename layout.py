#Overall layout
from tkinter import *
from taskFrames import *

class MYjira():
    def __init__(self, root):
        background= Frame(root, bg="#38BEA6")#green background
        background.place(relheight=1, relwidth=1)

        frame = Frame(background, bg="white")#white sheet where we work on
        frame.place(relheight=0.8,relwidth=0.8, relx=0.1, rely=0.1)

        toDo_frame = toDo(frame)
        inProgress_frame = inProgress(frame)
        done_frame = done(frame)

        newTask = Button(frame, text="New Task", padx=20, pady=10)
        newTask.place(x=248, y=775)

        clearTasks = Button(frame, text="Clear", padx = 20, pady=10)
        clearTasks.place(x=1152, y=775)


        