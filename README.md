# Python scraping training

Ce projet contient plusieurs fichiers permettant de scaper différentes informations du site [Books to Scrape](https://books.toscrape.com/index.html).

## Initier le projet

1. La première étape est de cloner ce repository.
2. Il est ensuite nécessaire de créer un environnement virtuel. Il suffit pour cela de faire les lignes de commande ci-dessous dans le dossier où vous avez téléchargé le projet.

Lignes de commande pour Windows :

```
python3 -m venv env

source env/bin/activate
```

Lignes de commande pour Mac/ Linux :

```
python -m venv env

env\Scripts\activate
```

3. Il faut par la suite installer les dépendances dans l'environnement virtuel. Afin de réaliser cela, veuillez taper la ligne de commande ci-dessous.

```
pip install -r requirements.txt
```

## Commencez à scraper

Il est maintenant possible de scraper le site. Cela est faisable en jouant un fichier directement dans votre éditeur de code, ou alors avec les commandes :

```
Python [nom du fichier à jouer]
```

ou :

```
python3 [nom du fichier à jouer]
```

**Pensez à bien remplacer `[nom du fichier à jouer]` par le nom effectif du fichier que vous souhaitez lancer (phase1.py, phase2.py, phase3.py, phase4.py, ou encore phase5.py) !**

Selon le fichier que vous lancez, vous obtiendrez un scraping plus ou moins complet. **Chaque fichier peut être joué individuellement des autres, excepté pour `phase5_piegraph.py`, `phase5_bargraph.py` et `phase6.py` qui nécessitent d'avoir lancé `phase4.py`.**    
Voici ce que font tous les fichiers :

### 1. phase1.py

Ce script Python visite une page du site, celle du livre [A Light in the Attic](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html), et en extrait diverses informations.  
Il les note dans un dossier csv appelé `single_book.csv` situé à la racine du projet.

### 2. phase2.py

Ce script Python récupère toutes les informations de tous les livres appartenant à la catégorie [Sequential Art](https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html). Il navigue entre les différentes pages pour récupérer l'entièreté des livres de la catégorie.   
Il les note dans un dossier appelé `category.csv` situé à la racine du projet.

### 3. phase3.py

Ce script Python récupère également les informations de tous les livres appartenant à la catégorie [Sequential Art](https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html), mais enregistre en plus les images de tous les livres parcourus dans un dossier appelé `images` et situé à la racine du projet.   
Toutes les images ont le titre du livre associé.

### 4. phase4.py 

Ce script Python consulte le site entier de [Books to Scrape](https://books.toscrape.com/index.html) afin de récupérer des informations sur tous les livres de toutes les catégories.   
Il note les informations des livres dans différents documents csv (ayant chacun le nom d'une catégorie et comprenant tous les livres de la catégorie concernée) situés dans un dossier appelé `csv` et situé à la racine du projet.   
Il stock également toutes les couvertures des livres dans des dossiers ayant le nom de la catégorie dont fait partie chaque livre, ces dossiers étant eux-mêmes rangés dans le dossier `images`. Chaque image a le nom du livre auquel elle appartient.

### 5. phase5_piegraph.py & phase5_bargraph

**Il est nécessaire d'avoir fait tourner phase4.py avant de lancer phase5_piegraph.py ou phase5_bargraph !**  

Ces scripts Python permettent de générer des graphiques à partir des fichers csv générés dans `phase4.py`.  

1. phase5_piegraph.py   

Ce script Python permet d'obtenir un diagramme circulaire montrant le pourcentage de livres par catégorie.   

2. phase5_bargraph.py   

Le graphique généré montre sous forme de graphique en barre le prix moyen des livres en fonction de la catégorie.   

### 6. phase6.py

**Il est nécessaire d'avoir fait tourner phase4.py avant de lancer phase6.py !**  

Ce script permet d'obtenir un pdf présentant diverses informations relatives aux données récupérées en scrapant [Books to Scrape](https://books.toscrape.com/index.html).   
Le PDF est appelé `rapport_prix_livres.pdf` et est placé à la racine du projet.