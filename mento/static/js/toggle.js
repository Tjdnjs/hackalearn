let user = document.querySelector("a#us");

user.addEventListener('click', () => {
    const usermenu = document.querySelector('.usermenu');
    usermenu.classList.toggle('active')
})