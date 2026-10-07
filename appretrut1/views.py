from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from .forms import UtiliForm
from .models import utili


# ==========================================
# ACCUEIL TOTAL
# ==========================================

def acceuiltotal(request):
    return render(
        request,
        'appretrut/acceuiltotal.html'
    )


# ==========================================
# INSCRIPTION
# ==========================================

def inscription(request):

    if request.method == 'POST':

        form = UtiliForm(request.POST)

        if form.is_valid():

            utilisateur = form.save(commit=False)

            # Sécuriser le mot de passe
            utilisateur.motdepasse = make_password(
                utilisateur.motdepasse
            )

            utilisateur.save()

            # Garder l'utilisateur connecté
            request.session['utilisateur_id'] = utilisateur.id

            messages.success(
                request,
                "Votre compte a été créé avec succès."
            )

            return redirect('acceuil_utilisateur')

    else:

        form = UtiliForm()

    return render(
        request,
        'appretrut/inscription/inscription.html',
        {
            'form': form
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

        try:

            utilisateur = utili.objects.get(
                email__iexact=email
            )

            # Vérifier le mot de passe
            if check_password(
                motdepasse,
                utilisateur.motdepasse
            ):

                # Nouvelle session
                request.session.cycle_key()

                # Enregistrer l'utilisateur connecté
                request.session['utilisateur_id'] = utilisateur.id

                messages.success(
                    request,
                    "Connexion réussie."
                )

                return redirect(
                    'acceuil_utilisateur'
                )

            else:

                return render(
                    request,
                    'appretrut/connexion.html',
                    {
                        'erreur':
                        'Adresse e-mail ou mot de passe incorrect.'
                    }
                )

        except utili.DoesNotExist:

            return render(
                request,
                'appretrut/connexion.html',
                {
                    'erreur':
                    'Adresse e-mail ou mot de passe incorrect.'
                }
            )

    return render(
        request,
        'appretrut/connexion.html'
    )


# ==========================================
# DECONNEXION
# ==========================================

def deconnexion(request):

    request.session.flush()

    return redirect(
        'connexion'
    )


# ==========================================
# ACCUEIL UTILISATEUR
# ==========================================

def acceuil_utilisateur(request):

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=request.session['utilisateur_id']
    )

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

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    return render(
        request,
        'appretrut/utilisateur/contact.html'
    )


# ==========================================
# ENTREPRISE POUR UTILISATEUR
# ==========================================

def entreprise_utilisateur(request):

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=request.session['utilisateur_id']
    )

    return render(
        request,
        'appretrut/utilisateur/entreprise.html',
        {
            'utilisateur': utilisateur
        }
    )


# ==========================================
# OFFRE UTILISATEUR
# ==========================================

def offre(request):

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    return render(
        request,
        'appretrut/utilisateur/offre.html'
    )


# ==========================================
# TABLEAU DE BORD UTILISATEUR
# ==========================================

def tabbord(request):

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=request.session['utilisateur_id']
    )

    return render(
        request,
        'appretrut/utilisateur/tabbord.html',
        {
            'utilisateur': utilisateur
        }
    )


# ==========================================
# MODIFIER PROFIL
# ==========================================

def modifier_profil(request):

    if 'utilisateur_id' not in request.session:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=request.session['utilisateur_id']
    )

    if request.method == 'POST':

        form = UtiliForm(
            request.POST,
            request.FILES,
            instance=utilisateur
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Votre profil a été modifié."
            )

            return redirect('tabbord')

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



    return render(
        request,
        'appretrut/entreprise/acceuil_entreprise.html',

    )


# ==========================================
# CONTACT ENTREPRISE
# ==========================================

def contact_entreprise(request):

   

    return render(
        request,
        'appretrut/entreprise/contact_entreprise.html'
    )


# ==========================================
# INFORMATIONS ENTREPRISE
# ==========================================

def entreprise_enprise(request):



    return render(
        request,
        'appretrut/entreprise/entreprise_entreprise.html'
    )


# ==========================================
# OFFRE ENTREPRISE
# ==========================================

def offre_entreprise(request):


    return render(
        request,
        'appretrut/entreprise/offre_entreprise.html'
    )


# ==========================================
# TABLEAU DE BORD ENTREPRISE
# ==========================================

def tabbord_entreprise(request):

 

   

    return render(
        request,
        'appretrut/entreprise/tabbord_entreprise.html',
   
    )


# ==========================================
# A PROPOS
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

    return render(
        request,
        'appretrut/administrateur/acceuil_administrateur.html'
    )


# ==========================================
# TABLEAU DE BORD ADMINISTRATEUR
# ==========================================

def tabbord_administrateur(request):

    utilisateurs = utili.objects.all()

    return render(
        request,
        'appretrut/administrateur/tabbord_administrateur.html',
        {
            'utilisateurs': utilisateurs
        }
    )


# ==========================================
# INFORMATIONS UTILISATEUR
# ==========================================

def infos_utilisateur(request, id):

    utilisateur = get_object_or_404(
        utili,
        id=id
    )

    return render(
        request,
        'appretrut/administrateur/infos_utilisateur.html',
        {
            'utilisateur': utilisateur
        }
    )


# ==========================================
# SUPPRIMER UTILISATEUR
# ==========================================

def supprimer_utilisateur(request, id):

    utilisateur = get_object_or_404(
        utili,
        id=id
    )

    utilisateur.delete()

    messages.success(
        request,
        "Utilisateur supprimé avec succès."
    )

    return redirect(
        'tabbord_administrateur'
    )


# ==========================================
# ENTREPRISE ADMINISTRATEUR
# ==========================================

def entreprise_administrateur(request):

    return render(
        request,
        'appretrut/administrateur/entreprise_administrateur.html'
    )


# ==========================================
# OFFRE ADMINISTRATEUR
# ==========================================

def offre_administrateur(request):

    return render(
        request,
        'appretrut/administrateur/offre_administrateur.html'
    )


# ==========================================
# CANDIDATURE ADMINISTRATEUR
# ==========================================

def candidature_administrateur(request):

    return render(
        request,
        'appretrut/administrateur/candidature_administrateur.html'
    )


# ==========================================
# CONTACT ADMINISTRATEUR
# ==========================================

def contact_administrateur(request):

    return render(
        request,
        'appretrut/administrateur/contact_administrateur.html'
    )