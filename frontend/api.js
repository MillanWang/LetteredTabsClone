function convert() {
    var tabs = document.getElementById("tabs").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/conversion", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        input: tabs
    }));
    xhr.onload = function () {
        data = JSON.parse(xhr.response);
        var result = document.getElementById("result-area");
        result.innerHTML = data["data"];
    }
}