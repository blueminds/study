
///<reference path="../../typings/typings/tsd.d.ts"/>
///<reference path="../../conf/conf.ts"/>

import {Conf} from  "../../conf/conf";


export class Course{
  
  constructor(){
    console.log("creating a course");
  }

  addTemplateHandlers(){
    $(".booking-course").click(function(){
      console.log("reservando curso");
    });
  }

  find(category:string, level:string, country:string, max_price:string ){
    return  new Promise(function(resolve, reject){
      var c = new Conf();


      $.get(c.get()['server']+"cursos/categoria/"+category+"/nivel/"+level+"/pais/"+country+"/precio_max/"+max_price, function(resp){

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
}
