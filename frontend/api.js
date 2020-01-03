function convert() {
    var tabs = document.getElementById("tabs").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/conversion", false); //USED TO BE TRUE
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        input: tabs
    }));
    console.log(xhr);
}