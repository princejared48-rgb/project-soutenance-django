from django.db import models

class Candidat(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)