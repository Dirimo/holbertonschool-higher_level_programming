fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      const name = data.name;
      const item = document.getElementById('character');
      item.textContent = name;
    });