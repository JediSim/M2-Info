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

def ScatterCentral(myId, data):
    sizePart = len(data)//nbProc

    if myId == 0:
        # On commence a sizePart car le noeud 0 garde la premiere partie
        for i in range(sizePart, len(data)-1, sizePart):
            # Si on est pas a la derniere partie
            if i+sizePart < len(data):
                send(i, data[i:i+sizePart])
            # Si on est a la derniere partie
            else:
                send(i, data[i:])
    else:
        msg = receive(0)
        print(msg)

def GatherCentral(myId,data):
    if myId == 0:
        for i in range(1, nbProc-1):
            msg = receive(i)
            messages.append(msg)
    else:
        send(0,data)

def ScatterRingOneSide(myId, data):
    chunk = len(data)//nbProc

    if myId == 0:
        send(1, data[chunk:])
    elif myId == nbProc-1:
        msg = receive(myId-1)
        print(msg)
    else:
        msg = receive(myId-1)
        send((myId+1)%nbProc, msg[chunk*myId:])

def GatherRingOneSide(myId, data):
    chunk = len(data)//nbProc

    if myId == 0:
        msg = receive(myId+1)
    elif myId == nbProc-1:
        msg = send(myId-1,data)
    else:
        msg = receive(myId+1)
        data.append(msg)
        send(myId-1, data)

def AllGather(myId, data):
    GatherCentral()
    BrodcastCentral()



def send(i, msg):
    ...

def receive(i):
    ...

def __main__():
    print("Hello World!")