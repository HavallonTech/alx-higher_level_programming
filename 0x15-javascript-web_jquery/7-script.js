$(function () {
    $.ajax({
        method: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(data){
            $('#character').text(data.name)
        },
        error: function(){
            console.error('Error fetching character data:', error);
        }
    });
});
