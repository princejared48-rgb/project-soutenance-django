function getProfileData() {
    return {
        nom: document.getElementById("nom1").value,
        prenom: document.getElementById("prenom1").value,
        naissance: document.getElementById("naissance1").value,
        sexe: document.getElementById("sexe1").value,
        ville: document.getElementById("ville1").value,
        nationalite: document.getElementById("nationalite1").value,
        domaine: document.getElementById("domaine1").value,
        metier: document.getElementById("metier1").value,
        experience: document.getElementById("exp1").value,
        niveau: document.getElementById("niveau1").value,
        competence: document.getElementById("competences1").value
    };
}

function setProfileFields(data) {
    const values = data || {};

    const mappings = [
        ["nom", "nom"],
        ["prenom", "prenom"],
        ["naissance", "naissance"],
        ["sexe", "sexe"],
        ["ville", "ville"],
        ["nationalite", "nationalite"],
        ["domaine", "domaine"],
        ["metier", "metier"],
        ["experience", "exp"],
        ["niveau", "niveau"],
        ["competence", "competences"]
    ];

    mappings.forEach(([sourceKey, targetId]) => {
        const displayField = document.getElementById(targetId);
        if (displayField) {
            displayField.value = values[sourceKey] || "";
        }

        const editField = document.getElementById(targetId + "1");
        if (editField) {
            editField.value = values[sourceKey] || "";
        }
    });
}

function clearModalBackdrops() {
    document.querySelectorAll(".modal-backdrop").forEach((backdrop) => backdrop.remove());
    document.body.classList.remove("modal-open");
}

function save() {
    const profile = getProfileData();
    const user = JSON.parse(localStorage.getItem("utilisateur") || "{}");

    const nextUser = {
        ...user,
        ...profile,
        photo: user.photo || document.getElementById("photoProfil").src
    };

    localStorage.setItem("utilisateur", JSON.stringify(nextUser));
    setProfileFields(nextUser);

    const photoInput = document.getElementById("photo1");
    const photoProfil = document.getElementById("photoProfil");
    const photoGrande = document.getElementById("photoGrande");

    if (photoInput && photoInput.files && photoInput.files[0]) {
        const url = URL.createObjectURL(photoInput.files[0]);
        photoProfil.src = url;
        photoGrande.src = url;
        nextUser.photo = url;
        localStorage.setItem("utilisateur", JSON.stringify(nextUser));
    }

    const modalEl = document.getElementById("exampleModal");
    const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
    modal.hide();
    clearModalBackdrops();
}

function initializeProfileModal() {
    const modalEl = document.getElementById("exampleModal");
    if (!modalEl) return;

    const saveBtn = document.getElementById("saveProfileBtn");
    if (saveBtn) {
        saveBtn.addEventListener("click", save);
    }

    const triggerButtons = document.querySelectorAll('[data-bs-target="#exampleModal"]');
    triggerButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const user = JSON.parse(localStorage.getItem("utilisateur") || "{}");
            setProfileFields(user);
        });
    });

    modalEl.addEventListener("hidden.bs.modal", clearModalBackdrops);
}

function initializePhotoPreview() {
    const photoProfil = document.getElementById("photoProfil");
    const photoGrande = document.getElementById("photoGrande");

    if (photoProfil && photoGrande) {
        photoProfil.addEventListener("click", () => {
            photoGrande.src = photoProfil.src;
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const user = JSON.parse(localStorage.getItem("utilisateur") || "{}");
    setProfileFields(user);

    if (user.photo) {
        const photoProfil = document.getElementById("photoProfil");
        const photoGrande = document.getElementById("photoGrande");
        if (photoProfil) photoProfil.src = user.photo;
        if (photoGrande) photoGrande.src = user.photo;
    }

    initializeProfileModal();
    initializePhotoPreview();
});