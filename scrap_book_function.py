
from bs4 import BeautifulSoup
import requests
import re
from word2number import w2n
from PIL import Image
from urllib.request import urlopen
import os
import shutil
import statistics
import csv


url = "https://books.toscrape.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}


def get_informations(scrapped_url):
    
    """Cette fonction retourne les informations d'un livre.
    
    Arguments :
    scrapped_url -- url du livre dont on veut récupérer les informations
    """
    
    response_single_book = requests.get(scrapped_url, headers=headers)
    soup_single_book = BeautifulSoup(response_single_book.content, 'html.parser')
    
    data = {}
    data['product_page_url'] = scrapped_url
        
    if response_single_book.status_code == 200:  
        data['universal_product_code (upc)'] = soup_single_book.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type').text
        data['title'] = soup_single_book.select_one('h1').text
        data['price_including_tax'] = soup_single_book.select_one('table > tr:nth-child(4) td:first-of-type').text
        data['price_excluding_tax'] = soup_single_book.select_one('table > tr:nth-child(3) td:first-of-type').text
        
        availability = soup_single_book.select_one('table > tr:nth-child(6) td:first-of-type').text
        data['number_available'] = re.search(r"\d+", availability).group()
        
        try:
            data['product_description'] = soup_single_book.select_one('div#product_description ~ p').text
        except:
            data['product_description'] = ''
        
        data['category'] = soup_single_book.select_one('ul.breadcrumb > li:nth-child(3) > a').text
        
        data['review_rating'] = w2n.word_to_num(soup_single_book.find('p', class_='star-rating')['class'][1])
        
        data['image_url'] = str(url + soup_single_book.find('img')['src'].replace('../',''))
        
        return data
        
    else:
        print(f"Erreur : {response_single_book.status_code}")
            


def save_image(image_url, image_name):
    
    """Cette fonction permet de sauvegarder une image à la racine du projet.
    
    Arguments :
    image_url -- url de l'image à enregistrer
    image_name -- nom que l'on veut donner à l'image
    """
    
    with Image.open(urlopen(image_url)) as image:
        name = re.sub(r'[<>:"/\|?*]', '', image_name)
        path = str('./images/' + name + '.jpg')
        image.save(path)

def save_image_in_directory(image_url, image_category, image_name):
    
    """Cette fonction permet de sauvegarder une image dans un dossier donné.
    
    Arguments :
    image_url -- url de l'image à enregistrer
    image_category -- nom du dossier dans lequel on souhaite enregistrer l'image
    image_name -- nom que l'on veut donner à l'image
    """
    
    with Image.open(urlopen(image_url)) as image:
        name = re.sub(r'[<>:"/\|?*]', '', image_name)
        path = str('./images/' + image_category + '/' + name + '.jpg')
        image.save(path)


def create_directory(directory_name):
    
    """Cette fonction permet de créer un dossier à la racine du projet.
    Si un dossier existe déjà avec le nom qu'on souhaite donner au nouveau dossier, alors elle supprime l'ancien dossier ainsi que les documents dedans, et récrée un dossier avec le nom souhaité.
    
    Arguments :
    directory_name -- nom que l'on souhaite donner au projet à créer
    """
    
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        shutil.rmtree(directory_name)
        os.mkdir(directory_name)


def get_global_mean():
    
    """Cette fonction permet de retourner la moyenne totale de tous les livres.
    
    Arguments :
    None
    """
    
    csv_list = (os.listdir('./csv'))
    
    price = 'price_including_tax'
    mean_prices = []
    
    for single_csv in csv_list:
        with open('./csv/' + single_csv, 'r') as file:
            reader = csv.DictReader(file)
            category_prices = [float(row[price].replace('£', '')) for row in reader]

            if category_prices:
                mean_price = statistics.mean(category_prices)
                mean_prices.append(mean_price)
    
    global_mean_price = str(float("{:.2f}".format(statistics.mean(mean_prices))))
    
    return global_mean_price
    
def get_most_filled_category():
    
    """Cette fonction permet de retourner le nom de la catégorie avec le plus de livres.
    
    Arguments :
    None
    """
 
    csv_list = (os.listdir('./csv'))
    
    most_filled_category = 0
    
    for single_csv in csv_list:
        with open('./csv/' + single_csv, 'r') as file:
            reader = csv.reader(file)
            row_count = len(list(reader))-1
            
            if row_count > most_filled_category:
                most_filled_category_name = single_csv
                most_filled_category = row_count
                
    return most_filled_category_name
    
def get_most_expensive_category():
    
    """Cette fonction permet de retourner le nom de la catégorie étant en moyenne la plus chère.
    
    Arguments :
    None
    """
 
    csv_list = (os.listdir('./csv'))
    
    mean_prices = []
    categories = []
    price = 'price_including_tax'
    higher_mean = 0

    for single_csv in csv_list:
        with open('./csv/' + single_csv, 'r') as file:
            reader = csv.DictReader(file)
            category_prices = [float(row[price].replace('£', '')) for row in reader]

            if category_prices:
                mean_price = statistics.mean(category_prices)
                mean_prices.append(mean_price)
                categories.append(single_csv.replace('.csv', ''))
            
    for i in range(0, len(mean_prices)):
        if mean_prices[i] > higher_mean:
            higher_mean = mean_prices[i]
            most_expensive_category = categories[i]
            
    return most_expensive_category