#!/usr/bin/node
const toggleHeader = document.querySelector('#toggle_header');
toggleHeader.addEventListener('click', changeClass);
const header = document.querySelector('header');
function changeClass () {
  header.classList.toggle('green');
  header.classList.toggle('red');
}
