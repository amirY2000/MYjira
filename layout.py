import tkinter as tk
class MYjira():
    def __init__(self, root):
        background= tk.Frame(root, bg="#38BEA6")#green background
        background.place(relheight=1, relwidth=1)
        frame = tk.Frame(background, bg="white")#white sheet where we work on
        frame.place(relheight=0.8,relwidth=0.8, relx=0.1, rely=0.1)

        ToDo_frame = tk.Frame(frame, bg="#F4AFAF")
        ToDo_frame.place(relheight=0.8,relwidth=0.2, relx=0.1, rely=0.1)
        InProgress_frame = tk.Frame(frame, bg="#AFF4EC")
        InProgress_frame.place(relheight=0.8,relwidth=0.2, relx=0.4, rely=0.1)
        done_frame = tk.Frame(frame, bg="#AFF4B4")
        done_frame.place(relheight=0.8,relwidth=0.2, relx=0.7, rely=0.1)
        