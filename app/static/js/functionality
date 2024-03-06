const menuToggle = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');
const dropdowns = document.querySelectorAll('.dropdown');

menuToggle.addEventListener('click', () => {
    menu.classList.toggle('open');
});

function toggleDropdown(element) {
    const dropdown = element.nextElementSibling;
    dropdowns.forEach(dropdown => dropdown.classList.remove('open'));
    element.parentElement.classList.toggle('open');
    dropdown.classList.toggle('open');
}