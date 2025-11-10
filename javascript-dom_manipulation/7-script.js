// JavaScript script that fetches and lists the title for all movies from https://swapi-api.hbtn.io/api/films/?format=json
const listMoviesElement = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMoviesElement.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
