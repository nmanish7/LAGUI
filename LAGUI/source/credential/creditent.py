import sys
import os
import subprocess

##========== Importin Other module with the help of Commands ==========##
from pathChanger import imp


try:
    imp('/login/')
    import login as log

except Exception as e:
    print("Module importing error", e)
##======================================================================##


class LOGIN:

    def __init__(self, user, passw):
        self.user = user
        self.password = passw

    def login(self):
        singin = log.LOGIN(self.user, self.password)
        # Here we know the passwor is correct or not if correct then it's return true.
        statusPasswd = singin.loginStatus()

        # Now here chekcing passwor correct or not if not then throwing a eror mesaage.

        if statusPasswd == True:
            os.system('su - {}'.format(self.user))
        else:
            print(statusPasswd)


# lo = LOGIN('manish', 'root')
# lo.login()


# abspath = os.path.abspath('.')
# currentdir = os.path.dirname(os.path.relpath(__file__))
# filePathScript = f'exec {abspath}/{currentdir}/exit.sh'
# filePathMe = f'exec {abspath}/{currentdir}/creditent.py'

# cmnd = f'{filePathMe} && {filePathScript}'


# os.system(cmnd)

# su --pty - manish -c "sudo useradd amnish"

# os.system('exec su - manish')
os.system('exit --help')
