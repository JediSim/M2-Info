from Message import Message

class BroadcastMessage(Message):
    def __init__(self, message, estampille, sender):
        super().__init__(message, estampille)
        self.sender = sender

    def getSender(self):
        return self.sender
    
    def __str__(self) -> str:
        return super().__str__() + " from " + str(self.sender)

