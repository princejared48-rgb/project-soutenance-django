from django import forms
from .models import utili, entre, administrateur

# ==========================================

# FORMULAIRE UTILISATEUR

# ==========================================

class UtiliForm(forms.ModelForm):


 confirmation = forms.CharField(
    label="Confirmer le mot de passe",
    widget=forms.PasswordInput(),
    required=True
)

class Meta:
    model = utili

    fields = [
        'nom',
        'prenom',
        'date_naissance',
        'email',
        'telephone',
        'motdepasse',
        'ville',
    ]

    widgets = {
        'motdepasse': forms.PasswordInput(),
        'date_naissance': forms.DateInput(
            attrs={'type': 'date'}
        ),
    }

def clean(self):
    cleaned_data = super().clean()

    motdepasse = cleaned_data.get('motdepasse')
    confirmation = cleaned_data.get('confirmation')

    if motdepasse and confirmation and motdepasse != confirmation:
        self.add_error(
            'confirmation',
            "Les mots de passe ne correspondent pas."
        )

    return cleaned_data


# ==========================================

# FORMULAIRE ENTREPRISE

# ==========================================

class EntreForm(forms.ModelForm):


 confirmation = forms.CharField(
    label="Confirmer le mot de passe",
    widget=forms.PasswordInput(),
    required=True
)

class Meta:
    model = entre

    fields = [
        'nom',
        'prenom',
        'date_naissance',
        'email',
        'telephone',
        'motdepasse',
        'ville',
    ]

    widgets = {
        'motdepasse': forms.PasswordInput(),
        'date_naissance': forms.DateInput(
            attrs={'type': 'date'}
        ),
    }

def clean(self):
    cleaned_data = super().clean()

    motdepasse = cleaned_data.get('motdepasse')
    confirmation = cleaned_data.get('confirmation')

    if motdepasse and confirmation and motdepasse != confirmation:
        self.add_error(
            'confirmation',
            "Les mots de passe ne correspondent pas."
        )

    return cleaned_data


# ==========================================

# FORMULAIRE ADMINISTRATEUR

# ==========================================

class AdministrateurForm(forms.ModelForm):


 confirmation = forms.CharField(
    label="Confirmer le mot de passe",
    widget=forms.PasswordInput(),
    required=True
)

class Meta:
    model = administrateur

    fields = [
        'nom',
        'prenom',
        'date_naissance',
        'email',
        'telephone',
        'motdepasse',
        'ville',
        'nationalite',
    ]

    widgets = {
        'motdepasse': forms.PasswordInput(),
        'date_naissance': forms.DateInput(
            attrs={'type': 'date'}
        ),
    }

def clean(self):
    cleaned_data = super().clean()

    motdepasse = cleaned_data.get('motdepasse')
    confirmation = cleaned_data.get('confirmation')

    if motdepasse and confirmation and motdepasse != confirmation:
        self.add_error(
            'confirmation',
            "Les mots de passe ne correspondent pas."
        )

    return cleaned_data






