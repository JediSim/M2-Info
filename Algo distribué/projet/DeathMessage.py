from Message import Message

class DeathMessage(Message):
    def __init__(self, estampille, sender):
        super().__init__("death", estampille)
        self.sender = sender

    def getSender(self):
        return self.sender

    def __str__(self):
        return super().__str__() + " death : " + str(self.sender)