class Message():
    def __init__(self, message, estampille):
        self.message=message
        self.estampille=estampille

    def getMessage(self):
        return self.message
    
    def getEstampille(self):
        return self.estampille
    
    def __str__(self) -> str:
        return "message : " + self.message + " estampille : " + str(self.estampille)
    