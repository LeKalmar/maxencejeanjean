from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField  # Remplacer RichTextField par HTMLField

# PAGES
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()  # Utiliser HTMLField de TinyMCE
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_pages')
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_pages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PageHistory(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='history')
    content = models.TextField()
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)
    char_diff = models.IntegerField(default=0)  # Nombre de caractères ajoutés ou supprimés

    def __str__(self):
        return f"Modification de {self.page.title} par {self.modified_by.username} à {self.modified_at}"
    
    #INFOBOX
class InfoboxType(models.Model):
    infobox_type_name = models.CharField(max_length=10)  # Nom du type (ex: Personne, Bâtiment, etc.)
    color_code = models.CharField(max_length=7)  # Code couleur pour le fond de l'infobox (ex : "#FFFF00" pour jaune)

    def __str__(self):
        return self.infobox_type_name
    
class Infobox(models.Model):
    infobox_page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='infoboxes')
    infobox_type = models.ForeignKey(InfoboxType, on_delete=models.CASCADE)  # Type d'infobox
    title = models.CharField(max_length=255)  # Le titre de l'infobox
    description = models.TextField(blank=True, null=True)  # Informations générales
    
    # Champs dynamiques pour chaque type d'infobox
    date_of_birth = models.DateField(null=True, blank=True)  # Date de naissance (pour une Personne)
    date_of_death = models.DateField(null=True, blank=True)  # Date de décès (pour une Personne)
    construction_date = models.DateField(null=True, blank=True)  # Date de construction (pour un Bâtiment)
    demolition_date = models.DateField(null=True, blank=True)  # Date de démolition (pour un Bâtiment)
    architect = models.CharField(max_length=255, null=True, blank=True)  # Architecte ou entreprise (pour un Bâtiment)
    first_mention = models.CharField(max_length=255, null=True, blank=True)  # Première mention (pour un Lieu-dit)
    
    # Champs pour les entités remplacées/remplaçantes
    replaced_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replaces_set')
    replaces = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replaced_by_set')

    def __str__(self):
        return f'Infobox: {self.title} ({self.infobox_type.infobox_type_name})'