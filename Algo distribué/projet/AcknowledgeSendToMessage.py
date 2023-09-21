from AcknowledgeMessage import AcknowledgeMessage

class AcknowledgeSendToMessage(AcknowledgeMessage):

    def __init__(self, message, estampille, dest, id):
        super().__init__(message, estampille, dest, id)
    
    def __str__(self) -> str:
        return super().__str__()