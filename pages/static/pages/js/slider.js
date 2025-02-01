document.addEventListener("DOMContentLoaded", function () {
    let index = 0;
    const slides = document.querySelectorAll(".slide");
    const totalSlides = slides.length;

    function showNextSlide() {
        slides[index].classList.remove("active"); // Cache l'ancienne slide
        index = (index + 1) % totalSlides; // Passe à la suivante
        slides[index].classList.add("active"); // Montre la nouvelle slide
    }

    setInterval(showNextSlide, 8000); // Change toutes les 5 secondes
});