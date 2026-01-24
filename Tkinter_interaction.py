from tkinter import *
from tkinter import ttk
from os import listdir

import json
from FTP_interaction import *

def create_frame(user, message):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, width=300)

    label = ttk.Label(frame, text=user)
    label.grid(row=0, column=0, padx=4, pady=4, sticky=W)

    label = ttk.Label(frame, text=message)
    label.grid(row=1, column=0, padx=4, pady=4, sticky=W)

    return frame

def destroy_all_frames(root):
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.destroy()

def update_messages_on_the_screen(root, ftp_connection):
    FTP_get_messages(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA/messages', '/volume(sda1)/LAN_FTP_MSG_DATA')
    msgs = listdir('messages')
    destroy_all_frames(root)
    for i in range(5):
        with open(f'messages/{msgs[5 - 1 - i]}', 'r') as msg_file:
            message = json.loads(msg_file.read())
        message = json.loads(message)
        create_frame('@' + message["user"], message["message"]).grid(row=i + 1, column=0, padx=4, pady=4, columnspan=4, sticky="ew")
    root.after(1000, lambda: update_messages_on_the_screen(root, ftp_connection))