$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  data.results.forEach(movie => {
    const movieTitle = movie.title;
    $('#list_movies').append('<li>' + movieTitle + '</li>');
  });
});
