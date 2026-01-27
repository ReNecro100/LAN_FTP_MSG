from tkinter import *
from tkinter import ttk

import json
from Tkinter_interaction import *

ftp_connection = FTP_connect('192.168.0.1')

if not FTP_check_login(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA'):
    #Окно входа
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

    btn = ttk.Button(text="Log in",
                     command=lambda: FTP_get_logins(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA', login_entry.get(),
                                                    password_entry.get(), root))
    btn.grid(row=3, column=1, padx=4, pady=4)

    root.mainloop()

#Главное окно
root = Tk()
root.title('LAN-FTP-MSG')
root.geometry("350x500")

message_entry = ttk.Entry(width=50)
message_entry.grid(row=0, column=0, padx=4, pady=4, columnspan=3)

btn = ttk.Button(text="➤", width=3, command=lambda: FTP_send_message(ftp_connection, message_entry, '/volume(sda1)/LAN_FTP_MSG_DATA/messages', '/volume(sda1)/LAN_FTP_MSG_DATA', root))
btn.grid(row=0, column=3, padx=4, pady=4)

update_messages_on_the_screen(root, ftp_connection)

root.mainloop()