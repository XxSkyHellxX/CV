var fotos = document.querySelectorAll('.dom');

function cambio(event){
    event.target.style.transform="scale(1.2)";
    event.target.style.color="rgb(229, 69, 11)";

}

function cambio2(event){
    event.target.style.transform="scale(1)";
    event.target.style.color="rgb(229, 69, 11)";
}

for (var i = 0; i < fotos.length; i++) {
    fotos[i].addEventListener('mouseover',cambio);
    fotos[i].addEventListener('mouseout',cambio2);
}

