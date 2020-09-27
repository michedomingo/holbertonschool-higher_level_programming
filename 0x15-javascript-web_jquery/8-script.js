$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  data.results.forEach(function (film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
