from threading import Semaphore
from random import randint

from time import sleep

from MessageDedie import MessageDedie

#from geeteventbus.subscriber import subscriber
#from geeteventbus.eventbus import eventbus
#from geeteventbus.event import event

#from EventBus import EventBus
from BroadcastMessage import BroadcastMessage
from Token import Token
from SynchronizeMessage import SynchronizeMessage
from DeathMessage import DeathMessage
from MailBox import MailBox
from BroadcastSynchMessage import BroadcastSynchMessage
from AcknowledgeMessage import AcknowledgeMessage
from SendToSynchMessage import SendToSynchMessage
from AcknowledgeSendToMessage import AcknowledgeSendToMessage
from ConnectionMessage import ConnectionMessage

from pyeventbus3.pyeventbus3 import *

class Com():
    # nbProcess = 0
    def __init__(self):
        # Thread.__init__(self)

        self.myId = None
        # Com.nbProcess +=1
        # self.setName(name)

        PyBus.Instance().register(self, self)
        self.semaphoreClock = Semaphore()

        self.mailbox = MailBox()
        self.clock = 0
        self.alive = True
        self.req = False
        self.notToken = True
        self.synchronized = False
        self.nbSynchronized = 0
        self.nbBroadcastSync = 0
        self.notAcknowledge = True
        self.deathNode = []
        self.nodesId = []
        self.tmpId = None
        self.myIdConfirmed = False


    def incrClock(self, concuClock=None):
        """
            Incrémente l'horloge logique
        """
        self.semaphoreClock.acquire()
        if concuClock == None:
            self.clock+=1
        elif concuClock > self.clock:
            self.clock = concuClock
            self.clock+=1
        else:
            self.clock+=1
        self.semaphoreClock.release()

    @subscribe(threadMode = Mode.PARALLEL, onEvent=BroadcastMessage)
    def onBroadcast(self, message):
        if self.myId != message.getSender():
            self.incrClock(message.getEstampille())
            self.mailbox.addMessage(message)

    def broadcast(self, message, sender):
        """
            Envoie un message à tous les process
            @param message: message à envoyer
            @param sender: processus qui envoie le message
        """
        sender = self.getIdFromName(sender)
        self.incrClock()
        b1 = BroadcastMessage(message, self.clock, sender)
        print(str(self.myId) + " send: " + str(b1))
        PyBus.Instance().post(b1)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=MessageDedie)
    def onReceive(self, message):
        if self.myId == message.getDest():
            self.incrClock(message.getEstampille())
            self.mailbox.addMessage(message)

    def sendTo(self, message, dest):
        """
            Envoie un message à un processus
            @param message: message à envoyer
            @param dest: destinataire du message
        """
        dest = self.getIdFromName(dest)
        self.incrClock()
        b1 = MessageDedie(message, self.clock, dest)
        print(str(b1) + " clock : " + str(self.clock))
        PyBus.Instance().post(b1)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Token)
    def onToken(self, token):
        if self.myId == token.getDest() and self.alive:
            # print("receive token : " + str(token), flush=True)
            # self.incrClock(token.getEstampille())
            # On a le jeton
            self.notToken = False
            # On regarde si on a demandé l'acces a la section critique
            if self.req:
                # On est dans la section critique
                print(str(self.myId) + " section critique : " + str(token), flush=True)
                # print(token)
            else:
                # On passe le jeton au processus suivant
                # print("SC : " + str(self.myId) + " " + str(token), flush=True)
                self.releaseSC()
        
    def requestSC(self):
        """
            Demande l'acces a la section critique
        """
        # On demande l'acces a la section critique
        self.req = True
        # Tant qu'on a pas le jeton
        while self.notToken == True and self.alive:
            sleep(2)

    def releaseSC(self):
        """
            Libère la section critique
        """
        # Ajoutté pour pouvoir arréter le processus a la fin
        if self.alive:
            self.req = False
            self.notToken = True
            # self.incrClock()
            # print("release : " + str(token))
            token = Token(self.clock, self.getNext())
            PyBus.Instance().post(token)

    def getNext(self):
        """
            Calcul le nom du processus suivant pour le token
        """
        return (self.myId + 1) % len(self.nodesId) - len(self.deathNode)
    
    @subscribe(threadMode = Mode.PARALLEL, onEvent=SynchronizeMessage)
    def onSynchronize(self, message):
        if self.myId != message.getSender() and self.alive:
            self.incrClock(message.getEstampille())
            self.nbSynchronized += 1
            print(str(self.myId) + " " + str(message) + " nbSynchronized : " + str(self.nbSynchronized))

    def synchronize(self):
        """
            Synchronisation des processus
        """
        self.incrClock()
        msg = SynchronizeMessage(self.myId, self.clock)
        PyBus.Instance().post(msg)
        # On attend que tous les processus-1 (ne pas compter le processus courant) aient envoyé un message de synchronisation
        while self.nbSynchronized < len(self.nodesId) - len(self.deathNode) - 1 and self.alive:
            print(str(self.myId) + " wait nbSynchronized : " + str(self.nbSynchronized) +  " Com.nbProcess : " + str(len(self.nodesId) - len(self.deathNode) - 1))
            sleep(2)
        self.nbSynchronized = 0

    @subscribe(threadMode = Mode.PARALLEL, onEvent=DeathMessage)
    def onDeath(self, message):
        """
            Reception d'un message de mort d'un processus
            Utilisé pour eviter le cas ou un processus avant la fin d'une sychronisation
        """
        if self.myId != message.getSender():
            # self.incrClock(message.getEstampille())
            # print(str(self.myId) + " " + str(message))
            # Com.nbProcess -= 1
            self.deathNode.append(message.getSender())

    def sendDeathMessage(self):
        msg = DeathMessage(self.clock, self.myId)
        PyBus.Instance().post(msg)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=AcknowledgeMessage)
    def onAcknowledgement(self, message):
        """
            Accusé reception d'un message synch
        """
        if self.myId == message.getDest():
            self.incrClock(message.getEstampille())
            self.nbBroadcastSync += 1

    @subscribe(threadMode = Mode.PARALLEL, onEvent=BroadcastSynchMessage)
    def onBroadcastSynch(self, message):
        """
            Reception d'un message de broadcast synch
        """
        if self.myId != message.getSender():
            self.incrClock(message.getEstampille())
            self.mailbox.addMessageSynch(message)
            

    def receiveSynchMessage(self, sender):
        """
            Reception d'un message de broadcast synch
            @param sender: processus qui envoie le message
        """
        sender = self.getIdFromName(sender)
        lastSynch = self.mailbox.getMsgFromSender(sender)
        if lastSynch.getSender() == sender:
            return lastSynch
        return None

    def broadcastSync(self, sender, message=None):
        """
            Envoie un message à tous les processus de manière synchronisé
            @param message: message à envoyer
            @param sender: processus qui envoie le message
        """
        sender = self.getIdFromName(sender)
        if self.myId == sender:
            self.incrClock()
            msg = BroadcastSynchMessage(message, self.clock, self.myId)
            PyBus.Instance().post(msg)
            while self.nbBroadcastSync < len(self.nodesId) - len(self.deathNode) - 1 and self.alive:
                sleep(2)
                print(str(self.myId) + " wait nbBroadcastSync : " + str(self.nbBroadcastSync) +  " Com.nbProcess : " + str(len(self.nodesId) - len(self.deathNode)))
        else:
            lastSynch = self.mailbox.getMsgFromSender(sender)
            while lastSynch == None and self.deathNode.count(sender) == 0:
                sleep(2)
                lastSynch = self.mailbox.getMsgFromSender(sender)
            if lastSynch != None:
                msg = AcknowledgeMessage("",self.clock, sender, lastSynch.getId())
                PyBus.Instance().post(msg)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=SendToSynchMessage)
    def onSendToSynch(self, message):
        """
            Reception d'un message de manière synchronisé
        """
        if self.myId == message.getReceiver():
            self.incrClock(message.getEstampille())
            self.mailbox.addMessageSynch(message)

    @subscribe(threadMode = Mode.PARALLEL, onEvent=AcknowledgeSendToMessage)
    def onAcknowledgeSendTo(self, message):
        """
            Accusé reception d'un message synch
        """
        if self.myId == message.getDest():
            self.notAcknowledge = False

    def recevFromSync(self, sender):
        """
            Reception d'un message de manière synchronisé
            @param message: message à envoyer
            @param sender: processus qui envoie le message
        """
        sender = self.getIdFromName(sender)
        lastSynch = self.mailbox.getMsgFromSender(sender)
        while lastSynch == None and self.deathNode.count(sender) == 0:
            sleep(2)
            lastSynch = self.mailbox.getMsgFromSender(sender)
            print("wait message : " + str(lastSynch))
        print(str(self.myId) + " " + str(lastSynch))
        if lastSynch != None:
            msg = AcknowledgeSendToMessage("",self.clock, sender, lastSynch.getId())
            PyBus.Instance().post(msg)
        return lastSynch

    def sendToSync(self, message, dest):
        """
            Envoie un message à un processus de manière synchronisé
            @param message: message à envoyer
            @param dest: destinataire du message
        """
        dest = self.getIdFromName(dest)
        self.incrClock()
        msg = SendToSynchMessage(self.myId, dest, message, self.clock)
        PyBus.Instance().post(msg)
        while self.notAcknowledge and self.deathNode.count(dest) == 0:
            sleep(2)
            print(str(self.myId) + " wait ack : " + str(self.deathNode))
        self.notAcknowledge = True

    @subscribe(threadMode = Mode.PARALLEL, onEvent=ConnectionMessage)
    def onConnect(self, message):
        """
            Reception d'un message de connection
            @param message: message de connection
        """
        if not message.getId() in self.nodesId:
            self.nodesId.append((message.getId(), message.getName()))
        elif message.getId() == self.tmpId:
            self.tmpId = randint(1, 1000)
            conMsg = ConnectionMessage("connectionInit", self.clock, self.tmpId)
            PyBus.Instance().post(conMsg)


    def connect(self, name):
        """
            connect le com
        """
        self.tmpId = randint(1, 1000)
        conMsg = ConnectionMessage("connectionInit", self.clock, self.tmpId, name)
        PyBus.Instance().post(conMsg)
        sleep(0.1)
        self.nodesId.sort(key=lambda x: x[0])
        self.myId = self.nodesId.index((self.tmpId, name))
        for i in range(len(self.nodesId)):
            self.nodesId[i] = (i, self.nodesId[i][1])
        print("myId : " + str(self.myId) + " myName : " + str(name) + " nodesId : " + str(self.nodesId))

    def stop(self):
        """
            stop le com proprement
        """
        self.alive = False
        self.sendDeathMessage()
        # self.join()

    def getMyId(self):
        return self.myId
    
    def getNbProcess(self):
        return len(self.nodesId) - len(self.deathNode)
    
    def getIdFromName(self, name):
        for i in range(len(self.nodesId)):
            if self.nodesId[i][1] == name:
                return self.nodesId[i][0]
        return None
    