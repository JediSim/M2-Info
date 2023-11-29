from graph import *

def graph_oriente():
    graph = Graph()
    for i in range(1, 8):
        sommet = Sommet(i)
        graph.addSommet(sommet)

    graph.addArc(graph.getSommet(1), graph.getSommet(2))
    graph.addArc(graph.getSommet(1), graph.getSommet(3))
    graph.addArc(graph.getSommet(4),graph.getSommet(2))
    graph.addArc(graph.getSommet(4),graph.getSommet(3))
    graph.addArc(graph.getSommet(3),graph.getSommet(4))
    graph.addArc(graph.getSommet(2),graph.getSommet(5))
    graph.addArc(graph.getSommet(2),graph.getSommet(7))
    graph.addArc(graph.getSommet(5),graph.getSommet(3))
    graph.addArc(graph.getSommet(5),graph.getSommet(5))
    graph.addArc(graph.getSommet(5),graph.getSommet(6))
    graph.addArc(graph.getSommet(6),graph.getSommet(7))
    graph.addArc(graph.getSommet(6),graph.getSommet(5))
    graph.addArc(graph.getSommet(6),graph.getSommet(2))

    return graph

def graph_non_oriente():
    graph = Graph()
    for i in range(1, 8):
        sommet = Sommet(i)
        graph.addSommet(sommet)

    graph.addArcDoubleSense(graph.getSommet(1), graph.getSommet(2))
    graph.addArcDoubleSense(graph.getSommet(1), graph.getSommet(3))
    graph.addArcDoubleSense(graph.getSommet(4),graph.getSommet(2))
    graph.addArcDoubleSense(graph.getSommet(4),graph.getSommet(3))
    graph.addArcDoubleSense(graph.getSommet(3),graph.getSommet(5))
    graph.addArcDoubleSense(graph.getSommet(2),graph.getSommet(5))
    graph.addArcDoubleSense(graph.getSommet(2),graph.getSommet(7))
    graph.addArcDoubleSense(graph.getSommet(5),graph.getSommet(6))
    graph.addArcDoubleSense(graph.getSommet(6),graph.getSommet(7))
    graph.addArcDoubleSense(graph.getSommet(6),graph.getSommet(2))
    graph.addArcDoubleSense(graph.getSommet(5),graph.getSommet(5))

    return graph

def graph_oriente_for_rank():
    graph = Graph()
    for i in range(1, 8):
        sommet = Sommet(i)
        graph.addSommet(sommet)
    
    graph.addArc(graph.getSommet(1), graph.getSommet(2))
    graph.addArc(graph.getSommet(1), graph.getSommet(3))
    graph.addArc(graph.getSommet(2), graph.getSommet(4))
    graph.addArc(graph.getSommet(2), graph.getSommet(5))
    graph.addArc(graph.getSommet(2), graph.getSommet(6))
    graph.addArc(graph.getSommet(2), graph.getSommet(7))
    graph.addArc(graph.getSommet(3), graph.getSommet(4))
    graph.addArc(graph.getSommet(3), graph.getSommet(5))
    graph.addArc(graph.getSommet(5), graph.getSommet(7))
    graph.addArc(graph.getSommet(6), graph.getSommet(5))

    return graph

def graph_dijkstra():
    graph = Graph()
    for i in range(1, 8):
        sommet = Sommet(i)
        graph.addSommet(sommet)
    
    graph.addArc(graph.getSommet(1), graph.getSommet(2), 8)
    graph.addArc(graph.getSommet(1), graph.getSommet(3), 2)
    graph.addArc(graph.getSommet(2), graph.getSommet(7), 10)
    graph.addArc(graph.getSommet(2), graph.getSommet(5), 3)
    graph.addArc(graph.getSommet(3), graph.getSommet(4), 3)
    graph.addArc(graph.getSommet(4), graph.getSommet(3), 4)
    graph.addArc(graph.getSommet(4), graph.getSommet(2), 2)
    graph.addArc(graph.getSommet(5), graph.getSommet(3), 5)
    graph.addArc(graph.getSommet(5), graph.getSommet(6), 4)
    graph.addArc(graph.getSommet(6), graph.getSommet(7), 2)
    graph.addArc(graph.getSommet(6), graph.getSommet(5), 2)
    graph.addArc(graph.getSommet(6), graph.getSommet(2), 5)

    return graph

matriceTestNonOriente = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0]
    ]
matriceeTestOriente = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
    ]

print("===================graph oriente====================")

# Construction du graphe orienté
graphOriente = graph_oriente()
print(graphOriente)

# Calcul de la matrice d'adjacence
graphOriente.calcMatriceAdjacence()
matrice = graphOriente.getMatriceAdjacence()
# print(matriceeTestOriente == matrice)
print(matrice)

# List noeuds a distance 2
distance2 = graphOriente.getSommetDistanceN(2)
print(distance2)

# Distance min entre 2 noeuds
distanceMin = graphOriente.getDistanceMin(graphOriente.getSommet(2), graphOriente.getSommet(6))
print(f"distance min entre 2 et 6 : {distanceMin}")

# Nombre de composantes connexes
nbComposantesConnexes = graphOriente.getNbComposantesConnexes()
print(f"nombre de composantes connexes : {nbComposantesConnexes}")



print("===================graph non oriente====================")
# Construction du graphe non orienté
graphNonOriente = graph_non_oriente()
print(graphNonOriente)

# Calcul de la matrice d'adjacence
graphNonOriente.calcMatriceAdjacence()
matrice = graphNonOriente.getMatriceAdjacence()
# print(matriceTestNonOriente == matrice)
print(matrice)

# List noeuds a distance 2
distance2 = graphNonOriente.getSommetDistanceN(2)
print(distance2)

# Distance min entre 2 noeuds
distanceMin = graphNonOriente.getDistanceMin(graphNonOriente.getSommet(2), graphNonOriente.getSommet(6))
print(f"distance min entre 2 et 6 : {distanceMin}")

# Nombre de composantes connexes
nbComposantesConnexes = graphNonOriente.getNbComposantesConnexes()
print(f"nombre de composantes connexes : {nbComposantesConnexes}") 

print("===================graph oriente pour rank====================")

graphRank = graph_oriente_for_rank()
graphRank.calcMatriceAdjacence()

rank = graphRank.rang()
print(f"rank : {rank}")

print("===================graph oriente pour dijkstra====================")

graphDijkstra = graph_dijkstra()
graphDijkstra.calcMatriceAdjacence()
graphDijkstra.calcMatricePoids()

print(graphDijkstra.matricePoids)

dijkstra = graphDijkstra.dijkstra(graphDijkstra.getSommet(1))
path = graphDijkstra.dijkstra_path(graphDijkstra.getSommet(1), graphDijkstra.getSommet(7))
print(dijkstra)
print(path)
