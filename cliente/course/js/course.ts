
///<reference path="../../typings/typings/tsd.d.ts"/>

export class Course{
  constructor(){
    console.log("creating a course");
  }

  addTemplateHandlers(){
    $(".booking-course").click(function(){
      console.log("reservando curso");
    });
  }

  find(){
    return  new Promise(function(resolve, reject){

      $.get('/course/templates/cursos.html', function(templates) {
          // Fetch the <script /> block from the loaded external
          // template file which contains our greetings template.
          var template = $(templates).filter('#cursos-template').html();
          var rendered = Mustache.render(template, {"cursos": [{},{},{},{},{},{},{}]});
          resolve(rendered);

      });

    });
  }
}
