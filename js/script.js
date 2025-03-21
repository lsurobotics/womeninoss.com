window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    const navbarImg = document.getElementById('navbar_fp');
    if (window.scrollY > 60 && !navbar.classList.contains("scroll")) {
        navbar.classList.add('scroll');
        if (navbarImg) {
            navbarImg.style.display = 'block';
        }
    } else if (window.scrollY <= 60) {
        navbar.classList.remove('scroll');
        if (navbarImg) {
            navbarImg.style.display = 'none';
        }
    }

});
window.addEventListener('DOMContentLoaded', function () {
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.id = 'scroll-to-top';
    scrollToTopButton.innerHTML = '<svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"> <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/></svg>';
    document.body.appendChild(scrollToTopButton);
    window.addEventListener('scroll', function () {
        if (window.scrollY > 200) {

            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });
    scrollToTopButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

window.addEventListener('DOMContentLoaded', function () {
    const sectionTitleTag = 'h2'
    const subSectionTitleTag = 'h3'
    if (window.location.href.includes('/posts/')) {
        const navbar = document.querySelector('.navbar');
        const navbarHeight = navbar ? navbar.offsetHeight : 0;
        const sectionTitles = Array.from(document.querySelectorAll(sectionTitleTag)).filter(sectionTitle => !navbar.contains(sectionTitle));

        const selectContainer = document.createElement('div');
        selectContainer.id = 'contents-select';
        selectContainer.classList.add('dropdown');

        const button = document.createElement('button');
        button.textContent = 'Table of Contents';
        button.classList.add('dropdown-btn');
        selectContainer.appendChild(button);

        const select = document.createElement('ul');
        select.classList.add('dropdown-content');
        selectContainer.appendChild(select);

        sectionTitles.forEach((sectionTitle, index) => {
            if (!sectionTitle.id) {
                sectionTitle.id = `sectionTitle-${index}`;
            }
            const option = document.createElement('li');
            option.textContent = sectionTitle.textContent;
            option.dataset.targetId = sectionTitle.id;
            select.appendChild(option);

            let nextElement = sectionTitle.nextElementSibling;
            while (nextElement && nextElement.tagName !== sectionTitleTag.toUpperCase()) {
                if (nextElement.tagName === subSectionTitleTag.toUpperCase()) {
                    if (!nextElement.id) {
                        nextElement.id = `subSectionTitle-${index}-${Math.random().toString(36).substr(2, 5)}`;
                    }
                    const subOption = document.createElement('li');
                    subOption.textContent = nextElement.textContent;
                    subOption.dataset.targetId = nextElement.id;
                    subOption.style.paddingLeft = '50px'; // <- Aqui o padding
                    select.appendChild(subOption);
                }
                nextElement = nextElement.nextElementSibling;
            }
        });

        button.addEventListener('click', function (e) {
            e.stopPropagation();
            select.classList.toggle('show');
        });

        select.addEventListener('click', function (e) {
            if (e.target.tagName === 'LI') {
                const targetId = e.target.dataset.targetId;
                const target = document.getElementById(targetId);
                select.classList.remove('show');
                if (target) {
                    const elementPosition = target.getBoundingClientRect().top + window.pageYOffset;
                    const offsetPosition = elementPosition - navbarHeight - 30;
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });

        document.addEventListener('click', function (e) {
            if (!selectContainer.contains(e.target)) {
                select.classList.remove('show');
            }
        });

        const postTitle = document.querySelector('.post-title');
        if (postTitle) {
            postTitle.appendChild(selectContainer);
        }
    }
});