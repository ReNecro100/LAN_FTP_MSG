#https://github.com/ReNecro100/LAN_FTP_MSG.git

#Модульность
#Гит
#ФТП

"""with open("Z:/messages.txt") as file:
    print(file.readlines())"""
# Так можно, но так не интересно
from tkinter import *
from tkinter import ttk

import json
from FTP_interaction import *

root = Tk()
root.geometry("300x250")

ftp_connection = FTP_connect('192.168.0.1')

login_entry = ttk.Entry()
login_entry.pack(anchor=NW, padx=6, pady=6)

password_entry = ttk.Entry()
password_entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Log in", command=lambda: FTP_get_logins(ftp_connection, 'volume(sda1)/LAN_FTP_MSG_DATA', login_entry.get(), password_entry.get()))
btn.pack(anchor=NW, padx=6, pady=6)

root.mainloop()