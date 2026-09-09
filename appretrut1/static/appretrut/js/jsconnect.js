document.addEventListener("DOMContentLoaded", function () {
    const formulaire = document.getElementById("connexionForm");

    if (!formulaire) return;

    formulaire.addEventListener("submit", function (event) {
        event.preventDefault();

        const passwordInput = document.getElementById("password");
        const password = passwordInput ? passwordInput.value.trim() : "";

        if (password === "1234") {
            window.location.href = urlAdmin;
        } else if (password === "5678") {
            window.location.href = urlUtilisateur;
        } else {
            alert("Code incorrect !");
        }
    });
});