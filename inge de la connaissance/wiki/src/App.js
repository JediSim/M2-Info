import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useEffect, useState } from "react";

function App() {
  const [voiture, setVoiture] = useState([]);

  // https://dbpedia.org/page/Vocabulary

  // select distinct * where {     
  //             ?s rdfs:label 'Bière'@fr.  
  //             ?s dbo:abstract ?w.        
  //             ?s dbo:thumbnail ?t.      
  //             FILTER (lang(?w) = 'fr').  
  //         } limit 100

  const urlBase = "http://dbpedia.org/sparql?type=json&query="

  var req = "select distinct * where {?s rdfs:label ?label . \
            ?label bif:contains 'voiture' . \
            ?s dbo:abstract ?abs. \
            ?s dbo:thumbnail ?thumb. \
            FILTER (lang(?abs) = 'fr'). \
            } LIMIT 100"
              // $s dbo:wikiPageExternalLink ?links  \
              // ?s dbo:wikiPageWikiLink ?l \

  useEffect(() => {
    axios.get(urlBase+req)
        .then(res =>  {
            console.log(res.data.results.bindings)
            setVoiture(res.data.results.bindings)
        })
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
      {voiture.forEach(element => {
          console.log(element)
          return (
            <div key={element.s.value}>
              <p>{element.s.value}</p>
              <p>{element.abs.value}</p>
              <img src={element.thumb.value} alt="voiture"/>
            </div>
          )
        })}
    </div>
  );
}

export default App;
