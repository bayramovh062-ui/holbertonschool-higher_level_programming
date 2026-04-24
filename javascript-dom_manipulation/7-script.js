#!/usr/bin/node
const ul = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(url)
  .then(response => response.json())
  .then((data) => {
    const results = data.results;
    for (let i = 0; i < results.length; i++) {
      const li = document.createElement('li');
      li.textContent = results[i].title;
      ul.appendChild(li);
    }
  });
