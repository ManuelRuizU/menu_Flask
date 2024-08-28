// modal.js
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('myModal');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const modalPhoto = document.getElementById('modal-photo');

    document.querySelectorAll('.btn-info').forEach(button => {
        button.addEventListener('click', function () {
            modalTitle.textContent = this.getAttribute('data-title');
            modalDescription.textContent = this.getAttribute('data-description');
            modalPhoto.src = this.getAttribute('data-photo');
        });
    });
});

