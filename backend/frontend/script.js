function upload() {
    let file = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("result");
        table.innerHTML = "";

        data.forEach(row => {
            table.innerHTML += `
            <tr>
                <td>${row.source}</td>
                <td>${row.destination}</td>
                <td>${row.bytes}</td>
                <td>${row.status}</td>
            </tr>`;
        });
    });
}
