function convert() {
    var tabs = document.getElementById("tabs").value;
    var xhr = new XMLHttpRequest();

    xhr.open("POST", `${window.location.href}conversion`, true);
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