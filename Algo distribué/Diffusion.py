from mpi4py import MPI

def diffusionCentralisee(id):
    comm = MPI.COMM_WORLD
    me = comm.Get_rank()
    size = comm.Get_size()
    # clock = 0
    print("Hi from <"+str(me)+">")
    buf = ["coucou",0]

    if me == id:
        print("I'm <"+str(me)+">: send " + buf[0])
        for i in range(1, size):
            buf[1]+=1
            comm.send(buf, dest=i, tag=99)
    else:
        buf = comm.recv(source=id, tag=99)
        buf[1]+=1
        print("I'm <"+str(me)+">: receive " + buf[0] + " clock : " + str(buf[1]))

# def __main__():
#     DiffusionCentralisee(0)

def diffusionAnneau(id):
    comm = MPI.COMM_WORLD
    me = comm.Get_rank()
    size = comm.Get_size()
    print("Hi from <"+str(me)+">")
    prev = (me - 1 + size) % size
    next = (me + 1) % size

    buf = ["coucou"]
    if me == id:
        print("I'm <"+str(me)+">: send " + buf[0])
        comm.send(buf, dest=(next), tag=99)
    elif me == (id - 1 + size) % size:
        buf = comm.recv(source=(prev), tag=99)
        print("I'm <"+str(me)+">: receive " + buf[0])
    else:
        buf = comm.recv(source=(prev), tag=99)
        print("I'm <"+str(me)+">: receive and send " + buf[0])
        comm.send(buf, dest=(next), tag=99)
        
def diffusionAnneauDouble(id):
    comm = MPI.COMM_WORLD
    me = comm.Get_rank()
    size = comm.Get_size()
    print("Hi from <"+str(me)+">")
    prev = (me - 1 + size) % size
    next = (me + 1) % size
    buf = ["coucou", 0]

    # print("node : " + str(me) + " elif pour 0 : " + str(round((size//2)+1+id)%size))
    # print("l'autre elif : "+ str((size//2)+1+id))

    if me == id:
        print("I'm <"+str(me)+">: send " + buf[0] + " clock : " + str(buf[1]), flush=True)
        buf[1]+=1
        comm.send(buf, dest=(next), tag=99)
        # print(str(me) + " : prev : " + str(prev) )
        print("I'm <"+str(me)+">: send " + buf[0] + " clock : " + str(buf[1]), flush=True)
        buf[1]+=1
        comm.send(buf, dest=(prev), tag=99)
    elif me == round((size//2)+1+id)%size:
        buf = comm.recv(source=(next), tag=99)
        buf[1]+=1
        print("I'm <"+str(me)+">: receive from next " + buf[0] + " clock : " + str(buf[1]), flush=True)
    elif me == round((size//2)+id)%size:
        buf = comm.recv(source=(prev), tag=99)
        buf[1]+=1
        print("I'm <"+str(me)+">: receive from prev " + buf[0] + " clock : " + str(buf[1]), flush=True)
    elif me < ((size//2)+id):
        buf = comm.recv(source=(prev), tag=99)
        buf[1]+=1
        print("I'm <"+str(me)+">: receive " + buf[0] + " clock : " + str(buf[1]), flush=True)
        buf[1]+=1
        comm.send(buf, dest=(next), tag=99)
        print("I'm <"+str(me)+">: send " + buf[0] + " clock : " + str(buf[1]), flush=True)
    elif me > ((size//2)+1+id):
        buf = comm.recv(source=(next), tag=99)
        buf[1]+=1
        print("I'm <"+str(me)+">: receive " + buf[0] + " clock : " + str(buf[1]), flush=True)
        buf[1]+=1
        comm.send(buf, dest=(prev), tag=99)
        print("I'm <"+str(me)+">: send " + buf[0] + " clock : " + str(buf[1]), flush=True)

        

def multicastCentralisee(source, destinataires, message):
    comm = MPI.COMM_WORLD
    me = comm.Get_rank()

    if me == source:
        for dest in destinataires:
            comm.send(message, dest=(dest), tag=99)
    if me in destinataires:
        buf = comm.recv(source=source, tag=99)
        print("I'm <"+str(me)+">: receive : " + buf + " from " + str(source))



# ======================================Test====================
# diffusionCentralisee(0)
# diffusionAnneau(0)
diffusionAnneauDouble(0)