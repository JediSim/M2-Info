myId = 0
nbProc = 6
messages = []

def BrodcastCentral(myId):
    if myId == 0:
        for i in range(1, nbProc-1):
            send(i, "Hello")
    else:
        msg = receive(0)
        print(msg)

def BrodacastRingOneSide(myId):
    if myId == 0:       
        send(1, "Hello")
    elif myId == nbProc-1:
        msg = receive(myId-1)
    else:
        msg = receive(myId-1)
        send((myId+1), msg)

# def BrodacastRingBothSide(myId):
#     if myId == 0:       
#         send(1, "Hello")
#     else:
#         if myId > nbProc//2:
#             msg = receive(myId-1)
#             send((myId-1)%nbProc, msg)
#         elif myId == nbProc//2:
#             msg = receive(myId-1)
#         else:

def send(i, msg):
    ...

def receive(i):
    ...

def __main__():
    print("Hello World!")