window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    const navbarImg = document.getElementById('navbar_fp');
    if (window.scrollY > 60 && !navbar.classList.contains("scroll")) {  
        navbar.classList.add('scroll'); 
        if(navbarImg){ 
            navbarImg.style.display='block';
        }
    } else if (window.scrollY <= 60) {  
        navbar.classList.remove('scroll');  
        if(navbarImg){ 
            navbarImg.style.display='none';
        }
    }
});
