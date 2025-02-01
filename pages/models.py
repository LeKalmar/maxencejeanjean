from django.db import models

class Projet(models.Model):
    TYPE_CHOICES = [
        ('cartographie', '🗺️ Cartographie'),
        ('livres', '📖 Livres'),
        ('genealogie', '🌳 Généalogie'),
        ('recherches', '🗃️ Recherches'),
        ('autre', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/')
    image_caption= models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    epingle = models.BooleanField(default=False)

    lien = models.CharField(max_length=200, blank=True, null=True)  # Lien vers la page détaillée


    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_creation']  # Trie les projets du plus récent au plus ancien
        db_table = 'pages_projet'  # Nom de la table dans la base de donnée
