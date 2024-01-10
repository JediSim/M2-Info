
class Relation {
    constructor(domain, id, nom) {
        this.domain = domain
        this.id = id
        this.nom = nom
    }
    toString() {
        return this.nom + " (" + this.id + ")" + " dans le domaine " + this.domain
    }
}

class Type {
    constructor(domain, id, nom) {
        this.domain = domain
        this.id = id
        this.nom = nom
    }
    toString() {
        return this.nom + " (" + this.id + ")" + " dans le domaine " + this.domain
    }
}

class Person {
    constructor(domain, id, nom) {
        this.domain = domain
        this.id = id
        this.nom = nom
    }
    toString() {
        return this.nom + " (" + this.id + ")" + " dans le domaine " + this.domain
    }
}

class Graph {
    constructor(){
        this.nodes = []
        this.relation = []
    }
    add(origin, relation, destination) {
        if (this.nodes.indexOf(origin) === -1)
            this.nodes.push(origin)
        if (this.nodes.indexOf(destination) === -1)
            this.nodes.push(destination)
        this.relation.push({
            origin: origin,
            relation: relation,
            destination: destination
        })
    }
    toString() {
        let str = ""
        for(let node in this.nodes) {
            str += this.nodes[node].toString() + "\n"
        }
        for(let relation in this.relation) {
            str += this.relation[relation].origin.toString() + " " + this.relation[relation].relation.toString() + " " + this.relation[relation].destination.toString() + "\n"
        }
        return str
    }
}

const graph = new Graph()

const isA = new Relation("USMB", "isA", "est un ")
const r = new Person("M2", "r", "Romain")   // domain, id, nom
const m2 = new Type("USMB","stu", "Etudiant")

graph.add(r, isA, m2)
console.log(graph.toString())