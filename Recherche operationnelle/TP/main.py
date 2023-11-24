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

graphOriente = graph_oriente()
print(graphOriente)

graphNonOriente = graph_non_oriente()
print(graphNonOriente)

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

graphOriente.calcMatriceAdjacence()
matrice = graphOriente.getMatriceAdjacence()
# print(matriceeTestOriente == matrice)
print(matrice)
degreEntrant = graphOriente.getDegreEntrant(graphOriente.getSommet(7))
degreSortant = graphOriente.getDegreSortant(graphOriente.getSommet(7))
distance2 = graphOriente.getSommetDistanceN(2)
print(distance2)
distanceMin = graphOriente.getDistanceMin(graphOriente.getSommet(2), graphOriente.getSommet(6))
print(f"distance min entre 2 et 6 : {distanceMin}")

graphNonOriente.calcMatriceAdjacence()
matrice = graphNonOriente.getMatriceAdjacence()
# print(matriceTestNonOriente == matrice)
print(matrice)
degreEntrant = graphNonOriente.getDegreEntrant(graphNonOriente.getSommet(5))
degreSortant = graphNonOriente.getDegreSortant(graphNonOriente.getSommet(5))
distance2 = graphNonOriente.getSommetDistanceN(2)
print(distance2)
distanceMin = graphNonOriente.getDistanceMin(graphNonOriente.getSommet(2), graphNonOriente.getSommet(6))
print(f"distance min entre 2 et 6 : {distanceMin}")
