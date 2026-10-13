from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import make_password, check_password

from .forms import UtiliForm, EntreForm, AdministrateurForm
from .models import utili, entre, administrateur

# ==========================================

# ACCUEIL TOTAL

# ==========================================

def acceuiltotal(request):
    return render(request, 'appretrut/acceuiltotal.html')
# ==========================================

# INSCRIPTION SELON LE RÔLE

# ==========================================


def inscription(request):
    role_choisi = 'utilisateur'

    formulaires = {
        'utilisateur': UtiliForm,
        'entreprise': EntreForm,
        'administrateur': AdministrateurForm,
    }

    if request.method == 'POST':
        role_choisi = request.POST.get('role', 'utilisateur')

        if role_choisi not in formulaires:
            messages.error(request, "Le rôle sélectionné est invalide.")
            return redirect('inscription')

        Formulaire = formulaires[role_choisi]
        form = Formulaire(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'].strip()

            email_existant = (
                utili.objects.filter(email__iexact=email).exists()
                or entre.objects.filter(email__iexact=email).exists()
                or administrateur.objects.filter(email__iexact=email).exists()
            )

            if email_existant:
                form.add_error(
                    'email',
                    "Cette adresse e-mail est déjà utilisée."
                )
            else:
                compte = form.save(commit=False)
                compte.motdepasse = make_password(compte.motdepasse)
                compte.save()

                request.session.flush()
                request.session['compte_id'] = compte.id
                request.session['role'] = role_choisi

                messages.success(
                    request,
                    "Votre compte a été créé avec succès."
                )

                if role_choisi == 'utilisateur':
                    return redirect('acceuil_utilisateur')
                elif role_choisi == 'entreprise':
                    return redirect('acceuil_entreprise')
                else:
                    return redirect('acceuil_administrateur')

    else:
        form = UtiliForm()

return render(
    
        request,
        'appretrut/inscription/inscription.html',
        {
            'form': form,
            'role_choisi': role_choisi,
        }
 )




# ==========================================

# CONNEXION

# ==========================================

def connexion(request):


 if request.method == 'POST':

    email = request.POST.get(
        'email',
        ''
    ).strip()

    motdepasse = request.POST.get(
        'motdepasse',
        ''
    )

    # Rechercher le compte dans les trois modèles
    modeles = [
        ('utilisateur', utili),
        ('entreprise', entre),
        ('administrateur', administrateur),
    ]

    compte_trouve = None
    role_trouve = None

    for role, Modele in modeles:

        compte = Modele.objects.filter(
            email__iexact=email
        ).first()

        if compte is not None:

            if check_password(
                motdepasse,
                compte.motdepasse
            ):
                compte_trouve = compte
                role_trouve = role
                break

    # Si les identifiants sont corrects
    if compte_trouve is not None:

        # Renouveler la session
        request.session.flush()

        request.session['compte_id'] = compte_trouve.id
        request.session['role'] = role_trouve

        messages.success(
            request,
            "Connexion réussie."
        )

        # Rediriger selon le type de compte
        if role_trouve == 'utilisateur':
            return redirect('acceuil_utilisateur')

        elif role_trouve == 'entreprise':
            return redirect('acceuil_entreprise')

        else:
            return redirect('acceuil_administrateur')

    else:

        messages.error(
            request,
            "Adresse e-mail ou mot de passe incorrect."
        )

return render(
    request,
    'appretrut/connexion.html'
)


# ==========================================

# DÉCONNEXION

# ==========================================

def deconnexion(request):


 request.session.flush()

messages.success(
    request,
    "Vous avez été déconnecté."
)

return redirect('connexion')


# ==========================================

# RÉCUPÉRER LE COMPTE CONNECTÉ

# ==========================================

def obtenir_utilisateur_connecte(request):


 compte_id = request.session.get('compte_id')
role = request.session.get('role')

# Vérifier la présence des informations de session
if not compte_id or not role:
    return None

# Associer chaque rôle à son modèle
modeles = {
    'utilisateur': utili,
    'entreprise': entre,
    'administrateur': administrateur,
}

Modele = modeles.get(role)

if Modele is None:
    request.session.flush()
    return None

try:

    return Modele.objects.get(
        id=compte_id
    )

except Modele.DoesNotExist:

    request.session.flush()
    return None


# ==========================================

# VÉRIFIER LE RÔLE

# ==========================================

def verifier_role(request, role_attendu):


 compte = obtenir_utilisateur_connecte(request)

if compte is None:
    return None

role_session = request.session.get('role')

if role_session != role_attendu:
    return None

return compte


# ==========================================

# ACCUEIL UTILISATEUR

# ==========================================

def acceuil_utilisateur(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:

    if not request.session.get('compte_id'):
        return redirect('connexion')

    messages.error(
        request,
        "Vous n'avez pas accès à cet espace."
    )

    return redirect('acceuiltotal')

return render(
    request,
    'appretrut/utilisateur/acceuil_utilisateur.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# CONTACT UTILISATEUR

# ==========================================

def contact(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/utilisateur/contact.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# ENTREPRISES POUR UTILISATEUR

# ==========================================

def entreprise_utilisateur(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/utilisateur/entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# OFFRES POUR UTILISATEUR

# ==========================================

def offre(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/utilisateur/offre.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# TABLEAU DE BORD UTILISATEUR

# ==========================================

def tabbord(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/utilisateur/tabbord.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# MODIFIER LE PROFIL UTILISATEUR

# ==========================================

def modifier_profil(request):


 utilisateur = verifier_role(
    request,
    'utilisateur'
)

if utilisateur is None:
    return redirect('connexion')

if request.method == 'POST':

    form = UtiliForm(
        request.POST,
        instance=utilisateur
    )

    if form.is_valid():

        profil = form.save(commit=False)

        # Conserver le mot de passe existant
        profil.motdepasse = utilisateur.motdepasse

        # Empêcher la modification du rôle
        profil.role = 'utilisateur'

        profil.save()

        messages.success(
            request,
            "Votre profil a été modifié avec succès."
        )

        return redirect('tabbord')

    else:

        messages.error(
            request,
            "Veuillez corriger les erreurs du formulaire."
        )

else:

    form = UtiliForm(
        instance=utilisateur
    )

return render(
    request,
    'appretrut/utilisateur/modifier_profil.html',
    {
        'form': form,
        'utilisateur': utilisateur
    }
)


# ==========================================

# ACCUEIL ENTREPRISE

# ==========================================

def acceuil_entreprise(request):


 utilisateur = verifier_role(
    request,
    'entreprise'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/entreprise/acceuil_entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# CONTACT ENTREPRISE

# ==========================================

def contact_entreprise(request):


 utilisateur = verifier_role(
    request,
    'entreprise'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/entreprise/contact_entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# INFORMATIONS ENTREPRISE

# ==========================================

def entreprise_enprise(request):

 utilisateur = verifier_role(
    request,
    'entreprise'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/entreprise/entreprise_entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# OFFRES ENTREPRISE

# ==========================================

def offre_entreprise(request):


 utilisateur = verifier_role(
    request,
    'entreprise'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/entreprise/offre_entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# TABLEAU DE BORD ENTREPRISE

# ==========================================

def tabbord_entreprise(request):


 utilisateur = verifier_role(
    request,
    'entreprise'
)

if utilisateur is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/entreprise/tabbord_entreprise.html',
    {
        'utilisateur': utilisateur
    }
)


# ==========================================

# À PROPOS

# ==========================================

def aprpos(request):


 return render(
    request,
    'aprpos.html'
)


# ==========================================

# ACCUEIL ADMINISTRATEUR

# ==========================================

def acceuil_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/administrateur/acceuil_administrateur.html',
    {
        'utilisateur': compte_admin,
        'administrateur': compte_admin,
    }
)


# ==========================================

# TABLEAU DE BORD ADMINISTRATEUR

# ==========================================

def tabbord_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

# Récupérer les comptes de chaque table
utilisateurs = utili.objects.filter(
    role='utilisateur'
)

entreprises = entre.objects.all()

administrateurs = administrateur.objects.all()

return render(
    request,
    'appretrut/administrateur/tabbord_administrateur.html',
    {
        'utilisateur': compte_admin,
        'administrateur_connecte': compte_admin,
        'utilisateurs': utilisateurs,
        'entreprises': entreprises,
        'administrateurs': administrateurs,
    }
)


# ==========================================

# INFORMATIONS UTILISATEUR

# ==========================================

def infos_utilisateur(request, id):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

utilisateur = get_object_or_404(
    utili,
    id=id
)

return render(
    request,
    'appretrut/administrateur/infos_utilisateur.html',
    {
        'administrateur': compte_admin,
        'utilisateur': utilisateur,
    }
)

# ==========================================

# SUPPRIMER UN UTILISATEUR

# ==========================================

@require_POST
def supprimer_utilisateur(request, id):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

utilisateur = get_object_or_404(
    utili,
    id=id
)

utilisateur.delete()

messages.success(
    request,
    "Utilisateur supprimé avec succès."
)

return redirect('tabbord_administrateur')


# ==========================================

# ENTREPRISES ADMINISTRATEUR

# ==========================================

def entreprise_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

entreprises = entre.objects.all()

return render(
    request,
    'appretrut/administrateur/entreprise_administrateur.html',
    {
        'administrateur': compte_admin,
        'entreprises': entreprises,
    }
)


# ==========================================

# OFFRES ADMINISTRATEUR

# ==========================================

def offre_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/administrateur/offre_administrateur.html',
    {
        'administrateur': compte_admin
    }
)


# ==========================================

# CANDIDATURES ADMINISTRATEUR

# ==========================================

def candidature_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/administrateur/candidature_administrateur.html',
    {
        'administrateur': compte_admin
    }
)


# ==========================================

# CONTACTS ADMINISTRATEUR

# ==========================================

def contact_administrateur(request):


 compte_admin = verifier_role(
    request,
    'administrateur'
)

if compte_admin is None:
    return redirect('connexion')

return render(
    request,
    'appretrut/administrateur/contact_administrateur.html',
    {
        'administrateur': compte_admin
    }
)

