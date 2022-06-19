let slideIndex = 1;
showSlides(slideIndex);

let prev = document.getElementById ('slider-dot-control');
let next = document.getElementById ('slider-prev-next-control');



function currentSlide(n) {
  showSlides(slideIndex = n);
}


function showSlides(n) {
    let slides = document.getElementsByClassName("info");
    if (n > slides.length) {
      slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let slide of slides) {
        slide.style.display = "none";
    }
    slides[slideIndex - 1].style.display = "flex";
  }
 var timer = 0;
 makeTimer(); //Создаем интервал
 function makeTimer(){
    clearInterval(timer) //Очистим интервал, это позволит прервать его работу и отменить перелистывание
    timer = setInterval(function(){
      slideIndex++;
      showSlides(slideIndex);
    },5000);
  }
