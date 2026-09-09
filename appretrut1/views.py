from django.shortcuts import render



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


# def acceuil_administrateur(request):    
#     return render(request, 'appretrut/administrateur/acceuil_administrateur.html')    
# def tabbord_administrateur(request):    
#     return render(request, 'appretrut/administrateur/tabbord_administrateur.html')    
# def entreprise_administrateur(request):    
#     return render(request, 'appretrut/administrateur/entreprise_administrateur.html') 
# def offre_administrateur(request):    
#     return render(request, 'appretrut/administrateur/offre_administrateur.html')
# def candidature_administrateur(request):    
#     return render(request, 'appretrut/administrateur/candidature_administrateur.html')    

# def contact_administrateur(request):    
#     return render(request, 'appretrut/administrateur/contact_administrateur.html')
def connexion(request):    
    return render(request, 'appretrut/connexion.html')
def inscription(request) :    
    return render(request, 'appretrut/inscription/inscription.html')
     