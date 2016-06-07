(function(){

  $('html, body').animate({ scrollTop: $('#choose-title').offset().top }, { duration: 2000 });
  $( "#datapicker" ).datepicker();
  $('select').material_select();

  console.log(Storage.load("filter"));

  $.post( Server_settings['url'] + "services/curso/", Storage.load("filter")  ,  function( resp ) {
    console.log(resp);
    $.get('./templates/cursos.html', function(templates) {
        // Fetch the <script /> block from the loaded external
        // template file which contains our greetings template.
        var template = $(templates).filter('#cursos-template').html();
        var rendered = Mustache.render(template, {"cursos": resp});
        $("#cursos-container").html(rendered);

    });

  });

})();
