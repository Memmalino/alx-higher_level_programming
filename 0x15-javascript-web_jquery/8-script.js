 {
  let films = data.results;
  films.forEach(film => {
    $('<li>' + film.title + '</li>').appendTo('#list_movies');
  });
});