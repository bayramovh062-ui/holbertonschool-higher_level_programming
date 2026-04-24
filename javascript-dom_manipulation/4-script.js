#!/usr/bin/node
const addItemBtn = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');
addItemBtn.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
