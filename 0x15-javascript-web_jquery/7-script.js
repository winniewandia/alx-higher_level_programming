$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
  const name = data.name;
  $('#character').text(name);
});
