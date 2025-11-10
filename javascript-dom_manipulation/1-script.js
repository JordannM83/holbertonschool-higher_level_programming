// JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id red_header
function changeColor () {
  document.getElementById('red_header').style.color = '#FF0000';
}

document.getElementById('red_header').addEventListener('click', changeColor);
