# Traitement d'image notes

## The learning phase in machine learning

The learning phase typically involves the following steps:

1. Data Collection: The first step is to gather a dataset that contains examples of the problem you want the model to learn. This dataset should include input features (also known as independent variables) and corresponding target values (also known as dependent variables or labels).

2. Data Preprocessing: Before training the model, it's important to preprocess the data to ensure it is in a suitable format. This may involve tasks such as cleaning the data, handling missing values, scaling features, or encoding categorical variables.

3. Model Selection: Next, you need to choose an appropriate machine learning algorithm or model that is well-suited for your problem. There are various types of models, such as linear regression, decision trees, support vector machines, and neural networks, each with its own strengths and weaknesses.

4. Training the Model: Once the model is selected, the learning phase involves feeding the training data into the model and adjusting its internal parameters to minimize the difference between the predicted outputs and the actual target values. This process is known as optimization or parameter estimation. The specific algorithm used for training depends on the chosen model.

5. Evaluation: After training the model, it is important to evaluate its performance on a separate validation or test dataset. This helps assess how well the model generalizes to unseen data and provides insights into its accuracy and reliability. Evaluation metrics such as accuracy, precision, recall, and F1 score are commonly used to measure the model's performance.

6. Iteration and Improvement: Machine learning is an iterative process, and it often requires refining the model by adjusting hyperparameters, trying different algorithms, or collecting more data. This iterative process continues until the model achieves satisfactory performance on the validation or test dataset.

It's important to note that the learning phase in machine learning is computationally intensive and may require significant computational resources, especially for large datasets or complex models. Additionally, the quality and quantity of the training data play a crucial role in the model's ability to learn and generalize well.

Overall, the learning phase in machine learning involves training a model using a dataset, optimizing its parameters, evaluating its performance, and iteratively improving it to achieve better results.

## Data set for ML

Tous les liens ne sont plus bon
[Face and Object data set](https://datagen.tech/guides/image-datasets/image-datasets/#CAMO_Camouflaged_Object)

## Milestone for DL

1. Les débuts : Réseaux de neurones artificiels (ANN) et Perceptron (années 1950-1960)
    - Les débuts de l'apprentissage automatique avec les réseaux de neurones artificiels.
    - Le perceptron comme le premier modèle de réseau de neurones, mais limité aux problèmes linéaires.

2. Années 1980-1990 : Déclin et renaissance avec les réseaux de neurones profonds
    - Problèmes d'apprentissage profond (vanishing gradients) ont conduit à un déclin de l'intérêt.
    - Redécouverte des réseaux de neurones profonds avec l'introduction d'algorithmes comme la rétropropagation (backpropagation).

3. 2006-2012 : Révolution avec les réseaux de neurones profonds
    - Succès du modèle de Deep Belief Networks (DBN) et des architectures profondes.
    - Utilisation de l'apprentissage non supervisé pour l'initialisation des réseaux de neurones profonds.

4. 2012 : Émergence de la convolution avec AlexNet
    - AlexNet, gagnant du concours ImageNet, a popularisé l'utilisation des convolutions pour le traitement des images.
    - Utilisation intensive de GPU pour accélérer l'entraînement des modèles.

5. 2014-2015 : LSTMs et GRUs pour le traitement du langage naturel
    - Long Short-Term Memory (LSTM) et Gated Recurrent Unit (GRU) pour traiter les séquences, notamment dans le domaine du langage naturel.

6. 2018-2019 : Transformer et l'attention
    - Introduction de l'architecture Transformer, principalement utilisée pour les tâches de traitement du langage naturel.
    - Mécanisme d'attention pour capturer les relations à longue distance (c'est pas pour les couples c'est capter l'info du début du texte qui impacte la fin).

7. 2020 et au-delà : AutoML, apprentissage fédéré, et modèles plus grands
    - AutoML pour automatiser le processus de conception de modèles.
    - L'apprentissage fédéré pour l'entraînement distribué sans centralisation des données.
    - Modèles de plus en plus grands comme GPT-3 avec des centaines de milliards de paramètres.

