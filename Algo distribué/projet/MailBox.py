class MailBox:

    def __init__(self):
        self.messages = []
        self.messagesSynch = []

    def isEmpty(self):
        return len(self.messages) == 0
    
    def getMsg(self):
        return self.messages.pop(0)
    
    def addMessage(self, message):
        self.messages.append(message)

    def addMessageSynch(self, message):
        self.messagesSynch.append(message)

    def getMsgSynch(self):
        return self.messagesSynch.pop(0)
    
    def getMsgFromSender(self, sender):
        for i in range(len(self.messagesSynch)):
            if self.messagesSynch[i].getSender() == sender:
                return self.messagesSynch[i]
        return None

    def isEmptySynch(self):
        return len(self.messagesSynch) == 0