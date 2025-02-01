# Generated by Django 5.1.5 on 2025-01-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_projet_epingle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='type',
            field=models.CharField(choices=[('cartographie', '🗺️ Cartographie'), ('livres', '📖 Livres'), ('genealogie', '🌳 Généalogie'), ('recherches', '🗃️ Recherches'), ('autre', 'Autre')], max_length=20),
        ),
    ]
