$(document).ready(function () {
  // globals
  $("#navigation").hide();

  // scroll
  $(window).scroll(function () {
    if ($(document).scrollTop() > 90) {
      $("#navigation").fadeIn(300);
    } else {
      $("#navigation").fadeOut();
    }
  });

  // hide nav
});

// image slider
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}
