
let form = document.querySelector("#user-text-form")

function createDiv(text, klass, parent) {
    let divElt = document.createElement("div");
    divElt.classList.add(klass);
    divElt.textContent = text;
    parent.appendChild(divElt);
    divElt.scrollIntoView();
    return divElt;
}

function createDivLink(url, klass, parent) {
    let divElt = document.createElement("div");
    divElt.classList.add(klass);
    divElt.innerHTML = "Lien vers page Wikipedia".link(url);
    parent.appendChild(divElt);
    divElt.scrollIntoView();
}

function createLink(text, url, parent) {
    let aElt = document.createElement("a");
    aElt.href = url;
    aElt.textContent = text;
    parent.appendChild(aElt);
}

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
        createDiv(data.adress, "answer", chatbox);
        createMap(data.coords, "map", chatbox);
        let article = createDiv(data.article, "answer", chatbox);
        createLink(" En savoir plus", data.url, article);
    });
})

main();
