from bs4 import BeautifulSoup
import requests
import csv
import re
from word2number import w2n

url = "https://books.toscrape.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


if response.status_code == 200:
    
    books = soup.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
    
    for book in books:
    
        product_page_url = book['href']
        
        url_single_book = str("https://books.toscrape.com/" + product_page_url)
    
        response_single_book = requests.get(url_single_book, headers=headers)
        soup_single_book = BeautifulSoup(response_single_book.text, 'html.parser')
        
        if response.status_code == 200:
    
            data = {}
            
            universal_product_code = soup_single_book.select_one('div.page > div.page_inner > .content > #content_inner > .product_page > table > tr:first-of-type td:first-of-type').text
            title = soup_single_book.select_one('h1').text
            price_including_tax = soup_single_book.select_one('table > tr:nth-child(4) td:first-of-type').text
            price_excluding_tax = soup_single_book.select_one('table > tr:nth-child(3) td:first-of-type').text
    
            availability = soup_single_book.select_one('table > tr:nth-child(6) td:first-of-type').text
            number_available = re.search(r"\d+", availability).group()
    
            product_description = soup_single_book.select_one('div#product_description ~ p').text
            category = soup_single_book.select_one('ul.breadcrumb > li:nth-child(3)').text
    
            review_rating = w2n.word_to_num(soup_single_book.find('p', class_='star-rating')['class'][1])
    
            image_url = str(url + soup_single_book.find('img')['src'].replace('../',''))
            
            data['title'] = title
        else:
            print(f"Erreur : {response.status_code}")
        
    with open('single_book.csv', 'w', encoding='utf-8', newline='') as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
        writer.writeheader()
            
        writer.writerow({'product_page_url': url_single_book, 'universal_product_code (upc)': universal_product_code, 'title': title, 'price_including_tax' : price_including_tax, 'price_excluding_tax': price_excluding_tax, 'number_available': number_available, 'product_description': product_description, 'category': category, 'review_rating': review_rating, 'image_url': image_url})
        print('encoding over')
        
else:
    print(f"Erreur : {response.status_code}")