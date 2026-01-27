from ftplib import FTP
from os import remove, system
import json
import time

def FTP_connect(address):
    ftp = FTP(address)
    ftp.login()
    return ftp

def FTP_get_logins(ftp_connection, dir, login, password, root):
    try:
        ftp_connection.cwd(dir)
    except:
        pass
    users = []
    ftp_connection.retrlines('RETR users.json', users.append)
    users[0] = json.loads(users[0])
    try:
        if users[0][login]==password:
            with open('login.txt', 'w') as log_file:
                log_file.writelines([login+'\n', password])
            root.destroy()
        else:
            root.title('Wrong password!')
    except:
        root.title('Wrong login!')

def FTP_check_login(ftp_connection, dir):
    with open('login.txt', 'r') as log_file:
        readedlines = log_file.readlines()
    if len(readedlines) == 0:
        return False
    else:
        try:
            ftp_connection.cwd(dir)
        except:
            pass
        users = []
        ftp_connection.retrlines('RETR users.json', users.append)
        users[0] = json.loads(users[0])
        try:
            if users[0][readedlines[0].replace('\n', '')] == readedlines[1]:
                return True
            else:
                return False
        except:
            return False

def FTP_send_message(ftp_connection, entry, dir, dir_login, root):
    from Tkinter_interaction import update_messages_on_the_screen
    with open('login.txt', 'r') as log_file:
        readedlines = log_file.readlines()
    if FTP_check_login(ftp_connection, dir_login):
        to_json = {
            "user": readedlines[0].replace('\n', ''),
            "date": time.time(),
            "message": entry.get()
        }
        filename = f'{time.time()}.json'
        with open(filename, 'w') as f:
            f.write(json.dumps(to_json))
        try:
            ftp_connection.cwd(dir)
        except:
            pass
        with open(filename, 'rb') as f:
            ftp_connection.storbinary(f'STOR {filename}', f)
        remove(filename)
        update_messages_on_the_screen(root, ftp_connection)
        entry.delete(0, len(entry.get()))
    else:
        pass

def FTP_get_messages(ftp_connection, dir, dir_login):
    if FTP_check_login(ftp_connection, dir_login):
        try:
            ftp_connection.cwd(dir)
        except:
            pass
        system('rd /s /q messages')
        system('md messages')
        last_five_messages = ftp_connection.nlst()[::-1][:5]
        while len(last_five_messages)<5:
            last_five_messages.append(f"None{time.time()}.json")
        msgs = []
        for i in range(5):
            if last_five_messages[i][:4]!="None":
                ftp_connection.retrlines(f'RETR {last_five_messages[i]}', msgs.append)
            else:
                msgs.append('{"user": "LAN-FTP-MSG", "date": 0, "message": "nothing"}')
            with open('messages/'+last_five_messages[i], 'w') as f:
                json.dump(msgs[i], f)
    else:
        pass