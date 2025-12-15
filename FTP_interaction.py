from ftplib import FTP
from os import remove

def FTP_login(address):
    ftp = FTP(address)
    ftp.login()
    return ftp

def FTP_get_messages(ftp_connection, dir):
    ftp_connection.cwd(dir)
    with open('messages.txt', 'wb') as messages:
        ftp_connection.retrbinary('RETR messages.txt', messages.write)
    with open('messages.txt', 'r') as messages:
        print(messages.readlines())
    remove('messages.txt')
