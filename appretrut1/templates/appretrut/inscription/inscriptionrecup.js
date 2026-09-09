


document.getElementById("inscriptionForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const fichierPhoto = document.getElementById("photo2").files;

    const utilisateur = {
        nom: document.getElementById("nom2").value,
        prenom: document.getElementById("prenom2").value,
        naissance: document.getElementById("date-naissance2").value,
        email: document.getElementById("email2").value,
        telephone: document.getElementById("telephone2").value,
        ville: document.getElementById("ville2").value,
        sexe: document.getElementById("sexe2").value,
        metier: document.getElementById("metier2").value,
        experience: document.getElementById("experiance2").value,
        niveau: document.getElementById("niveau2").value,
        nationalite: document.getElementById("nationalite2").value,
        domaine: document.getElementById("domaine2").value,
        password: document.getElementById("password2").value,
        competence: document.getElementById("competence2").value
    };

    if (fichierPhoto) {
        const reader = new FileReader();

        reader.onload = function() {
            utilisateur.photo = reader.result;

            localStorage.setItem(
                "utilisateur",
                JSON.stringify(utilisateur)
            );

           window.location.href = "../utilisateur/tabbord.html";
        };

        reader.readAsDataURL(fichierPhoto);

    } else {

        utilisateur.photo = "";

        localStorage.setItem(
            "utilisateur",
            JSON.stringify(utilisateur)
        );

          window.location.href = "../utilisateur/tabbord.html";
    }
});