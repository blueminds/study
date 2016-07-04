var Curso = {
  find: function(category, level, country, max_price ){
    return  new Promise(function(resolve, reject){
      var server = "http://localhost:20000/api2/dev/";

      $.get(server+"cursos/categoria/"+category+"/nivel/"+level+"/pais/"+country+"/precio_max/"+max_price, function(resp){

        if(resp['code'] == "404"){
          reject(resp);
        }else{
          $.get('/course/templates/cursos.html', function(templates) {
            // Fetch the <script /> block from the loaded external
            // template file which contains our greetings template.
            var template = $(templates).filter('#cursos-template').html();
            var rendered = Mustache.render(template, {"cursos": resp });
            var response = [];
            response['rendered'] = rendered;
            response['cursos'] = resp;
            resolve(response);

          });
        }
      });
    });
  }
};
