#https://github.com/ReNecro100/LAN_FTP_MSG.git

#Модульность
#Гит
#ФТП

"""with open("Z:/messages.txt") as file:
    print(file.readlines())"""
# Так можно, но так не интересно

from FTP_interaction import *
ftp_connection = FTP_login('192.168.0.1')
FTP_get_messages(ftp_connection, 'volume(sda1)')