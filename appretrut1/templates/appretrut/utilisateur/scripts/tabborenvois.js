const utilisateur = JSON.parse(localStorage.getItem("utilisateur"));

if (utilisateur) {

    document.getElementById("nom").value = utilisateur.nom;
    document.getElementById("prenom").value = utilisateur.prenom;
    document.getElementById("naissance").value = utilisateur.naissance;
    document.getElementById("sexe").value = utilisateur.sexe;
    document.getElementById("ville").value = utilisateur.ville;
    document.getElementById("nationalite").value = utilisateur.nationalite;

    document.getElementById("domaine").value = utilisateur.domaine;
    document.getElementById("metier").value = utilisateur.metier;
    document.getElementById("exp").value = utilisateur.experience;
    document.getElementById("niveau").value = utilisateur.niveau;

    document.getElementById("competences").value = utilisateur.competence;

    if (utilisateur.photo) {
        document.getElementById("photoProfil").src = utilisateur.photo;
        document.getElementById("photoGrande").src = utilisateur.photo;
    }
}