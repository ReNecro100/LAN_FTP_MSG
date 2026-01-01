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
from Tkinter_interaction import *

ftp_connection = FTP_connect('192.168.0.1')
FTP_get_messages(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA/messages', '/volume(sda1)/LAN_FTP_MSG_DATA')

if not FTP_check_login(ftp_connection, '/volume(sda1)/LAN_FTP_MSG_DATA'):
    login_window(ftp_connection)
main_window(ftp_connection)