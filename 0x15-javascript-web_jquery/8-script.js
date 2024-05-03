$(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(all_data) {
            $.each(all_data.results, function (index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        }
    });
});
