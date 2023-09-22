from threading import Lock, Thread
from time import sleep
from Com import Com

class Process(Thread):
    
    def __init__(self,name):
        Thread.__init__(self)

        self.com = Com()
        
        self.nbProcess = self.com.getNbProcess()

        self.myId = self.com.getMyId()
        self.setName(name)

        self.alive = True
        self.start()
    

    def run(self):
        loop = 0
        while self.alive:
            print(self.getName() + " Loop: " + str(loop))
            sleep(1)

            if loop == 0:
                self.com.connect(self.getName())

            if self.getName() == "P0":
                self.com.sendTo("wesh le sang", "P1")
                self.com.broadcast("coucou tout le monde", self.getName())
                
                self.com.synchronize()
                print("P0 est synchro", flush=True)
                self.com.broadcastSync(self.getName(), "P0 est synchro")
                msg = self.com.recevFromSync("P2")
                print(str(self.getName()) + " " + str(msg), flush=True)

            if self.getName() == "P1":
                if not (self.com.mailbox.isEmpty()):
                    
                    self.com.requestSC()
                    print("P1 a le jeton")
                    while not self.com.mailbox.isEmpty():
                        msg = self.com.mailbox.getMsg()
                        print(str(self.getName()) + " " + str(msg), flush=True)
                    self.com.releaseSC()
                print("P1 : " + str(self.alive) + " - deathNode : " + str(self.com.deathNode) + " - nodesId : " + str(self.com.nodesId), flush=True)
                self.com.synchronize()
                print("P1 est synchro", flush=True)
                self.com.broadcastSync("P0")
                    
            if self.getName() == "P2":
                # TODO: C'est peut être pas la bonne méthode pour lancer le token sur le ring
                if loop == 0:
                    self.com.releaseSC()
                # while not self.com.mailbox.isEmpty():
                #     msg = self.com.mailbox.getMsg()
                #     print(str(self.getName()) + " " + str(msg))
                self.com.synchronize()
                print("P2 est synchro", flush=True)
                self.com.broadcastSync("P0")
                self.com.sendToSync("OK", "P0")
                print("P2 : " + str(self.alive) + " - deathNode : " + str(self.com.deathNode) + " - nodesId : " + str(self.com.nodesId), flush=True)

                

            loop+=1
        print(self.getName() + " stopped")

    def stop(self):
        self.alive = False
        # self.com.sendDeathMessage()
        self.com.stop()
        self.join()
