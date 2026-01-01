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

def update_messages_on_the_screen(root, ftp_connection):
    FTP_get_messages(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA/messages', '/volume(sda1)/LAN_FTP_MSG_DATA')
    msgs = listdir('messages')
    for i in range(5):
        with open(f'messages/{msgs[5 - 1 - i]}', 'r') as msg_file:
            message = json.loads(msg_file.read())
        message = json.loads(message)
        create_frame('@' + message["user"], message["message"]).grid(row=i + 1, column=0, padx=4, pady=4, columnspan=4)

def login_window(ftp_connection):

    root = Tk()
    root.title('LAN-FTP-MSG')
    root.geometry("300x200")

    login_label = ttk.Label(text="Login page:")
    login_label.grid(row=0, column=1, padx=4, pady=4)

    login_label = ttk.Label(text="Login:")
    login_label.grid(row=1, column=0, padx=4, pady=4)

    login_entry = ttk.Entry()
    login_entry.grid(row=1, column=1, padx=4, pady=4)

    password_label = ttk.Label(text="Password:")
    password_label.grid(row=2, column=0, padx=4, pady=4)

    password_entry = ttk.Entry()
    password_entry.grid(row=2, column=1, padx=4, pady=4)

    btn = ttk.Button(text="Log in", command=lambda: FTP_get_logins(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA', login_entry.get(), password_entry.get(), root))
    btn.grid(row=3, column=1, padx=4, pady=4)

    root.mainloop()

def main_window(ftp_connection):

    root = Tk()
    root.title('LAN-FTP-MSG')
    root.geometry("350x500")

    message_entry = ttk.Entry(width=50)
    message_entry.grid(row=0, column=0, padx=4, pady=4, columnspan=3)

    btn = ttk.Button(text="➤", width=3, command=lambda: FTP_send_message(ftp_connection, message_entry, '/volume(sda1)/LAN_FTP_MSG_DATA/messages', '/volume(sda1)/LAN_FTP_MSG_DATA', root))
    btn.grid(row=0, column=3, padx=4, pady=4)

    update_messages_on_the_screen(root, ftp_connection)

    root.mainloop()