from django.urls import path
from . import views

app_name = "wikiarras"

urlpatterns = [
    path('', views.wiki, name='accueil-wiki'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('page/<int:page_id>/edit/', views.page_edit, name='page_edit'),
]