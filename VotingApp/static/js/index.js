burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
navList = document.querySelector('.nav-list')
rightNav = document.querySelector('.rightnav')



burger.addEventListener('click', () =>{
    rightNav.classList.toggle('visibility-class-resp')
    navList.classList.toggle('visibility-class-resp')
    navbar.classList.toggle('height-nav-resp')
})