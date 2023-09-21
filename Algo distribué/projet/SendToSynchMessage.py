from MessageDedie import MessageDedie
from uuid import uuid4

class SendToSynchMessage(MessageDedie):
    def __init__(self, sender, receiver, message, estampille):
        super().__init__(message, estampille, receiver)
        self.sender = sender
        self.receiver = receiver
        self.id = uuid4()

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getId(self):
        return self.id

    def __str__(self):
        return "SendToSynchMessage: sender = " + str(self.sender) + " receiver = " + str(self.receiver) + " message = " + str(self.message)