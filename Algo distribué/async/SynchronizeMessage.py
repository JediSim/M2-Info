from Message import Message

class SynchronizeMessage(Message):
    def __init__(self, sender, estampille):
        super().__init__("synchronize", estampille)
        self.sender = sender

    def getSender(self):
        return self.sender

    def __str__(self):
        return f"from {self.sender} at {self.estampille} synchronize"