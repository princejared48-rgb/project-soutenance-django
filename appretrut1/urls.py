
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuiltotal, name='acceuiltotal'),
    path('utilisateur/', views.acceuil_utilisateur, name='acceuil_utilisateur'),
    path('contact/', views.contact, name='contact'),
    path('entreprise/', views.entreprise, name='entreprise'),
    path('offre/', views.offre, name='offre'),
    path('tabbord/', views.tabbord, name='tabbord'),        
    path('administrateur/', views.acceuil_administrateur, name='acceuil_administrateur'),
    path('tabbord_administrateur/', views.tabbord_administrateur, name='tabbord_administrateur'),
    path('entreprise_administrateur/', views.entreprise_administrateur, name='entreprise_administrateur'),
    path('offre_administrateur/', views.offre_administrateur, name='offre_administrateur'),
    path('candidature_administrateur/', views.candidature_administrateur, name='candidature_administrateur'),
    path('contact_administrateur/', views.contact_administrateur, name='contact_administrateur'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'), 
    path('supprimer-utilisateur/<int:id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
    path('modifier-profil/', views.modifier_profil, name='modifier_profil'),   
]