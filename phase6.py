from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import scrap_book_function
from reportlab.lib.utils import ImageReader
import phase5_bargraph
import phase5_piegraph
import os

scrap_book_function.create_directory('graphs')

phase5_bargraph.make_bar_graph()
phase5_piegraph.make_pie_graph()

global_mean_price = scrap_book_function.get_global_mean()
most_filled_category = scrap_book_function.get_most_filled_category()
most_expensive_category = scrap_book_function.get_most_expensive_category()

def create_pdf(filename, title, key):
    
    """Cette fonction permet de créer un pdf affichant diverses informations récupérées en scrapant le site.
    
    Arguments :
    filename -- nom du pdf généré
    title -- titre apparaissant au début du pdf
    key -- clé unique associée au titre
    """
    
    c = canvas.Canvas(filename, pagesize=A4)
    
    c.bookmarkPage(key)
    
    c.addOutlineEntry(title, key, level=0, closed=None)
    c.setTitle(title)
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, title)
    
    c.setFont("Helvetica-Bold", 14)
    subtitle_graph = 'Représentations graphiques'
    c.drawString(100, 750, subtitle_graph)
    
    c.setFont("Helvetica", 12)
    
    pie_graph_path = './graphs/pie_graph.png'
    bar_graph_path = './graphs/bar_graph.png'
    
    pie_graph_desc = "Le graphique ci-dessous montre la répartition des livres en fonction des catégories :"
    c.drawString(100, 710, pie_graph_desc)
    
    if os.path.exists(pie_graph_path):
        pie_graph = ImageReader(pie_graph_path)
        c.drawImage(pie_graph, 100, 390, width=400, height=300)
        
    bar_graph_desc = "Le graphique ci-dessous montre le prix moyen des livres selon la catégorie :"
    c.drawString(100, 360, bar_graph_desc)
    
    if os.path.exists(bar_graph_path):
        bar_graph = ImageReader(bar_graph_path)
        c.drawImage(bar_graph, 100, 40, width=400, height=300)
    
    
    c.showPage()
    
    c.setFont("Helvetica-Bold", 14)
    subtitle_graph = 'Statistiques clés'
    c.drawString(100, 800, subtitle_graph)
    
    c.setFont("Helvetica", 12)
    pie_graph_desc = str("Prix moyen global des livres : £" + global_mean_price)
    c.drawString(100, 760, pie_graph_desc)
    
    pie_graph_desc = str("Catégorie la plus représentée : " + most_filled_category)
    c.drawString(100, 740, pie_graph_desc)
    
    pie_graph_desc = str("Catégorie la plus chère : " + most_expensive_category)
    c.drawString(100, 720, pie_graph_desc)
    
    c.save()

create_pdf("rapport_prix_livres.pdf", "Rapport des prix des livres d'occasion", 'title_outline')