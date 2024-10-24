import csv
import os, os.path
import matplotlib.pyplot as plt
import scrap_book_function

scrap_book_function.create_directory('graphs')

def make_pie_graph():
    """Cette fonction permet de créer un diagramme circulaire à partir d'un ensemble de csv.
    
    Arguments :
    None
    """
    
    plt.close()
    
    csv_list = (os.listdir('./csv'))

    pie_labels = []
    y = []

    for single_csv in csv_list:
        with open('./csv/' + single_csv, 'r') as file:
            reader = csv.reader(file)
            row_count = len(list(reader))-1
            pie_labels.append(single_csv)
            y.append(row_count)
        

    plt.pie(y, labels = pie_labels, autopct='%1.1f%%')
    plt.title('Pourcentage de livres en fonction de la catégorie')
    plt.savefig('./graphs/pie_graph.png')
    
    if __name__ != "__main__":
        plt.savefig('./graphs/pie_graph.png')
        plt.close()
 
   
if __name__ == "__main__":
    make_pie_graph()
    plt.show() 