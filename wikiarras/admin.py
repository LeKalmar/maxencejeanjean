from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')  # Colonnes affichées
    list_filter = ('created_at', 'updated_at', 'created_by')  # Filtres sur le côté
    search_fields = ('title', 'content', 'created_by__username')  # Barre de recherche
    ordering = ('-created_at',)  # Tri par date de création (récent en premier)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_modified_by')  # Champs non modifiables dans l’admin

    def save_model(self, request, obj, form, change):
        """ Remplit automatiquement les champs utilisateur lors de la création/modification """
        if not obj.pk:  # Si la page est nouvelle
            obj.created_by = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)