from django import forms
from .models import Page
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Infobox, InfoboxType
from tinymce.widgets import TinyMCE  # Importer TinyMCEWidget

#COMPTE
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Le compte est inactif par défaut
        if commit:
            user.save()
        return user
    
# PAGE
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
        labels = {
            'title': "Titre",
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Entrez le titre ici...', 'class': 'article-title-input'}),
            'content': TinyMCE(attrs={'placeholder': 'Écrivez ici...', 'class': 'tinymce-editor'}),  # Utiliser TinyMCEWidget
        }

#INFOBOX
class InfoboxForm(forms.ModelForm):
    class Meta:
        model = Infobox
        fields = ['infobox_type', 'title', 'description', 'date_of_birth', 'date_of_death',
                  'construction_date', 'demolition_date', 'architect', 'first_mention', 'replaced_by', 'replaces'
                  ]