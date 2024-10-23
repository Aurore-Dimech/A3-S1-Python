
from bs4 import BeautifulSoup
import requests
import re
from word2number import w2n
from PIL import Image


url = "https://books.toscrape.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


def get_informations(scrapped_url):
    response_single_book = requests.get(scrapped_url, headers=headers)
    soup_single_book = BeautifulSoup(response_single_book.content, 'html.parser')
    
    data = {}
    data['product_page_url'] = scrapped_url
        
    if response.status_code == 200:  
        data['universal_product_code (upc)'] = soup_single_book.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type').text
        data['title'] = soup_single_book.select_one('h1').text
        data['price_including_tax'] = soup_single_book.select_one('table > tr:nth-child(4) td:first-of-type').text
        data['price_excluding_tax'] = soup_single_book.select_one('table > tr:nth-child(3) td:first-of-type').text
        
        availability = soup_single_book.select_one('table > tr:nth-child(6) td:first-of-type').text
        data['number_available'] = re.search(r"\d+", availability).group()
        
        data['product_description'] = soup_single_book.select_one('div#product_description ~ p').text
        data['category'] = soup_single_book.select_one('ul.breadcrumb > li:nth-child(3) > a').text
        
        data['review_rating'] = w2n.word_to_num(soup_single_book.find('p', class_='star-rating')['class'][1])
        
        data['image_url'] = str(url + soup_single_book.find('img')['src'].replace('../',''))
        
        return data
        
    else:
        print(f"Erreur : {response.status_code}")
            

def save_image(image_url):
    Image.open(image_url)            