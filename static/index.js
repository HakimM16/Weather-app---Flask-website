function changeColor() {
    fetch('/color')
        .then(response => response.json())
        .then(data => {
            document.body.style.backgroundColor = data.color;
        });
}
