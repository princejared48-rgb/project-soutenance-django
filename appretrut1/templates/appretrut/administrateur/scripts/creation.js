function recup(){

    let entreprise = document.querySelector("#entreprise").value;
    let poste = document.querySelector("#poste").value;
    let domaine = document.querySelector("#domaine").value;
    let description = document.querySelector("#description").value;
    let salaire = document.querySelector("#salaire").value;
    let contract = document.querySelector("#contract").value;

    let offre = {
        entreprise,
        poste,
        domaine,
        description,
        salaire,
        contract
    };

    let offres = JSON.parse(localStorage.getItem("offres")) || [];

    offres.push(offre);

    localStorage.setItem("offres", JSON.stringify(offres));

    location.href = "offre.html";
}