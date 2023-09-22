from ConnectionMessage import ConnectionMessage

class ConnectionModificationId(ConnectionMessage):
    def __init__(self, message, estampille, id):
        super().__init__(message, estampille, id)

    def getId(self):
        return self.id

    def __str__(self):
        return "ConnectionModificationId: " + super().__str__() + " id : " + str(self.id)