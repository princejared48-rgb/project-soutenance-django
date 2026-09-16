from django.shortcuts import render, redirect, get_object_or_404

from .forms import UtiliForm
from .models import utili
from datetime import datetime


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


def inscription(request):
    if request.method == "POST":
        print("FICHIERS RECUS :", request.FILES)

        form = UtiliForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            utilisateur = form.save()

            print("PHOTO ENREGISTREE :", utilisateur.photo)
            print("URL PHOTO :", utilisateur.photo.url if utilisateur.photo else "AUCUNE PHOTO")

            request.session['utilisateur_id'] = utilisateur.id
            return redirect("tabbord")

        else:
            print("ERREURS :", form.errors)

    else:
        form = UtiliForm()

    return render(
        request,
        'appretrut/inscription/inscription.html',
        {'form': form}
    )
def modifier_profil(request):

    utilisateur_id = request.session.get('utilisateur_id')

    if not utilisateur_id:
        return redirect('connexion')

    utilisateur = get_object_or_404(
        utili,
        id=utilisateur_id
    )

    if request.method == "POST":

        # Récupération des données
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date_naissance')
        sexe = request.POST.get('sexe')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        nationalite = request.POST.get('nationalite')
        domaine = request.POST.get('domaine')
        metier = request.POST.get('metier')
        experience = request.POST.get('experience')
        niveau_etudes = request.POST.get('niveau_etudes')
        competence = request.POST.get('competence')
        motdepasse = request.POST.get('motdepasse')

        # Modifier les champs
        utilisateur.nom = nom
        utilisateur.prenom = prenom

        # IMPORTANT : ne pas mettre None dans date_naissance
        if date_naissance:
            utilisateur.date_naissance = datetime.strptime(
                date_naissance,
                '%Y-%m-%d'
            ).date()
        
        utilisateur.motdepasse = motdepasse
        utilisateur.sexe = sexe
        utilisateur.email = email
        utilisateur.telephone = telephone
        utilisateur.ville = ville
        utilisateur.nationalite = nationalite
        utilisateur.domaine = domaine
        utilisateur.metier = metier
        utilisateur.experience = experience
        utilisateur.niveau_etudes = niveau_etudes
        utilisateur.competence = competence

        # Nouvelle photo
        if request.FILES.get('photo'):
            utilisateur.photo = request.FILES.get('photo')

        # Sauvegarde
        utilisateur.save()

        return redirect('tabbord')

    return redirect('tabbord')  