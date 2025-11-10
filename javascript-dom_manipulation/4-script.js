// JavaScript script that adds a li element to a list when the user clicks on the element with id add_item
document.getElementById('add_item').addEventListener('click', function () {
  const ul = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
