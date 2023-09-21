from BroadcastMessage import BroadcastMessage
from uuid import uuid4

class BroadcastSynchMessage(BroadcastMessage):

    def __init__(self, message, estampille, sender):
        super().__init__(message, estampille, sender)
        self.id = uuid4()

    def getId(self):
        return self.id
    
    def __str__(self) -> str:
        return super().__str__() + " id : " + str(self.id)
        