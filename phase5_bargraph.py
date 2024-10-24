import csv
import os, os.path
import matplotlib.pyplot as plt
import statistics

def make_bar_graph():
    """Cette fonction permet de créer un graphique en bar à partir d'un ensemble de csv.
    
    Arguments :
    None
    """
    
    plt.close()
    
    csv_list = (os.listdir('./csv'))

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
    
    if __name__ != "__main__":
        plt.savefig('./graphs/bar_graph.png')
        plt.close()

    
if __name__ == "__main__":
    make_bar_graph()
    plt.show()