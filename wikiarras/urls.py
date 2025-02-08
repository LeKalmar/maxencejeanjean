from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "wikiarras"

urlpatterns = [
    path('', views.wiki, name='accueil-wiki'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('page/<int:page_id>/edit/', views.page_edit, name='page_edit'),
    path('page/<int:page_id>/history/', views.page_history, name='page_history'),
    path('page/new/', views.create_page, name='create_page'),  # Nouvelle URL pour la création
    path('search/ajax/', views.search_ajax, name='search_ajax'),  # Recherche AJAX
    path('search/', views.search_results, name='search_results'),  # Page de résultats
    path('compte/connexion/', auth_views.LoginView.as_view(template_name='compte/connexion.html'), name='connexion'),
    path('compte/deconnection/', auth_views.LogoutView.as_view(), name='deconnection'),
    path('compte/inscription/', views.register, name='inscription'),
]