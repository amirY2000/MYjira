#Overall layout
from tkinter import font
from taskFrames import *

class MYjira():
    def __init__(self, root):
        background= Frame(root, bg="#38BEA6")#green background
        background.place(relheight=1, relwidth=1)

        self.frame = Frame(background, bg="white")#white sheet where we work on
        self.frame.place(relheight=0.8,relwidth=0.8, relx=0.1, rely=0.1)

        toDo_frame = toDo(self.frame)
        inProgress_frame = inProgress(self.frame)
        done_frame = done(self.frame)

        newTask = Button(self.frame, text="New Task", padx=20, pady=10, command=self.newTask_command)
        newTask.place(x=248, y=775)

        clearTasks = Button(self.frame, text="Clear", padx = 20, pady=10)
        clearTasks.place(x=1152, y=775)

    def newTask_command(self):
        popUp = newTask(self.frame)