class Messager:
    def __init__(self,comm) -> None:
        self.clock = 0
        self.comm = comm
        
    def send(self, msg, to):
        self.clock+=1
        msg[1]=self.clock
        self.comm.send(msg, dest=to, tag=99)
        print("I'm <"+str(self.comm.Get_rank())+">: send : " + msg + " to " + str(to) + " clock : " + str(self.clock))

    def recv(self, source):
        msg = self.comm.recv(source=source, tag=99)
        if msg[1] < self.clock:
            self.clock+=1
        else:
            self.clock = msg[1]
            self.clock+=1
        print("I'm <"+str(self.comm.Get_rank())+">: receive : " + msg + " from " + str(source) + " clock : " + str(self.clock))

