const track = document.querySelector(".alumni-track");
const cards = document.querySelectorAll(".alumni-card");
const next = document.querySelector(".arrow.right");
const prev = document.querySelector(".arrow.left");

let index = 0;
const visibleCards = 3;
const cardWidth = 345;

/* move slider */

function updateSlider(){
track.style.transform = `translateX(-${index * cardWidth}px)`;
}

/* right */

next.onclick = ()=>{
index++;

if(index > cards.length - visibleCards){
index = 0;
}

updateSlider();
}

/* left */

prev.onclick = ()=>{
index--;

if(index < 0){
index = cards.length - visibleCards;
}

updateSlider();
}

/* auto slider */

setInterval(()=>{
index++;

if(index > cards.length - visibleCards){
index = 0;
}

updateSlider();

},4000);

const awardsTrack = document.querySelector(".awards-track");
const awardsSlides = document.querySelectorAll(".awards-slide");
const awardsNext = document.querySelector(".awards-right");
const awardsPrev = document.querySelector(".awards-left");
const awardsDots = document.querySelectorAll(".awards-dots .dot");

let awardsIndex = 0;

function updateAwardsSlider(){
    awardsTrack.style.transform = `translateX(-${awardsIndex * 100}%)`;

    awardsDots.forEach(dot => dot.classList.remove("active"));
    awardsDots[awardsIndex].classList.add("active");
}

awardsNext.addEventListener("click", () => {
    awardsIndex++;
    if(awardsIndex >= awardsSlides.length){
        awardsIndex = 0;
    }
    updateAwardsSlider();
});

awardsPrev.addEventListener("click", () => {
    awardsIndex--;
    if(awardsIndex < 0){
        awardsIndex = awardsSlides.length - 1;
    }
    updateAwardsSlider();
});

awardsDots.forEach(dot => {
    dot.addEventListener("click", () => {
        awardsIndex = Number(dot.dataset.index);
        updateAwardsSlider();
    });
});

setInterval(() => {
    awardsIndex++;
    if(awardsIndex >= awardsSlides.length){
        awardsIndex = 0;
    }
    updateAwardsSlider();
}, 5000);

document.addEventListener("DOMContentLoaded", function(){

const cards = document.querySelectorAll(".must-event-card");

const observer = new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity="1";
entry.target.style.transform="translateY(0)";
}

});

});

cards.forEach(card=>{

card.style.opacity="0";
card.style.transform="translateY(40px)";
card.style.transition="0.6s";

observer.observe(card);

});

});


    const socialLinks = document.querySelectorAll(".social-fixed a");

    socialLinks.forEach(link => {
        link.addEventListener("click", function () {
            // remove active from all
            socialLinks.forEach(l => l.classList.remove("active"));

            // add active to clicked
            this.classList.add("active");
        });
    });

    