function onLoadFile(event) {
    document.getElementById('id_specificData').innerHTML = event.target.result;
    //document.getElementByName('saveAndSendNow').disabled = false;
}

function loadAndParseFile(event) {
    var file = document.getElementById('fileButton').files[0];
    //var fileName = document.getElementById('fileButton').files[0].name;

    document.getElementById('fileSize').innerHTML = file.size + " B";

    var reader = new FileReader();
    reader.onload = onLoadFile;
    reader.readAsText(file);
}