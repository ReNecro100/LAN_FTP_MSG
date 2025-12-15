from ftplib import FTP
from os import remove
import json

def FTP_connect(address):
    ftp = FTP(address)
    ftp.login()
    return ftp

def FTP_get_logins(ftp_connection, dir, login, password):
    try:
        ftp_connection.cwd(dir)
    except:
        pass
    users = []
    ftp_connection.retrlines('RETR users.json', users.append)
    users[0] = json.loads(users[0])
    try:
        if users[0][login]==password:
            print("ura")
        else:
            print('neljzia')
    except:
        print('neljzia')

"""def FTP_get_messages(ftp_connection, dir):
    try:
        ftp_connection.cwd(dir)
    except:
        pass
    with open('messages.txt', 'wb') as messages:
        ftp_connection.retrbinary('RETR messages.txt', messages.write)
    remove('messages.txt')""" #Eto potom, tochno ne v tekstovom formate

#def FTP_send_message(ftp_connection, dir, message):