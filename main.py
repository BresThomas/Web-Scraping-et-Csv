# Importation de la bibliothèque csv et de la classe Film
import csv
from Class import Film


liste_films = []  # Création de la liste --> liste_films

with open("Top_Films_Mac.csv",  'r') as f:  # Selon si vous êtes sur Mac ou sur Windows penser à changer le fichier csv
    """ Permet de lire le fichier Csv --> 'Top_Films.csv',
    et d'ajouter tout son contenu dans la liste --> 'liste_csv' """

    lecteur = csv.reader(f, delimiter=";")
    for ligne in lecteur:
        liste_films.append(ligne)  # On ajoute les données du fichier csv "Top_Films" dans le liste "liste_films"

# Si vous avez besoin de créer le fichier csv "new_top_film.csv", ajouté ceci :
# Film.creation_csv(self=None)
# Penser à supprimé la suite du programme pour ne pas créer d'erreur


for n in range(1, 251):  # Boucle pour inscrire les films de 1 à 250
    films_recherche = Film(liste_films[n][0], liste_films[n][1], liste_films[n][2], liste_films[n][3], liste_films)  # Création du film que l'on recherche
    url = films_recherche.url_image()  # Appelle de la fonction url_image issu de la classe Film pour creer une variable "url", soit l'url de l'affiche du film.

    """Pour essayer quelques fonction"""
    #  films_recherche.affiche_titre()
    #  films_recherche.affiche_year()
    #  films_recherche.affiche_note()


    with open('new_top_film.csv', 'a') as f:
        """" Ajout du contenu au fichier Csv --> 'new_top_film.csv'"""

        fieldnames = ['Rank', 'Title', 'Year', 'IMDb_Rating', "Url"]  # Descripteurs du fichier csv
        a_csv = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames, lineterminator='\r')
        # Ajoute une ligne au fichier csv "new_top_films.csc", celle-ci comprend:
        # Le rang du film sur le site IMDB, le titre du film, l'année de sorti, aisni que la note, et l'url de l'affiche du film.
        a_csv.writerow({'Rank': liste_films[n][0], 'Title': liste_films[n][1], 'Year': liste_films[n][2], 'IMDb_Rating': liste_films[n][3], "Url": url})