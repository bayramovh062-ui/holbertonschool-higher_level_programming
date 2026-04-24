#!/usr/bin/node
document.addEventListener('DOMContentLoader', () => {
  const helloElement = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  fetch(url)
    .then(response => response.json())
    .then((data) => {
      helloElement.textContent = data.hello;
    });
});
