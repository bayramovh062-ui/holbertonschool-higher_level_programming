#!/usr/bin/node
const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', changeColor);
const header = document.querySelector('header');
function changeColor () {
  header.style.color = '#FF0000';
}
