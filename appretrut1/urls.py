from django.urls import path
from . import views


urlpatterns = [

    # ==========================================
    # ACCUEIL
    # ==========================================

    path(
        '',
        views.acceuiltotal,
        name='acceuiltotal'
    ),


    # ==========================================
    # CONNEXION / INSCRIPTION
    # ==========================================

    path(
        'connexion/',
        views.connexion,
        name='connexion'
    ),

    path(
        'inscription/',
        views.inscription,
        name='inscription'
    ),

    path(
        'deconnexion/',
        views.deconnexion,
        name='deconnexion'
    ),


    # ==========================================
    # ESPACE UTILISATEUR
    # ==========================================

    path(
        'utilisateur/',
        views.acceuil_utilisateur,
        name='acceuil_utilisateur'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'entreprise/',
        views.entreprise_utilisateur,
        name='entreprise_utilisateur'
    ),

    path(
        'offre/',
        views.offre,
        name='offre'
    ),

    path(
        'tabbord/',
        views.tabbord,
        name='tabbord'
    ),

    path(
        'modifier-profil/',
        views.modifier_profil,
        name='modifier_profil'
    ),



# ==========================================
# ESPACE ENTREPRISE
# ==========================================

path(
    'entreprisee/',
    views.acceuil_entreprise,
    name='acceuil_entreprise'
),

path(
    'entreprisee/contact/',
    views.contact_entreprise,
    name='contact_entreprise'
),



path(
    'entreprisee/offres/',
    views.offre_entreprise,
    name='offre_entreprise'
),

path(
    'entreprisee/tabbord/',
    views.tabbord_entreprise,
    name='tabbord_entreprise'
),
    # ==========================================
    # A PROPOS
    # ==========================================

    path(
        'aprpos/',
        views.aprpos,
        name='aprpos'
    ),


    # ==========================================
    # ADMINISTRATEUR
    # ==========================================

    path(
        'administrateur/',
        views.acceuil_administrateur,
        name='acceuil_administrateur'
    ),

    path(
        'administrateur/tabbord/',
        views.tabbord_administrateur,
        name='tabbord_administrateur'
    ),

    path(
        'administrateur/entreprises/',
        views.entreprise_administrateur,
        name='entreprise_administrateur'
    ),

    path(
        'administrateur/offres/',
        views.offre_administrateur,
        name='offre_administrateur'
    ),

    path(
        'administrateur/candidatures/',
        views.candidature_administrateur,
        name='candidature_administrateur'
    ),

    path(
        'administrateur/contacts/',
        views.contact_administrateur,
        name='contact_administrateur'
    ),

    path(
        'administrateur/utilisateur/<int:id>/',
        views.infos_utilisateur,
        name='infos_utilisateur'
    ),

    path(
        'administrateur/utilisateur/<int:id>/supprimer/',
        views.supprimer_utilisateur,
        name='supprimer_utilisateur'
    ),

]