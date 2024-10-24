import csv
import os, os.path
import matplotlib.pyplot as plt
import statistics

csv_list = (os.listdir('./csv'))

pie_labels = []
y = []

for single_csv in csv_list:
    with open('./csv/' + single_csv, 'r') as file:
        reader = csv.reader(file)
        row_count = len(list(reader))-1
        pie_labels.append(single_csv)
        y.append(row_count)
        

# plt.pie(y, labels = pie_labels, autopct='%1.1f%%')
# plt.title('Pourcentage de livres en fonction de la catégorie')
# plt.show() 


mean_prices = []
categories = []
price = 'price_including_tax'

for single_csv in csv_list:
    with open('./csv/' + single_csv, 'r') as file:
        reader = csv.DictReader(file)
        category_prices = [float(row[price].replace('£', '')) for row in reader]

        if category_prices:
            mean_price = statistics.mean(category_prices)
            mean_prices.append(mean_price)
            categories.append(single_csv.replace('.csv', ''))

plt.barh(categories, mean_prices)
plt.xlabel('Prix moyen (en £)')
plt.ylabel('Catégories')
plt.title('Prix moyen des livres en fonction de la catégorie')
plt.show()