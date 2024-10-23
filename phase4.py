from bs4 import BeautifulSoup
import requests
import csv
import scrap_book_function
import re


base_url = "https://books.toscrape.com/"
url = base_url + "index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

scrap_book_function.create_directory('images')
scrap_book_function.create_directory('csv')


if response.status_code == 200:
    
    categories = soup.select('.nav-list > li > ul li > a')
    for category in categories:
        scrap_book_function.create_directory(str('./images/' + category.text.strip()))
        
        csv_path = './csv/' + category.text.strip() 
        with open(csv_path, 'w', encoding='utf-8', newline='') as fichier_csv:
            fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
            writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
            writer.writeheader()
        
    
        category_url = base_url + str(category['href'])
        response_category = requests.get(category_url, headers=headers)
        soup_category = BeautifulSoup(response_category.content, 'html.parser')
    
        total_number_books = int(soup_category.select_one('div > form > strong').text)
        scraped_books = []
        
        while len(scraped_books) < total_number_books:
            
            if len(scraped_books) < 20:
                books = soup_category.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
                try:
                    next_page_url = soup_category.select_one('ul.pager > li.next > a')['href']
                except TypeError as e:
                    next_page_url = None
            else:
                books = soup_next_page.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
                try:
                    next_page_url = soup_next_page.select_one('ul.pager > li.next > a')['href']
                except:
                    next_page_url = None

            url = next_page_url
            response_next_page = requests.get(category_url.replace('index.html', '') + str(url), headers=headers)
            soup_next_page = BeautifulSoup(response_next_page.content, 'html.parser')
    
            with open(csv_path, 'a', encoding='utf-8', newline='') as fichier_csv:
                writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)

                for i in range(0, len(books)):
                    product_page_url = str("https://books.toscrape.com/catalogue/" + books[i]['href'].replace('../',''))
                    data = scrap_book_function.get_informations(product_page_url)
                    scraped_books.append(data['universal_product_code (upc)'])

                    scrap_book_function.save_image_in_directory(data['image_url'], category.text.strip(), data['title'])

                    writer.writerow(data)   
                        
else:
        print(f"Erreur : {response.status_code}")