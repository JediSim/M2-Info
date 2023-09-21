from MessageDedie import MessageDedie

class AcknowledgeMessage(MessageDedie):

    def __init__(self, message, estampille, dest, id):
        super().__init__(message, estampille, dest)
        self.id = id

    def getId(self):
        return self.id
    
    def __str__(self) -> str:
        return super().__str__() + " id : " + str(self.id)
