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

Selon le fichier que vous lancez, vous obtiendrez un scraping plus ou moins complet. **Chaque fichier peut être joué individuellement des autres, excepté pour `phase5.py`qui nécessite d'avoir lancé `phase4.y`.**  Voici ce que font tous les fichiers :

### phase1.py

Ce script Python visite une page du site, celle du livre [A Light in the Attic](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html), et en extrait diverses informations.  
Il les note dans un dossier csv appelé `single_book.csv` situé à la racine du projet.

### phase2.py

Ce script Python récupère toutes les informations de tous les livres appartenant à la catégorie [Sequential Art](https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html). Il navigue entre les différentes pages pour récupérer l'entièreté des livres de la catégorie.   
Il les note dans un dossier appelé `category.csv` situé à la racine du projet.

### phase3.py

Ce script Python récupère également les informations de tous les livres appartenant à la catégorie [Sequential Art](https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html), mais enregistre en plus les images de tous les livres parcourus dans un dossier appelé `images` et situé à la racine du projet.   
Toutes les images ont le titre du livre associé.

### phase4.py 

Ce script Python consulte le site entier de [Books to Scrape](https://books.toscrape.com/index.html) afin de récupérer des informations sur tous les livres de toutes les catégories.   
Il note les informations des livres dans différents documents csv (ayant chacun d'une catégorie et comprenant tous les livres de la catégorie concernée) situés dans un dossier appelé `csv` et situé à la racine du projet.   
Il stock également toutes les couvertures des livres dans des dossiers ayant le nom de la catégorie dont fait partie chaque livre, ces dossiers étant eux-mêmes rangés dans le dossier `images`. Chaque image a le nom du livre auquel elle appartient.

### phase5.py

**Il est nécessaire d'avoir fait tourner phase4.py avant de lancer phase5.py !**     
Ce script Python permet de générer des graphiques à partir des fichers csv générés dans `phase4.py`.   
Dans l'état actuel, le graphique généré montre sous forme de graphique en barre le prix moyen des livres en fonction de la catégorie.     
Il est également possible d'afficher un diagramme circulaire montrant le pourcentage de livres par catégorie. Pour cela, il faut décommenter les lignes 19 à 20 de `phase5.py` :

```
plt.pie(y, labels = pie_labels, autopct='%1.1f%%')
plt.title('Pourcentage de livres en fonction de la catégorie')
plt.show() 
```

Puis commenter les lignes 38 à 42 de `phase5.py` :

```
# plt.barh(categories, mean_prices)
# plt.xlabel('Prix moyen (en £)')
# plt.ylabel('Catégories')
# plt.title('Prix moyen des livres en fonction de la catégorie')
# plt.show()
```