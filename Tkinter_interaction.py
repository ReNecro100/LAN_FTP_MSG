from tkinter import *
from tkinter import ttk
from os import listdir

from FTP_interaction import *

def create_frame(user, message):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, width=300)

    label = ttk.Label(frame, text=user)
    label.grid(row=0, column=0, padx=4, pady=4, sticky=W)

    label = ttk.Label(frame, text=message, wraplength=300)
    label.grid(row=1, column=0, padx=4, pady=4, sticky=W)

    return frame

def destroy_all_frames(root):
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.destroy()

def update_messages_on_the_screen(root, connection):
    connection.FTP_get_messages('/volume(sda1)/LAN_FTP_MSG_DATA')
    destroy_all_frames(root)
    for i, j in enumerate(connection.messages):
        message = json.loads(j)
        create_frame('@' + message["user"], message["message"]).grid(row=i + 1, column=0, padx=4, pady=4, columnspan=4, sticky="ew")
    root.after(1000, lambda: update_messages_on_the_screen(root, Connection))