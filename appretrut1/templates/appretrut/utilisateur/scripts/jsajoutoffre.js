 









let offres = JSON.parse(localStorage.getItem("offres")) || [];

let liste = document.querySelector("#offre1");

offres.forEach((offre, index) => {

    let div = document.createElement("div");

    div.className = "col-lg-4 col-md-6";

    div.innerHTML = `
    
        <div class="card shadow h-100 offre-card">

            <div class="card-header text-center bg-white">

                <h5 class="entreprise">
                    ${offre.entreprise}
                </h5>

                <h6 class="poste">
                    ${offre.poste}
                </h6>

            </div>

            <div class="card-body">

                <div class="partie">
                    <h6 class="titre">Domaine</h6>
                    <p>${offre.domaine}</p>
                </div>

                <div class="partie">
                    <h6 class="titre">Description</h6>
                    <p>${offre.description}</p>
                </div>

            </div>

            <div class="card-body salaire">

                <h6 class="titre">Salaire</h6>

                <p>${offre.salaire} FCFA / mois</p>

            </div>

            <div class="card-body salaire">

                <h6 class="titre">Type de contrat</h6>

                <p>${offre.contract}</p>

            </div>

            <div class="card-footer bg-white">

                <button class="btn btn-primary w-100 mb-2">
                    POSTULER
                </button>

             

            </div>

        </div>

    `;

    liste.appendChild(div);

});

function supprimerOffre(index){

    let offres = JSON.parse(localStorage.getItem("offres")) || [];

    offres.splice(index,1);

    localStorage.setItem("offres",JSON.stringify(offres));

    location.reload();

}