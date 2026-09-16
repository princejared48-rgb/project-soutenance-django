from django.shortcuts import render, redirect, get_object_or_404

from .forms import UtiliForm
from .models import utili


def acceuiltotal(request):
    return render(request, 'appretrut/acceuiltotal.html')


def acceuil_utilisateur(request):
    return render(
        request,
        'appretrut/utilisateur/acceuil_utilisateur.html'
    )


def contact(request):
    return render(
        request,
        'appretrut/utilisateur/contact.html'
    )


def entreprise(request):
    return render(
        request,
        'appretrut/utilisateur/entreprise.html'
    )


def offre(request):
    return render(
        request,
        'appretrut/utilisateur/offre.html'
    )


# =========================
# PROFIL UTILISATEUR
# =========================

def tabbord(request):

    utilisateur_id = request.session.get('utilisateur_id')

    if not utilisateur_id:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=utilisateur_id
    )

    return render(
        request,
        'appretrut/utilisateur/tabbord.html',
        {
            'utilisateur': utilisateur
        }
    )


# =========================
# ADMINISTRATEUR
# =========================

def acceuil_administrateur(request):
    return render(
        request,
        'appretrut/administrateur/acceuil_administrateur.html'
    )


def tabbord_administrateur(request):

    utilisateurs = utili.objects.all()

    return render(
        request,
        'appretrut/administrateur/tabbord_administrateur.html',
        {
            'utilisateurs': utilisateurs
        }
    )


def supprimer_utilisateur(request, id):

    utilisateur = get_object_or_404(
        utili,
        id=id
    )

    utilisateur.delete()

    return redirect('tabbord_administrateur')


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


def entreprise_administrateur(request):
    return render(
        request,
        'appretrut/administrateur/entreprise_administrateur.html'
    )


def offre_administrateur(request):
    return render(
        request,
        'appretrut/administrateur/offre_administrateur.html'
    )


def candidature_administrateur(request):
    return render(
        request,
        'appretrut/administrateur/candidature_administrateur.html'
    )


def contact_administrateur(request):
    return render(
        request,
        'appretrut/administrateur/contact_administrateur.html'
    )


# =========================
# CONNEXION
# =========================
def connexion(request):
    if request.method == "POST":
        email = request.POST.get("email")
        motdepasse = request.POST.get("motdepasse")

        try:
            utilisateur = utili.objects.get(
                email=email,
                motdepasse=motdepasse
            )

            request.session['utilisateur_id'] = utilisateur.id

            return redirect("tabbord")

        except utili.DoesNotExist:
            return render(
                request,
                'appretrut/connexion.html',
                {
                    'erreur': 'Email ou mot de passe incorrect.'
                }
            )

    return render(request, 'appretrut/connexion.html')


# =========================
# INSCRIPTION
# =========================

def inscription(request):

    if request.method == "POST":

        form = UtiliForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            print("FORMULAIRE VALIDE")

            utilisateur = form.save()

            print(
                "UTILISATEUR ENREGISTRE :",
                utilisateur
            )

            # Enregistrer son ID dans la session
            request.session['utilisateur_id'] = utilisateur.id

            # Aller vers son profil
            return redirect("tabbord")

        else:

            print(
                "ERREURS DU FORMULAIRE :",
                form.errors
            )

    else:

        form = UtiliForm()

    return render(
        request,
        'appretrut/inscription/inscription.html',
        {
            'form': form
        }
    )