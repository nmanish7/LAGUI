import subprocess


class PASSWORDSTATUS:
    stausFlag = {"LP": "Last password change",
                 "PE": "Password expires",
                 "PI": "Password inactive",
                 "AE": "Account expires",
                 "MNDBSC": "Minimum number of days between password change",
                 "MNDBPC": "Maximum number of days between password change",
                 "NOWBPE": "Number of days of warning before password expires"}

    def __init__(self, user, stausType):
        self.user = user
        self.stausType = stausType

    def check(self):

        try:
            if self.stausType == 'ALL':
                process = subprocess.check_output(
                    f'chage -l {self.user} | cut -d: -f 2', shell=True).decode('utf-8').split('\n')
                process.pop()

            else:
                process = subprocess.check_output(
                    f'chage -l {self.user} | grep "{self.stausFlag[self.stausType]}" | cut -d: -f 2 ', shell=True).decode('utf-8')

            #  print(self.user, self.stausFlag[self.stausType])
            return process
        except KeyError:
            return "Unkown key Error"
        return "Unknow Error, Contact Developer"


"""
Using Guides:

    username = "manish"
    passwordStatusCode = "ALL"

    user = PASSWORDSTATUS(username, passwordStatusCode)
    print(user.check())
"""

"""
Password Staus Code:

    ALL > Get ALL the Password Status Results in Array (LP, PE, PI, AE, MNDBSC, MNDBPC, NOWBPE)

    LP> Last password change                                     
    PE> Password expires                                        
    PI > Password inactive                                       
    AE > Account expires                                         
    MNDBSC > Minimum number of days between password change          
    MNDBPC > Maximum number of days between password change          
    NOWBPE > Number of days of warning before password expires  

"""