8. Défis et considérations éthiques
    - Évolution de la recherche vers des modèles plus puissants soulève des questions éthiques concernant la confidentialité, la transparence, et la responsabilité.

## Milestones par categorie de problème

1. Classification :

    - **Débuts** : Utilisation de réseaux de neurones simples pour la classification binaire. Modèles comme le perceptron.

    - **Évolution** : Émergence des réseaux de neurones profonds. Modèles tels que LeNet, AlexNet, VGG, et enfin, l'utilisation généralisée de CNN (Convolutional Neural Networks) pour la classification d'images.

    - **Innovations récentes** : Architectures plus complexes comme ResNet, Inception, et EfficientNet. Utilisation de techniques d'augmentation de données, de normalisation de lot, et de techniques d'optimisation avancées.

2. Détection d’objets :

    - **Débuts** : Utilisation d'approches basées sur des fenêtres glissantes. Limitations en termes de précision et de vitesse de traitement.

    - **Évolution** : Apparition de Faster R-CNN, introduisant la région de proposition (Region Proposal Network). YOLO (You Only Look Once) qui effectue la détection d'objets en une seule passe. Evolution vers des versions plus rapides (YOLOv2, YOLOv3) et des modèles comme SSD (Single Shot Multibox Detector).

    - **Innovations récentes** : YOLOv4 et YOLOv5 avec des améliorations de performances et une meilleure gestion des petits objets. Intégration de modèles de détection d'objets dans des applications en temps réel.

3. Super-résolution :

    - **Débuts** : Méthodes traditionnelles basées sur la récupération d'informations à partir de plusieurs images plus petites.

    - **Évolution** : Introduction de CNN pour la super-résolution, notamment le modèle SRCNN (Super-Resolution Convolutional Neural Network).

    - **Innovations récentes** : Modèles GAN (Generative Adversarial Networks) comme SRGAN, qui génèrent des images plus réalistes et détaillées. Réseaux résiduels pour une meilleure convergence.

4. Colorisation :

    - **Débuts** : Méthodes manuelles ou basées sur des règles pour attribuer des couleurs à des images en niveaux de gris.

    - **Évolution** : Utilisation de CNN pour apprendre les correspondances de couleurs. Exemple : modèle de colorisation automatique de Zhang et al.

    - **Innovations récentes** : Intégration de modèles GAN pour produire des colorisations plus naturelles et réalistes. Améliorations dans la gestion des contours et des détails.

5. Transport de couleur :

    - **Débuts** : Méthodes basées sur la correction de couleur globale.

    - **Évolution** : Introduction de modèles d'apprentissage profond pour transférer des couleurs de manière plus fine et précise.

    - **Innovations récentes** : Modèles qui tiennent compte du contexte de la scène pour des résultats plus cohérents.

6. Flot optique :

    - **Débuts** : Méthodes classiques basées sur la corrélation entre les images.

    - **Évolution** : Introduction de modèles basés sur des réseaux de neurones, comme FlowNet, qui prédit directement le flot optique.

    - **Innovations récentes** : Optimisations pour la vitesse et la précision. Utilisation de réseaux plus profonds et de mécanismes d'attention.

7. Génération d’image à partir de texte :

    - **Débuts** : Approches basées sur la correspondance mot à mot.

    - **Évolution** : Utilisation de modèles GAN comme StackGAN et text-to-image synthesis basés sur des architectures Transformer.

    - **Innovations récentes** : Modèles comme DALL-E, capables de générer des images variées et détaillées à partir de descriptions textuelles.

8. Détection et suivi de visages / expressions :

    - **Débuts** : Méthodes basées sur des caractéristiques faciales spécifiques, suivi de visages avec des modèles géométriques simples.

    - **Évolution** : Introduction de modèles basés sur des caractéristiques apprises automatiquement, comme les CNN. Utilisation de réseaux pour la détection d'expressions faciales.

    - **Innovations récentes** : Modèles end-to-end pour la détection et le suivi, intégration de modèles de vision par ordinateur avec des modèles d'apprentissage profond pour une meilleure précision. Utilisation de modèles spécifiques pour la reconnaissance des émotions.
