from django.db import models


class utili(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=100,unique=True)
    telephone = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    sexe = models.CharField(max_length=20)
    metier = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    niveau_etudes = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    domaine = models.CharField(max_length=150)
    motdepasse = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)
    competence = models.TextField(blank=True, null=True)
    