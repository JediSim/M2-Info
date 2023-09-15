from threading import Lock, Thread

from time import sleep

from MessageDedie import MessageDedie

#from geeteventbus.subscriber import subscriber
#from geeteventbus.eventbus import eventbus
#from geeteventbus.event import event

#from EventBus import EventBus
from Bidule import Bidule
from BroadcastMessage import BroadcastMessage
from Token import Token

from pyeventbus3.pyeventbus3 import *

class Process(Thread):
    nbProcess = 0
    def __init__(self,name):
        Thread.__init__(self)


        self.myId = Process.nbProcess
        Process.nbProcess +=1
        self.setName(name)

        PyBus.Instance().register(self, self)

        self.clock = 0
        self.alive = True
        self.req = False
        self.notToken = True
        self.start()
        
    @subscribe(threadMode = Mode.PARALLEL, onEvent=Bidule)
    def process(self, event):

        self.incrClock(event.getEstampille())
        print(self.getName() + ' Processes event: ' + event.getMachin() + " clock : " + str(self.clock))



    def run(self):
        loop = 0

        if self.getName() == "P3":
            # token = Token(self.clock, self.getName())
            self.release()

        while self.alive:
            print(self.getName() + " Loop: " + str(loop) + " clock : " + str(self.clock),flush=True)
            sleep(1)

            if self.getName() == "P1":
                self.incrClock()
                # b1 = Bidule("ga", self.clock)
                # b2 = Bidule("bu")
                # print(self.getName() + " send: " + b1.getMachin() + " clock : " + str(self.clock))
                # =========================================== BM
                # b1 = BroadcastMessage("ga", self.clock, self.getName())
                # print(self.getName() + " " + str(b1))
                # PyBus.Instance().post(b1)
                # =========================================== MP
                # b1 = MessageDedie("ga", self.clock, "P2")
                # print(self.getName() + " " + str(b1))
                # PyBus.Instance().post(b1)
                # =========================================== Token
                self.request()
                print("ATTANTION !!!! c'est critique clock : " + str(self.clock))
                self.release()
            

            loop+=1
        print(self.getName() + " stopped")

    def incrClock(self, concuClock=None):
        if concuClock == None:
            self.clock+=1
        elif concuClock > self.clock:
            self.clock = concuClock
            self.clock+=1
        else:
            self.clock+=1

    @subscribe(threadMode = Mode.PARALLEL, onEvent=BroadcastMessage)
    def onBroadcast(self, event):
        if self.getName() != event.getSender():
            self.incrClock(event.getEstampille())
            print(self.getName() + ' Processes event: ' + event.getMessage() + " clock : " + str(self.clock))

    def broadcast(self, message):
        self.incrClock()
        b1 = BroadcastMessage(message, self.clock)
        print(self.getName() + " send: " + b1.getMessage() + " clock : " + str(self.clock))
        PyBus.Instance().post(b1)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=MessageDedie)
    def onReceive(self, message):
        if self.getName() == message.getDest():
            self.incrClock(message.getEstampille())
            print(str(message) + " clock : " + str(self.clock))

    def sendTo(self, message, dest):
        self.incrClock()
        b1 = MessageDedie(message, self.clock, dest)
        print(str(b1) + " clock : " + str(self.clock))
        PyBus.Instance().post(b1)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Token)
    def onToken(self, token):
        if self.getName() == token.getDest():
            # print("receive token : " + str(token), flush=True)
            self.incrClock(token.getEstampille())
            self.notToken = False
            if self.req:
                # On est dans la section critique
                print("section critique : " + str(token), flush=True)
                # print(token)
            else:
                self.release()
        
    def request(self):    
        self.req = True
        while self.notToken == True:
            sleep(2)

    def release(self):
        # Ajoutté pour pouvoir arréter le processus a la fin
        if self.alive:
            self.req = False
            self.notToken = True
            self.incrClock()
            # print("release : " + str(token))
            token = Token(self.clock, self.getNext())
            PyBus.Instance().post(token)

    def getNext(self):
        return "P" + str((self.myId + 1)%Process.nbProcess + 1)

    def stop(self):
        self.alive = False
        self.join()
