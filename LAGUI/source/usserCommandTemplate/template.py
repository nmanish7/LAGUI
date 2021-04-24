import pexpect


class COMANDTEMPLATE:
    def __init__(self, username, password, cmnd):
        self.username = username
        self.command = cmnd
        self.default = f"su --pty - {self.username} -c \"{self.command}\""
        self.password = password

    def executingCommand(self):
        userCommand = pexpect.spawn(self.default)
        nextLineExpectation = userCommand.expect(['password', ''])
        userCommand.sendline(self.password)
        afterExecutionMessage = userCommand.read().decode('utf-8').split('\n')
        afterExecutionMessage.pop()
        try:
            if afterExecutionMessage[0] == f'{self.password}\r':
                afterExecutionMessage.remove(f'{self.password}\r')
            if afterExecutionMessage[-1] == f'{self.password}\r':
                afterExecutionMessage.pop()
        except:
            pass

        if afterExecutionMessage[0] == f'{"[sudo] password for "}{self.username}: \r':
            afterExecutionMessage.pop(0)
        return afterExecutionMessage


etc = COMANDTEMPLATE('manish', 'root', 'sudo useradd koka')
etc = COMANDTEMPLATE(
    'manish', 'root', 'sudo cat /etc/passwd')

print(etc.executingCommand())


##==================== Usage Instruction =====================##
"""

username = '' //Linux user name
password = ''  //Password of username
command = ''    //Command you want to execute (Here you include sudo or non-sudo both commands.. e.g.: cat /etc/passwd , sudo useradd rani)

variable = COMANDTEMPLATE(username, password, command) // Calling Class

messageReturn = variable.executingCommand() // Here you get return messages after executing the commmands e.g. You get some value if command run successfully or you get error message if it's failed. All the element will be as a value of one line each.

print(messageReturn)

"""
##====================== END Aggremment ======================##
