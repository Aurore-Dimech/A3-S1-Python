from bs4 import BeautifulSoup
import requests
import csv
import scrap_book_function
import os
import shutil

base_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/"
url = base_url + "/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

directory_name = "images"

try:
    os.mkdir(directory_name)
except FileExistsError:
    shutil.rmtree(directory_name)
    os.mkdir(directory_name)

if response.status_code == 200:
    
    total_number_books = int(soup.select_one('div > form > strong').text)
    scraped_books = []
    
    with open('category.csv', 'w', encoding='utf-8', newline='') as fichier_csv:
        fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
        writer.writeheader()
    
    
    while len(scraped_books) < total_number_books:

        if len(scraped_books) < 20:
            books = soup.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
            try:
                next_page_url = soup.select_one('ul.pager > li.next > a')['href']
            except TypeError as e:
                next_page_url = None
        else:
            books = soup_next_page.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
            try:
                next_page_url = soup_next_page.select_one('ul.pager > li.next > a')['href']
            except:
                next_page_url = None

        url = next_page_url
        response_next_page = requests.get(base_url + str(url), headers=headers)
        soup_next_page = BeautifulSoup(response_next_page.content, 'html.parser')
    
        with open('category.csv', 'a', encoding='utf-8', newline='') as fichier_csv:
            writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
            
            for i in range(0, len(books)):
                product_page_url = str("https://books.toscrape.com/catalogue/" + books[i]['href'].replace('../',''))
        
                data = scrap_book_function.get_informations(product_page_url)
                scraped_books.append(data['universal_product_code (upc)'])

                scrap_book_function.save_image(data['image_url'], data['title'])
            
                writer.writerow(data)     
            

        
else:
    print(f"Erreur : {response.status_code}")