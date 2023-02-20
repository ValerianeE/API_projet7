# API_projet7

**Contexte :**

Vous êtes Data Scientist au sein d'une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.

![image](https://user-images.githubusercontent.com/121805896/220085372-ceae2291-0c76-4bbc-9111-f34c776e6bd6.png)

L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).
De plus, les chargés de relation client ont fait remonter le fait que les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l’entreprise veut incarner.
Prêt à dépenser décide donc de développer un dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement. 

**Objectif :**

1. Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
2. Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.
3. Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le dashboard interactif qui appelle l’API pour les prédictions.

**Découpage des dossiers :**

Deux dépôts Github ont été créés pour ce projet. Ce dépôt, « API_projet7 », est celui qui correspond à la partie API du projet. Cette API a été créée avec le framework Flask. Voici le contenu des fichiers :
- Le code de l'API correspond au fichier main.py
- Un test unitaire d'un calcul du score effectué par l'API se fait automatiquement via le code contenu dans test_unitaire.py lors du déploiement de cette dernière
- model.pkl est un modèle importé lors du lancement de l'API
- sampled.csv est un fichier de données lui aussi importé lors du lancement
- Les autres fichiers présents dans ce dépôt servent au déploiement de l'API

Dans l'API, la fonction predict() permet de récupérer la probabilité de faillite d'un client pour rembourser son prêt à partie de son numéro identifiant, ainsi qu'une partie des SHAP Values nécessaires pour certains graphiques dans le dashboard.
