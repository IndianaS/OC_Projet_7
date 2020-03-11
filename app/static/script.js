
let form = document.querySelector("#user-text-form")

/** 
 * Div chatbox creation function.
*/
function createDiv(text, klass, parent) {
    let divElt = document.createElement("div");
    divElt.classList.add(klass);
    divElt.textContent = text;
    parent.appendChild(divElt);
    divElt.scrollIntoView();
    return divElt;
}

/** 
 * Url link creation function.
*/
function createLink(text, url, parent) {
    let aElt = document.createElement("a");
    aElt.href = url;
    aElt.textContent = text;
    parent.appendChild(aElt);
}

/** 
 * Google map creation function.
*/
function createMap(position, klass, parent) {
    let mapElt = document.createElement("div");
    mapElt.classList.add(klass);
    console.log(position);
    let map = new google.maps.Map(mapElt, {
        zoom: 6,
        center: position
    });

    var marker = new google.maps.Marker({
        position: position,
        map: map,
        title: "Voilà l'endroit demandé"
    });
    parent.appendChild(mapElt);
}

/** 
 * Call functions for display in the chatbox.
*/
form.addEventListener("submit", function (event) {
    event.preventDefault();
    fetch("/ajax", {
        method: "Post",
        body: new FormData(form)
    }).then(function (response) {
        return response.json()
    }).then(function (data) {
        console.log(data)
        let chatbox = document.querySelector("#chatbox")
        createDiv(data.question, "question", chatbox);
        createDiv(data.response, "answer", chatbox);
        createDiv(data.adress, "answer", chatbox);
        createMap(data.coords, "map", chatbox);
        let article = createDiv(data.article, "answer", chatbox);
        createLink(" En savoir plus", data.url, article);
    });
})

main();
