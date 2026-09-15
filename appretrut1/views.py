from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UtiliForm
from .models import utili



def acceuiltotal(request):
    return render(request, 'appretrut/acceuiltotal.html')

def acceuil_utilisateur(request):
    return render(request, 'appretrut/utilisateur/acceuil_utilisateur.html')
def contact(request):
    return render(request, 'appretrut/utilisateur/contact.html')   
def entreprise(request):
    return render(request, 'appretrut/utilisateur/entreprise.html')
def offre(request):
    return render(request, 'appretrut/utilisateur/offre.html')        
def tabbord(request):
    return render(request, 'appretrut/utilisateur/tabbord.html')        


def acceuil_administrateur(request):    
    return render(request, 'appretrut/administrateur/acceuil_administrateur.html')    
def tabbord_administrateur(request):

    utilisateurs = utili.objects.all()

    return render(
        request,
        'appretrut/administrateur/tabbord_administrateur.html',
        {'utilisateurs': utilisateurs}
    )


def supprimer_utilisateur(request, id):

    utilisateur = get_object_or_404(
        utili,
        id=id
    )

    utilisateur.delete()

def infos_utilisateur(request, id):
    utilisateur = get_object_or_404(utili, id=id)

    return render(
        request,
        'appretrut/administrateur/infos_utilisateur.html',
        {'utilisateur': utilisateur}
    )
def infos_utilisateur(request, id):
    utilisateur = get_object_or_404(utili, id=id)

    return render(
        request,
        'appretrut/administrateur/infos_utilisateur.html',
        {'utilisateur': utilisateur}
    )
    
def entreprise_administrateur(request):    
    return render(request, 'appretrut/administrateur/entreprise_administrateur.html') 
def offre_administrateur(request):    
    return render(request, 'appretrut/administrateur/offre_administrateur.html')
def candidature_administrateur(request):
    return render(request, 'appretrut/administrateur/candidature_administrateur.html')

def contact_administrateur(request):    
    return render(request, 'appretrut/administrateur/contact_administrateur.html')
def connexion(request):    
    return render(request, 'appretrut/connexion.html')
def inscription(request):

    if request.method == "POST":
        form = UtiliForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("candidature_administrateur")

    else:
        form = UtiliForm()

    return render(
        request,
        'appretrut/inscription/inscription.html',
        {'form': form}
    )
     