const fs = require('fs')
const rdf = require("rdflib")


const RDF = rdf.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
const RDFS = rdf.Namespace("http://www.w3.org/2000/01/rdf-schema#")
const XSD = rdf.Namespace("http://www.w3.org/2001/XMLSchema#")
const FOAF = rdf.Namespace("http://xmlns.com/foaf/0.1/")
const DC = rdf.Namespace("http://purl.org/dc/elements/1.1/")
const SKOS = rdf.Namespace("http://www.w3.org/2004/02/skos/core#")

const APP = rdf.Namespace("http://luc-damas.fr/rdf#")


// RDF : http://www.w3.org/1999/02/22-rdf-syntax-ns#
// RDFS : http://www.w3.org/2000/01/rdf-schema#
// FOAF : http://xmlns.com/foaf/0.1/
// XSD : http://www.w3.org/2001/XMLSchema#
// DC : http://purl.org/dc/elements/1.1/

const me = APP("Luc") //  Subject : http://luc-damas.fr/rdf#Luc
const robin = APP("Robin")
const geek = APP("Geek")


function getId(name) {
    return name.replace(/\s/g, "_")
}

let data = fs.readFileSync(__dirname + '/example.json').toString();
data = JSON.parse(data);

const store = rdf.graph();

const baseUrl = APP().value

for(let element in data) {
    store.add(APP(getId(element)), RDFS("label"), element)
    for(let aliases in data[element].aliases) {
        store.add(APP(getId(element)), SKOS("altLabel"), data[element].aliases[aliases])
    }
    store.add(APP(getId(element)), RDF("type"), data[element].type)
    store.add(APP(getId(element)), SKOS("definition"), data[element].definition)
    for(let linkedSubject in data[element].linkedSubjects) {
        store.add(APP(getId(element)), SKOS("related"), data[element].linkedSubjects[linkedSubject])
    }
    store.add(APP(getId(element)), APP("pronounce"), data[element].pronounce)
}

console.log(store.toString())