#!/usr/bin/node
const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', addClass);
const header = document.querySelector('header');
function addClass () {
  header.classList.add('red');
}
