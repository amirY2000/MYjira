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

class newTask():
    def __init__(self, frame):
        popUp = Toplevel(frame)
        popUp.title("New Task")
        popUp.geometry("400x285")
        popUp.config(bg="#38A1C5")

        title_frame = Frame(popUp, bg="#38A1C5")
        title_frame.pack(ipadx=80, pady=2.5)
        title = Label(title_frame, text="Title", bg="#38A1C5", font=(15))
        title.grid(row=0,column=0)
        title_feild = Entry(title_frame, font=("Helvetica"))
        title_feild.grid(row=0,column=1, padx=61)
        
        dueDate_frame = Frame(popUp, bg="#38A1C5")
        dueDate_frame.pack(ipadx=80, pady=2.5)
        dueDate = Label(dueDate_frame, text="Due Date", bg="#38A1C5", font=(15))
        dueDate.grid(row=0,column=0)
        dueDate_feild = Entry(dueDate_frame, font=("Helvetica"))
        dueDate_feild.grid(row=0,column=1, padx=23)

        description_frame = Frame(popUp, bg="#38A1C5")
        description_frame.pack(ipadx=80, pady=5)

        description = Label(description_frame, text="Description", bg="#38A1C5", font=(15))
        description.grid(row=3, column=0)
        description_feild = Text(description_frame, width=30, height=10, font=("Helvetica"))
        description_feild.grid(row=3,column=1, padx=10)

        buttonFrame = Frame(popUp, bg="#38A1C5")
        buttonFrame.pack()

        saveButton = Button(buttonFrame, text="Save")
        saveButton.grid(row=0, column=0, padx=50, ipadx=20)

        cancelButton = Button(buttonFrame, text="Cancel", command=popUp.destroy)
        cancelButton.grid(row=0, column=1, padx=50, ipadx=20)
        
        
    