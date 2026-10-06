from django.db import models


class utili(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    telephone = models.CharField(max_length=100)

    # PAS de unique=True ici
    motdepasse = models.CharField(max_length=128)
    ville = models.CharField(max_length=100, blank=True, null=True)
nationalite = models.CharField(max_length=100, blank=True, null=True)
domaine = models.CharField(max_length=100, blank=True, null=True)
metier = models.CharField(max_length=100, blank=True, null=True)
experience = models.CharField(max_length=100, blank=True, null=True)
niveau_etudes = models.CharField(max_length=100, blank=True, null=True)
competence = models.TextField(blank=True, null=True)