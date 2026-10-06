from django import forms
from .models import utili


class UtiliForm(forms.ModelForm):

    confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmer le mot de passe'}
        ),
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
        ]

        widgets = {
            'motdepasse': forms.PasswordInput(
                attrs={'placeholder': 'Mot de passe'}
            ),

            'date_naissance': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        motdepasse = cleaned_data.get('motdepasse')
        confirmation = cleaned_data.get('confirmation')

        if motdepasse and confirmation:
            if motdepasse != confirmation:
                raise forms.ValidationError(
                    "Les deux mots de passe ne correspondent pas."
                )

        return cleaned_data

