---
title: You only look once Unified, real-time object detection
---
You only look once: Unified, real-time object detection
===

[TOC]

## Introduction

### Anciennes methodes

#### DPM (deformable parts models)

DPM est un classifier que l'on passe sur l'image comme un fenetre coulissante de manière à passer sur l'intégralité de l'image. Il utilise differents pipelines de manière concurente pour extraire les features, prédires les boxes, classifier.

#### R-CNN

R-CNN est un réseau par convolution. Le principe est de reperer des zones ou il y a potentiellement des objets. Ensuite on passe un classifier pour détecter le contenu de cette zone. Avec un traitement de pre-processing on défini les zones des objets dans l'image, on élimine les duplications de détection et on rescore les zones en fonction des autres objets dans l'image. Ce qui nous donne a la fin un réseau assez lent.

### Et maintenant ? YOLO

L'idée pour créer YOLO est de transformer la détection d'objet en un seul problème de regression, du pixel de l'image jusqu'à la détection des zones et la probabilité des class. Ce qui donne un réseau de convolution qui prédit les zones et les probabilitées des zones en même temps.

Yolo est donc particulièrement rapide puisqu'il n'y a que le réseau de convolution a traverser.

Contrairement aux deux autres techniques YOLO voit la totalité de l'image lors de son entrainement et de l'utilisation. Cela lui permet de prendre en compte le contexte de l'image pour faire ses prédictions.

## Comment ca marche ?

Le réseau commence par découper l'image en $S \times S$ blocs. Si le centre d'un objet tombe dans un bloc, ce bloc est responsable de sa détection.

Chaque blocs prédisent $B$ bordures d'objet et leur score de confiance. Ce score montre a quel point le model est confiant sur sa bordure, c'est a dire que la bordure est bien placée et il y a bien un objet dedans. On l'écrit comme suis, $Pr(Object) ∗ IOU^{truth}_{pred}$. Si il n'y a pas d'objet dans la boxe le score doit être de zero, sinon on veut qu'il soit égual à l'intersection over union entre la zone prédite et le ground truth (la véritée de terrain).

Chaque boxe contiennent 5 prédictions $x,y,w,h$ et la confiance. $(x,y)$ sont les coordonnées du centre de la boxe. $(w,h)$ sont la hauteur et la largeur de la boxe. La prediction de confiance represente l'$IOU$ entre la boxe et n'importe quelle boxe ground truth.

Chaques blocs prédisent aussi $C$ probabilité conditionnel de class $Pr(Class_i|Object)$. Ces probabilités sont condtionnées par le fait qu'une boxe contienne un objet.

Au moment de la phase test on multiplie les probabilités.
$$
Pr(Class_i|Object) ∗ Pr(Object) ∗ IOU^{truth}_{pred} = Pr(Class_i) ∗ IOU^{truth}_{pred}
$$

![](https://codimd.math.cnrs.fr/uploads/upload_9904a2052acb1c74479b2b1ca4543b70.png)

## Design du réseau

Ce model est implémenté comme un réseau de convolution. Les premiers layers de convolution permet d'extraire les features de l'image alors que les derniers, qui sont complètement connectés, prédises les probabilité et les coordonnées.
Cette architecture est inspirée par le GoogLeNet model pour la classification d'image. Il y a 24 layers de convolution suivit par 2 layers complètements connecté. A la place du module d'inception utilisé par le GoogLeNet, YOLO utilise un layer de reduction $1 \times 1$ suivit par un layer convolutionnel $3 \times 3$.
Une version rapide de YOLO à été entrainé pour repousser la limite de la détection rapide d'objet. Fast YOLO utilise le même type de réseau en reduisant le nombre de layer de convolution (9 à la place de 24).

![](https://codimd.math.cnrs.fr/uploads/upload_777a88c33a9055ee4440dd02a8271f1a.png)

## Entrainement

L'entrainement commence par la partie des 20 premiers layers de convolution sur le dataset ImageNet. Cette première partie d'eentrainement a été arrétée quand le réseau a atteind un resultat de 88 % de reussite sur le set de validation ImageNet-2012.
Le model est ensuite convertie pour faire de la détéction. Pour augmenter ls performances du réseau ils ajoutent 4 layers de convolution et 2 layers totalement connécté. Ils augmentent aussi la résolution de l'image d'entrée de $224 \times 224$ à $448 \times 448$ car détection demande une meilleur qualité.
Ils utilisent la Somme des carrés des résidus pour calculer l'erreur car elle permet d'être facilement optimisée. Elle permet aussi de déscendre facilement le score de confiance à zéro dans les boxes qui ne contienent pas d'objet.

## Comparaison et test

![](https://codimd.math.cnrs.fr/uploads/upload_8c25063deb35757e5cd1d2605aec177c.png)

Il a été comparé avec d'autres réseau de neurones spécialisé dans la détection d'objet. Comme le montre ce petit tableau comparatif YOLO a reussi à rendre réellement possible la détection d'objet en temps réel.

![](https://codimd.math.cnrs.fr/uploads/upload_4a1c47491e985c870111c29aa6b12fd6.png)

La plus grosse source d'erreur de YOLO est la position des objets dans l'image. On peut observer que, par rapport a R-CNN, YOLO à moins de chance de confondre un objet avec le fond.


## Résultats

![](https://codimd.math.cnrs.fr/uploads/upload_4d862bd9eb75533a86a59fc038a6d5b2.png)

YOLO a été testé sur des datasets d'oeuvre d'art, avec son annalise du contexte il est bien meilleur à détecter des objets dans des ouvres d'arts.

![](https://codimd.math.cnrs.fr/uploads/upload_d3b286f5366958500996e41f41a7585b.png)

Il a été testé aussi sur des images de film et il présente des bons résultats même si ici il confont un homme et un avion.

## Exemple de code