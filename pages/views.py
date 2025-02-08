from django.shortcuts import render
from .models import Projet

def index(request):
    projets = Projet.objects.all()  # Tous les projets, triés du plus récent au plus ancien
    projets_epingles = Projet.objects.filter(epingle=True)
    return render(request, 'pages/index.html', {'projets_epingles': projets_epingles, 'projets': projets})

def recherches(request):
    projets_recherches = Projet.objects.filter(type='recherches')
    return render(request, 'pages/recherches.html', {'projets': projets_recherches})

def cartes(request):
    projets_cartes = Projet.objects.filter(type='cartographie')
    return render(request, 'pages/cartes.html', {'projets': projets_cartes})

def genealogie(request):
    projets_genealogie = Projet.objects.filter(type='genealogie')
    return render(request, 'pages/genealogie.html', {'projets': projets_genealogie})

def livres(request):
    return render(request, 'pages/livres.html')

def apropos(request):
    return render(request, 'pages/apropos.html')

def projet_detail(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    if projet.lien:
        # Redirige vers le fichier statique
        return render(request, f'pages/{projet.lien}')
    else:
        return render(request, 'pages/index.html')  # Redirige vers la page d'accueil
    

#Légende de la carte Desailly
# views.py
def desailly_view(request):
    legend_data = [
        {
            "title": "Clergé séculier",
            "items": [
                {"icon": "cathedrale.png", "label": "Cathédrale"},
                {"icon": "eglise-paroissiale.png", "label": "Église paroissiale"},
                {"icon": "Eglise.png", "label": "Église"},
                {"icon": "Paroisse.png", "label": "Paroisse"},
                {"icon": "bat-religieux.png", "label": "Bâtiment religieux"},
                {"icon": "cimetiere.png", "label": "Cimetière"},
            ]
        },
        {
            "title": "Clergé régulier",
            "items": [
                {"icon": "abbaye-saint-vaast.png", "label": "Abbaye Saint-Vaast"},
                {"icon": "Abbaye.png", "label": "Abbaye"},
                {"icon": "refuge-abbaye.png", "label": "Refuge d'Abbaye"},
                {"icon": "Couvent.png", "label": "Couvent"},
                {"icon": "Couvent-point.png", "label": "Bâtiment conventuel"},
            ]
        },
        # Ajoutez d'autres catégories ici
    ]
    return render(request, 'pages/projets/desailly.html', {'legend_data': legend_data})