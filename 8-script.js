// Wait for DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    });
});