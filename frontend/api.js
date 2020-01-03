function convert() {
    var tabs = document.getElementById("tabs").value;
    var xhr = new XMLHttpRequest();
    var host = window.location.hostname;
    // Add port if running locally
    var url = '';
    if (host === "localhost") {
        url = 'http://localhost:5000/conversion';
    } else {
        url = 'https://lettered-tabs.herokuapp.com/conversion';
    }

    xhr.open("POST", url, true);
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