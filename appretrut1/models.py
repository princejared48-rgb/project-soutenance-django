
from django.db import models


# ==========================================
# MODÈLE UTILISATEUR
# ==========================================

class utili(models.Model):

    ROLES = [
        ('utilisateur', 'Utilisateur'),
        ('entreprise', 'Entreprise'),
        ('administrateur', 'Administrateur'),
    ]

    nom = models.CharField(max_length=100)

    prenom = models.CharField(max_length=100)

    date_naissance = models.DateField()

    email = models.EmailField(
        max_length=100,
        unique=True
    )

    telephone = models.CharField(max_length=100)

    motdepasse = models.CharField(max_length=128)

    ville = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    nationalite = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    domaine = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    metier = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    niveau_etudes = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    competence = models.TextField(
        blank=True,
        null=True
    )

    # Rôle attribué au compte
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='utilisateur'
    )

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.role}"


# ==========================================
# MODÈLE ENTREPRISE
# ==========================================

class entre(models.Model):

    nom = models.CharField(max_length=100)

    prenom = models.CharField(max_length=100)

    date_naissance = models.DateField()

    email = models.EmailField(
        max_length=100,
        unique=True
    )

    telephone = models.CharField(max_length=100)

    motdepasse = models.CharField(max_length=128)

    ville = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    nationalite = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    domaine = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    metier = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    niveau_etudes = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    competence = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# ==========================================

# MODÈLE ADMINISTRATEUR

# ==========================================

class administrateur(models.Model):


 nom = models.CharField(max_length=100)

prenom = models.CharField(max_length=100)

date_naissance = models.DateField()

email = models.EmailField(
    max_length=100,
    unique=True
)

telephone = models.CharField(max_length=100)

motdepasse = models.CharField(max_length=128)

ville = models.CharField(
    max_length=100,
    blank=True,
    null=True
)

nationalite = models.CharField(
    max_length=100,
    blank=True,
    null=True
)

def __str__(self):
    return f"{self.prenom} {self.nom} - Administrateur"






