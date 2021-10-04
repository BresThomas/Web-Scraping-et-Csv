# Importation de la bibliothèque csv, requests, et BeautifulSoup
import requests
import csv
from bs4 import BeautifulSoup

class Film:
    """ Attributs:
            userAgent: Il est important de mettre votre userAgent avec d'utiliser ce programme.
            liste_films: Liste des données du fichier csv.
            title: Le titre du film.
            rank: Le rank du film sur le site IMDB
            year: L'année de sorti du film
            rating: Le rang sur le site IMDB
            page: L'url de la page de recherche du film dans le site Allociné."""

    def __init__(self, Rank, Title, Year, IMDb_Rating, Liste_films):
        """Initialisation des attributs d’instance"""

        self.userAgent = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0"}
        self.liste_films = Liste_films
        self.title = Title
        self.rank = Rank
        self.year = Year
        self.rating = IMDb_Rating
        self.page = None

    def affiche_titre(self):
        """Affiche le titre du film"""

        print("Le titre du film est : " + self.title)

    def affiche_year(self):
        """Affiche l'année de sorti du film"""

        print("L'année de parution du film est : " + self.year)

    def affiche_note(self):
        """Affiche la note sur le site IMDB du film"""

        print("La note du film est de : " + self.rating)

    def url_image(self):
        """Cherche l'url équivalent à une recherche du film dans la barre de recherche Allociné,
        puis récupere l'url de l'affiche du film depuis sa page allocine"""

        url = "https://www.allocine.fr/rechercher/?q="  # Debut de l'url de la page de recherche du film dans Allociné
        nom = str(self.title).replace(" ", "+")  # Ajout du titre avec le caractère "+" qui remplace les espaces
        self.page = (url + nom)  # Assemblage des 2 variables pour optenir l'url de la page de recherche du film dans le site Allociné.

        r = requests.get(self.page, headers=self.userAgent)  # ouvrir page internet : python - request
        soup = BeautifulSoup(r.text, "html.parser")  # récupère le code source de la page : python  - beautifulsoup
        img = soup.find(alt=self.title)  # Recherche dans le code source la ligne du code correspondant à l'affiche du film
        img_final = img['data-src']  # Récupère le contenu de la ligne

        return img_final  # Renvoie l'url de l'affiche du film
        
    def creation_csv(self):
        """Creation du fichier csv : 'new_top_film.csv', (utile uniquement si il n'existe pas)."""

        with open('new_top_film.csv', 'w', newline="\n") as csvfile:
            """ Permet de creer le fichier Csv --> 'new_top_film.csv' """

            fieldnames = ['Rank', 'Title', 'Year', 'IMDb_Rating', "Url"]  # Ajout des descripteurs
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()  # Ecris les descripteurs dans le fichier csv

