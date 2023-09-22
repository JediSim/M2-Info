from Message import Message

class ConnectionMessage(Message):
    def __init__(self, message, estampille, id, name):
        super().__init__(message, estampille)
        self.id = id
        self.name = name

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def __str__(self):
        return "ConnectionMessage: " + super().__str__() + " id : " + str(self.id)