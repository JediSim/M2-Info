const fs = require('node:fs');

let ontoJSONStr = ""
let prevLevel = 0
let level = 0

const data = fs.readFileSync(__dirname+'/ontology.txt', "utf8")
const gamesDict = { }

data.split("\n").forEach(line => {

  if (line.trim() != "") {
    let [indentName,games] = line.split("|")
    let name = indentName.trim()
    level = indentName.split("\t").length-1
    games = games.split(",")

    games.forEach(game => {
      if (game != "") {
        if (!gamesDict[game])
          gamesDict[game] = []
        gamesDict[game].push(name)
      }
    })


    if (level != 0) {
      for(let i=level; i<prevLevel+1; i++) {
        ontoJSONStr += "\t".repeat(level)
        ontoJSONStr += "] }"
      }
    }

    if (name.length > 0) {
      if (prevLevel >= level && prevLevel != 0)
          ontoJSONStr += ","
      ontoJSONStr += "\n" + "\t".repeat(level) + '{ "name": "' + name + '", "level": '+level+', '
      ontoJSONStr += '"games": [ '
      games.forEach((game,i) => {
        ontoJSONStr += '"' + game + '"'
        if (i<games.length-1)
          ontoJSONStr += ", "
      })
      ontoJSONStr += ' ], '
      ontoJSONStr += '"subs": ['  
    }

    prevLevel = level
  }

})

for(let i=0; i<prevLevel+1; i++) {
  ontoJSONStr += "\t".repeat(prevLevel)
  ontoJSONStr += "] }"
}

ontology = JSON.parse(ontoJSONStr)



const allTexts = fs.readFileSync(__dirname+'/allTexts.txt', "utf8")
const texts = allTexts.split("-------------------------------------------------------------------------------------------------------------------------")





exports.gamingOntology = ontology
exports.games = gamesDict
exports.texts = texts



