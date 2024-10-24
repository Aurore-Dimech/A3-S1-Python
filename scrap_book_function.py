
from bs4 import BeautifulSoup
import requests
import re
from word2number import w2n
from PIL import Image
from urllib.request import urlopen
import os
import shutil


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
    image_name -- nome que l'on veut donner à l'image
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
    image_name -- nome que l'on veut donner à l'image
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