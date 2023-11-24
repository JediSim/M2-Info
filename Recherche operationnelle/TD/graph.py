class Graph:
    def __init__(self):
        self.sommets = []

    def addSommet(self, sommet):
        self.sommets.append(sommet)

    def addArc(self, sommet1, sommet2):
        sommet1.addVoisin(sommet2)

    def getSommet(self, nom):
        for sommet in self.sommets:
            if sommet.nom == nom:
                return sommet
        return None
    
    def getVoisins(self, sommet):
        return sommet.voisin


    def __str__(self):
        res = "Graph:\n"
        for i in range(0, len(self.sommets)):
            res += str(self.sommets[i]) + "\n"
        return res
    
class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.voisin = []

    def addVoisin(self, voisin):
        self.voisin.append(voisin)

    def __str__(self):
        return "Sommet: " + str(self.nom) + " Voisins: " + str(self.voisin)

    def __repr__(self):
        return str(self.nom)

    def __eq__(self, other):
        return self.nom == other.nom

    def __hash__(self):
        return hash(self.nom)


