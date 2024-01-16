

const { gamingOntology, games, texts } = require("./data/games.js")
const express = require("express")
const app = express()




app.use("/css", express.static(__dirname + "/css"))
app.use("/js", express.static(__dirname + "/js"))

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html")
})

app.listen(8080)
