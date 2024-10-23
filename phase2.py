from bs4 import BeautifulSoup
import requests
import csv
import scrap_book_function

url = "https://books.toscrape.com/catalogue/category/books/psychology_26/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


if response.status_code == 200:
    
    books = soup.select('section > div:nth-child(2) > ol > li > .product_pod > .image_container > a')
    
    with open('category.csv', 'w', encoding='utf-8', newline='') as fichier_csv:
        fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
        writer.writeheader()
    
        for i in range(0, len(books)):
            product_page_url = str("https://books.toscrape.com/catalogue/" + books[i]['href'].replace('../',''))
        
            data = scrap_book_function.get_informations(product_page_url)
            
            writer.writerow(data)     
        
else:
    print(f"Erreur : {response.status_code}")