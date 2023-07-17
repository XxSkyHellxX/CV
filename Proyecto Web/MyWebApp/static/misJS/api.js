let url = 'https://date.nager.at/Api/v2/NextPublicHolidays/CL';

fetch(url)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))
const mostrarData = (data) => {
    console.log(data)
    let body = ""
    for (var i = 0; i <data.length ; i++) {
        //${(data)[i].name}
        body += `
            <ol class="list-group rounded-0">    
                <li class="list-group-item " style="background-color: rgba(255, 255, 255, 0.826);">
                    <h6 class="text-start letrasPerfil mt-1"  >
                    ${(data)[i].localName} <span style="float:right">${(data)[i].date}</span> </h6>
                </li>
            </ol>    
                `
    }   
    document.getElementById('data').innerHTML = body
}

