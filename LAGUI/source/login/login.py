import spwd  # Shadow password database (to read /etc/shadow).
import crypt  # Interface to crypt(3), to encrypt passwords.

##========== Importin Other module with the help of Commands ==========##
from pathChanger import imp


try:
    imp('/passwd_attrib/')
    import passwordStatus as pS

except Exception as e:
    print("Module importing error", e)
##======================================================================##

# This is an password status checker module.


class LOGIN:
    def __init__(self, username, password):
        self.user = username
        self.pasword = password

    def loginStatus(self):
        try:
            passwdStatus = pS.PASSWORDSTATUS(self.user, 'ALL')
            pStatus = passwdStatus.check()

            # Here we get all the password status in the form of arrya in 'pStatus'
            #(LP, PE, PI, AE, MNDBSC, MNDBPC, NOWBPE)

        except Exception as k:
            print(k)

        try:
            enc_pwd = spwd.getspnam(self.user)[1]

            if pStatus[1] != ' never' or pStatus[2] != ' never':
                return "Password Expired or Inactive. Please contact System Admin."

            elif enc_pwd in ["NP", "!", "", None]:
                return "User '%s' has no password set. Please contact System Admin" % self.user

            elif enc_pwd[0:1] in ["LK", "*", "L", '!']:
                return "User account is locked. Please Contact System Admin"

            elif crypt.crypt(self.pasword, enc_pwd) == enc_pwd:
                return True
            else:
                return "Incorrect password"
        except KeyError:
            return "User '%s' not found" % self.user
        return "Unknown Error, Contact Developer !"


# Usage Technique Example When you are importing to other files:
"""
import login

user = 'manish'
passwd = '1234'

log = login.LOGIN(user,passwd)
status=log.loginStatus()

print(status)

"""

# Usage above technique when you are importing my module  to another code

# Code Develop by Manish
