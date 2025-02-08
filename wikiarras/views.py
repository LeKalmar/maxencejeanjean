from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Page, PageHistory, InfoboxType, Infobox
from .forms import PageForm, InfoboxForm, CustomUserCreationForm
import random


def wiki(request):
    return render(request, 'wikiarras/wiki.html')

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    formatted_content = page.content
    infobox = page.infoboxes.first()  # Récupère la première infobox associée à la page

    # Formulaire pour créer ou éditer une infobox
    if request.method == 'POST':
        form = InfoboxForm(request.POST, instance=infobox)
        if form.is_valid():
            infobox = form.save(commit=False)
            infobox.infobox_page = page
            infobox.save()
            return redirect('page_detail', page_id=page.id)
    else:
        form = InfoboxForm(instance=infobox)

    return render(request, 'wikiarras/page_detail.html', {
        'page': page,
        'formatted_content': formatted_content,
        'infobox': infobox,
    })

def page_history(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    history = page.history.all().order_by('-modified_at')
    return render(request, 'wikiarras/page_history.html', {'page': page, 'history': history})

def wiki(request):
    query = request.GET.get("q")  # Récupère la requête de recherche
    if query:
        pages = Page.objects.filter(title__icontains=query)  # Filtre les articles contenant le texte
    else:
        pages = Page.objects.all()  # Affiche toutes les pages par défaut

    return render(request, "wikiarras/wiki.html", {"pages": pages, "query": query})   

def search_ajax(request): #RECHERCHE WIKI
    query = request.GET.get('q', '')
    if query:
        # Rechercher dans le titre et le contenu
        pages = Page.objects.filter(title__icontains=query).order_by('-created_at')
        pages = pages | Page.objects.filter(content__icontains=query).order_by('-created_at')
    else:
        pages = Page.objects.none()

    # Créer une liste des résultats avec uniquement les champs nécessaires
    results = [{'id': page.id, 'title': page.title} for page in pages]
    
    return JsonResponse({'results': results})

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        # Recherche dans le titre d'abord, puis dans le contenu
        pages_title = Page.objects.filter(title__icontains=query).order_by('-created_at')
        pages_content = Page.objects.filter(content__icontains=query).order_by('-created_at')
        # Exclure les pages déjà dans les résultats par titre
        pages = pages_title | pages_content.exclude(id__in=pages_title.values('id'))
    else:
        pages = Page.objects.none()

    return render(request, 'wikiarras/search_results.html', {'pages': pages, 'query': query})

def random_article(request):
    # Récupérer tous les IDs des articles
    ids = Page.objects.values_list('id', flat=True)
    random_article_url = None

    if ids:
        # Choisir un ID au hasard
        random_id = random.choice(ids)
        # Générer l'URL de l'article aléatoire
        random_article_url = f'/wiki/page/{random_id}/'

    return render(request, 'wikiarras/wiki.html', {'random_article_url': random_article_url})

#COMPTE
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez ajouter ici une notification pour l'administrateur
            return redirect('wikiarras:registration_pending')
    else:
        form = CustomUserCreationForm()
    return render(request, 'compte/inscription.html', {'form': form})

@login_required
def activate_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('wikiarras:home')  # Seuls les superutilisateurs peuvent activer des comptes

    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()
    return redirect('wikiarras:admin_dashboard')  # Redirigez vers un tableau de bord administrateur

#EDITION PAGE
@login_required
def create_page(request):
    if request.method == 'POST':
        print("Formulaire soumis !")  # Vérifie si POST est reçu
        print(request.POST)  # Affiche les données reçues
        form = PageForm(request.POST)
        if form.is_valid():
            print("Formulaire valide, enregistrement...")
            page = form.save(commit=False)
            page.created_by = request.user
            page.last_modified_by = request.user  # Définir last_modified_by
            page.save()
            print("Page saved")
            # Enregistrer la création comme la première modification
            PageHistory.objects.create(
                page=page,
                content=page.content,
                modified_by=request.user,
                char_diff=0  # Aucune différence pour la première entrée
            )
            print("PageHistory created")
            return redirect('wikiarras:page_detail', page_id=page.id)
        else:
            print("Form errors:", form.errors)
    else:
        form = PageForm()
    return render(request, 'wikiarras/create_page.html', {'form': form})

@login_required
def page_edit(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            # Récupérer le contenu actuel avant de sauvegarder
            previous_content = page.content

            # Sauvegarder les modifications
            page = form.save(commit=False)
            page.save()

            # Calculer la différence de caractères
            char_diff = len(page.content) - len(previous_content)

            # Enregistrer l'historique avec la différence
            PageHistory.objects.create(
                page=page,
                content=page.content,
                modified_by=request.user,
                char_diff=char_diff
            )

            return redirect('wikiarras:page_detail', page_id=page.id)
    else:
        form = PageForm(instance=page)
    return render(request, 'wikiarras/page_edit.html', {'form': form, 'page': page})
