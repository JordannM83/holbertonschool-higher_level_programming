// JavaScript script that toggles the class of the header element when the user clicks on the tag id toggle_header
// JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header
document.getElementById('toggle_header').addEventListener('click', function () {
  document.querySelector('header').classList.toggle('red');
  document.querySelector('header').classList.toggle('green');
});
