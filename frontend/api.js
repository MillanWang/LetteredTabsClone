function convert() {
    var tabs = document.getElementById("tabs").value;
    var xhr = new XMLHttpRequest();
    var host = window.location.hostname;
    // Add port if running locally
    if (host === "localhost") {
        host = `${host}:5000`
    }

    xhr.open("POST", `http://${host}/conversion`, true);
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