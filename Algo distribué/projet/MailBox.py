class MailBox:

    def __init__(self):
        self.messages = []

    def isEmpty(self):
        return len(self.messages) == 0
    
    def getMsg(self):
        return self.messages.pop(0)
    
    def addMessage(self, message):
        self.messages.append(message)