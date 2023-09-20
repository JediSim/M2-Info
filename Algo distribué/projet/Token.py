from typing import Any
from MessageDedie import MessageDedie

class Token(MessageDedie):
    def __init__(self, estampille, dest):
        super().__init__("token", estampille, dest)

    def setDest(self, dest):
        self.dest = dest

    def __str__(self) -> str:
        return super().__str__()