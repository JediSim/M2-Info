from Message import Message

class MessageDedie(Message):
    
    def __init__(self, message, estampille, dest):
        super().__init__(message, estampille)
        self.dest = dest

    def getDest(self):
        return self.dest
    
    def __str__(self) -> str:
        return super().__str__() + " to " + str(self.dest)
    