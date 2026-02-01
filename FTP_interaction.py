from ftplib import FTP
from os import remove, system
import json
import time

#Наверное сделаю классом это дело... Не сейчас однако
class Connection:
    def __init__(self, address):
        ftp = FTP(address)
        ftp.login()
        self.ftp_connection = ftp
        self.messages = []

    def FTP_get_logins(self, dir, login, password, root):
        try:
            self.ftp_connection.cwd(dir)
        except:
            pass
        users = []
        self.ftp_connection.retrlines('RETR users.json', users.append)
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

    def FTP_check_login(self, dirr):
        with open('login.txt', 'r') as log_file:
            readedlines = log_file.readlines()
        if len(readedlines) == 0:
            return False
        else:
            try:
                self.ftp_connection.cwd(dirr)
            except:
                pass
            users = []
            self.ftp_connection.retrlines('RETR users.json', users.append)
            users[0] = json.loads(users[0])
            try:
                if users[0][readedlines[0].replace('\n', '')] == readedlines[1]:
                    return True
                else:
                    return False
            except:
                return False

    def FTP_send_message(self, entry, dir, dir_login, root):
        from Tkinter_interaction import update_messages_on_the_screen
        with open('login.txt', 'r') as log_file:
            readedlines = log_file.readlines()
        if self.FTP_check_login(dir_login):
            to_json = {
                "user": readedlines[0].replace('\n', ''),
                "date": time.time(),
                "message": entry.get()
            }
            filename = f'{time.time()}.json'
            with open(filename, 'w') as f:
                f.write(json.dumps(to_json))
            try:
                self.ftp_connection.cwd(dir)
            except:
                pass
            with open(filename, 'rb') as f:
                self.ftp_connection.storbinary(f'STOR {filename}', f)
            remove(filename)
            update_messages_on_the_screen(root, self.ftp_connection)
            entry.delete(0, len(entry.get()))
        else:
            pass

    def FTP_get_messages(self, dir_login):
        self.messages = []
        if self.FTP_check_login(dir_login):
            last_five_messages = self.ftp_connection.nlst()[::-1][:5]

            for i in range(5):
                if last_five_messages[i][:4]!="None":
                    self.ftp_connection.retrlines(f'RETR {last_five_messages[i]}', self.messages.append)
                else:
                    self.messages.append('{"user": "LAN-FTP-MSG", "date": 0, "message": "nothing"}')
                """with open('messages/'+last_five_messages[i], 'w') as f:
                    json.dump(self.messages[i], f)"""
        else:
            pass