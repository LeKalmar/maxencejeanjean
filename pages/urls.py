from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recherches/', views.recherches, name='mesrecherches'),
    path('cartes/', views.cartes, name='mescartes'),
    path('genealogie/', views.genealogie, name='genealogie'),
    path('livres/', views.livres, name='livres'),
    path('apropos/', views.apropos, name='apropos'),
    path('projet/<int:projet_id>/', views.projet_detail, name='projet_detail'),
]
