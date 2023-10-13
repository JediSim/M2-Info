# TP1

## Problème 1

### Algo 1

```
Fonction fusionner(tableau gauche, tableau droit)
    tableau résultat
    Tant que gauche n'est pas vide et droit n'est pas vide
        Si gauche[0] < droit[0]
            Ajouter gauche[0] à résultat
            Retirer le premier élément de gauche
        Sinon
            Ajouter droit[0] à résultat
            Retirer le premier élément de droit
    Fin Tant Que

    Ajouter le reste de gauche à résultat
    Ajouter le reste de droit à résultat
    Retourner résultat

Fonction triFusion(tableau)
    Si la longueur du tableau est inférieure ou égale à 1
        Retourner tableau
    Sinon
        Trouver le point médian du tableau
        Diviser le tableau en deux moitiés, gauche et droit
        gaucheTrié = triFusion(gauche)
        droitTrié = triFusion(droit)
        Retourner fusionner(gaucheTrié, droitTrié)
    Fin Si
```
