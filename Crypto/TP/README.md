
## Usage

aller dans le bon répertoire puis compiler avec la commande suivante

```bash
make
```

nom de l'executable ./rbt

## Questions

### Q1
```bash
./rbt --hash Salut
```

### Q2
```bash
./rbt --calculN --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --taille 4
```

### Q3
```bash
./rbt --help
```

### Q4

```bash
./rbt --i2c 2 --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --taille 4
```

### Q6

```bash
./rbt --h2i oups 1 --taille 5 --alphabet abcdefghijklmnopqrstuvwxyz
```

### Q7

```bash
./rbt --i2i 100 --taille 5 --alphabet abcdefghijklmnopqrstuvwxyz
```

### Q8

En quoi est-ce que l'ajout du paramètre t dans la fonction h2i permet d'augmenter la couverture de la table ?

Cela permet de réduire le nombre de collisions, et donc d'augmenter la couverture de la table.

### Q9

```bash
./rbt --creer_table 200 100 --taille 5 --alphabet abcdefghijklmnopqrstuvwxyz
```

### Q10

créer et sauvegarder une table --create largeur hauteur
```bash
./rbt --create 200 100 test --taille 5 --alphabet abcdefghijklmnopqrstuvwxyz
```

charge la table test et l'affiche
```bash
./rbt --info test --taille 5 --alphabet abcdefghijklmnopqrstuvwxyz
```

### Q11

on génère une table adaptée.

```bash	
./rbt --create 1000 1000 test --taille 4 --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
puis on crack le hash

```bash
./rbt --crack 16de25af888480da1af57a71855f3e8c515dcb61 test
```

### Q13

```bash
./rbt --couverture largeur hauteur --taille 4 --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### Q14

#### Premier hash

Pour `16de25af888480da1af57a71855f3e8c515dcb61` avec une taille de `4` et l'alphabet suivant : `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

on génère une table adaptée.

```bash	
./rbt --create 1000 1000 test --taille 4 --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

```bash
./rbt --crack 16de25af888480da1af57a71855f3e8c515dcb61 test
```

le resultat est **CODE** 

>temps de calcul de la table : 0.65s
>
>taille de la table : 13.6Ko
>
>temps de calcul de l'inverse (crackage) : 0.127s  

#### Deuxième hash

Pour `dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2` de taille `5` et l'alphabet suivant : `abcdefghijklmnopqrstuvwxyz0123456789,;:$.` 

on cherche une couverture acceptable

```bash
./rbt --couverture 1000 1000000 --taille 5 --alphabet "abcdefghijklmnopqrstuvwxyz0123456789,;:$."
```
ce qui donne une couverture de 96.493134

on génère une table adaptée.

```bash
./rbt --create 1000 1000000 test --taille 5 --alphabet "abcdefghijklmnopqrstuvwxyz0123456789,;:$."
```
1000000 100000000
```bash
./rbt --crack dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2 test
```

le resultat est **n00b.**

>temps de calcul de la table : 9min 57s
>
>taille de la table : 18Mo
>
>temps de calcul de l'inverse (crackage) : 0.3s


### Q15

Pour couvrir tout les mots de passe la taille est $len(alphabet)^{taille password}$ soit 36^8
Le temps nécessaire pour générer la table est de (36^8)*t ou t est le temps de calcul d'un hash et de l'écriture dans un fichier des deux colonnes (password et H8)

### Q16

```bash
./rbt --crack_exaustif 16de25af888480da1af57a71855f3e8c515dcb61 --taille 4 --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
Temps pour trouver : 0.3s 

```bash
./rbt --crack_exaustif dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2 --taille 5 --alphabet "abcdefghijklmnopqrstuvwxyz0123456789,;:$."
```
Temps pour trouver : 20s


Avec une recherche exaustive, en moyenne, le temps pour trouver le mot de passe est de

$len(alphabet)^{taille password}/2 = (36^8)/2$ 


### Q17
 
L'intérêt du sel est de rendre le hash plus complexe à cracker. En effet, le sel est un ajout de caractères aléatoires au mot de passe. Ainsi, le hash est différent pour chaque mot de passe, même si le mot de passe est le même. Cela rend donc la rainbow table inutile, car le hash n'est pas le même pour un même mot de passe.
