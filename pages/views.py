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
                {"icon": "Cathédrale.png", "label": "Cathédrale"},
                {"icon": "Eglise paroissiale.png", "label": "Église paroissiale"},
                {"icon": "Eglise.png", "label": "Église"},
                {"icon": "Paroisse.png", "label": "Paroisse"},
                {"icon": "Bâtiment religieux.png", "label": "Bâtiment religieux"},
                {"icon": "Cimetière.png", "label": "Cimetière"},
            ]
        },
        {
            "title": "Clergé régulier",
            "items": [
                {"icon": "abbaye Saint-Vaast.png", "label": "Abbaye Saint-Vaast"},
                {"icon": "Abbaye.png", "label": "Abbaye"},
                {"icon": "Refuge d'Abbaye.png", "label": "Refuge d'Abbaye"},
                {"icon": "Couvent.png", "label": "Couvent"},
                {"icon": "Couvent-point.png", "label": "Bâtiment conventuel"},
            ]
        },
        {
            "title": "Administration & justice",
            "items": [
                {"icon": "Bâtiment public.png", "label": "Bâtiment public"},
                {"icon": "Etats d'Artois.png", "label": "Etats d'Artois"},
                {"icon": "Justice.png", "label": "Justice"},
                {"icon": "Hôtel de ville.png", "label": "Hôtel de ville"},
                {"icon": "Prison.png", "label": "Prison"},
                {"icon": "gibet.png", "label": "Gibet"},
            ]
        },
        {
            "title": "Militaire",
            "items": [
                {"icon": "Caserne.png", "label": "Caserne"},
                {"icon": "Caserne-surface.png", "label": "Bâtiment de caserne"},
                {"icon": "Château.png", "label": "Château"},
                {"icon": "Magasin.png", "label": "Magasin"},
                {"icon": "Porte.png", "label": "Porte"},
                {"icon": "Fausse porte.png", "label": "Fausse porte"},
                {"icon": "Rempart.png", "label": "Rempart"},
                {"icon": "Dénivelé.png", "label": "Dénivelé"},
                {"icon": "Terre-plein.png", "label": "Terre-plein"},
            ]
        },
        {
            "title": "Services",
            "items": [
                {"icon": "Hospice.png", "label": "Hospice"},
                {"icon": "Jeu de paume.png", "label": "Jeu de paume"},
                {"icon": "École.png", "label": "École"},
                {"icon": "Pauvreté.png", "label": "Pauvreté"},
                {"icon": "Pensionnat.png", "label": "Pensionnat"},
                {"icon": "Port.png", "label": "Port"},
            ]
        },
        {
            "title": "Moulins",
            "items": [
                {"icon": "Moulin en bois.png", "label": "Moulin en bois"},
                {"icon": "Moulin à tour.png", "label": "Moulin à tour"},
                {"icon": "Moulin détruit.png", "label": "Moulin détruit"},
                {"icon": "Moulin à eau.png", "label": "Moulin à eau"},
            ]
        },
        {
            "title": "Cadastre",
            "items": [
                {"icon": "Bâtiment.png", "label": "Bâtiment"},
                {"icon": "Cour.png", "label": "Cour"},
                {"icon": "Herbe.png", "label": "Friche"},
                {"icon": "Jardin.png", "label": "Jardin"},
                {"icon": "Pré.png", "label": "Prairie"},
                {"icon": "Labour.png", "label": "Terres à labour"},
                {"icon": "Labour & jardinage.png", "label": "Labour & jardinage"},
                {"icon": "Marais.png", "label": "Marais"},
                {"icon": "Disparu.png", "label": "Disparu"},
                {"icon": "Masse.png", "label": "Masse"},
            ]
        },
        {
            "title": "Chaussée",
            "items": [
                {"icon": "Pont.png", "label": "Pont"},
                {"icon": "Escalier.png", "label": "Escalier"},
                {"icon": "Gué.png", "label": "Gué"},
            ]
        },
        {
            "title": "Eau",
            "items": [
                {"icon": "Eau en surface.png", "label": "Eau en surface"},
                {"icon": "Eau souterraine.png", "label": "Eau souterraine"},
            ]
        },
        {
            "title": "Divers",
            "items": [
                {"icon": "Arbre de beaumetz.png", "label": "Arbre de Beaumetz"},
                {"icon": "Arbre.png", "label": "Arbre"},
                {"icon": "Calvaire.png", "label": "Calvaire"},
                {"icon": "Puits.png", "label": "Puits"},
                {"icon": "Source.png", "label": "Source"},
            ]
        },
    ]
    return render(request, 'pages/projets/desailly.html', {'legend_data': legend_data})