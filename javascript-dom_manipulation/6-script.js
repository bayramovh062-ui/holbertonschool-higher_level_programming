#!/usr/bin/node
const character = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
  .then(response => response.json())
  .then((data) => {
    character.textContent = data.name;
  });
