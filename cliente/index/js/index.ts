///<reference path="../../typings/typings/tsd.d.ts"/>
///<reference path="../../course/js/course.ts"/>




import {Course} from "../../course/js/course";


class IndexInitialData{

  loadFiltersData(){




    var coruse_types = [
      "Tipo 1",
      "Tipo 2",
      "Tipo 3",
      "Tipo 4",
      "Tipo 5",

    ];

    $( "#type" ).autocomplete({
      source: coruse_types
    });

    var coruse_levels = [
      "Nivel 1",
      "Nivel 2",
      "Nivel 3",
      "Nivel 4",

    ];
    $( "#level" ).autocomplete({
      source: coruse_levels
    });


    var coruse_cities = [
      "Ciudad 1",
      "Ciudad 2",
      "Ciudad 3",
      "Ciudad 4",

    ];
    $( "#citie" ).autocomplete({
      source: coruse_cities
    });

    var coruse_max_price = [
      "Price 1",
      "Price 2",
      "Price 3",
      "Price 4",

    ];
    $( "#max_price" ).autocomplete({
      source: coruse_max_price
    });

  }

  btn_search_handler(){

    $(".src-btn").click(function(){
      $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });

      var c = new Course();
      var promise:any = c.find();

      promise.then(function(response){
        $("#intereactive-container").html(response);
        c.addTemplateHandlers();

      }, function(err){ console.log(err)});



      return false;
    });
  }

  init(){
    console.log("starting index");
    this.loadFiltersData();
    this.btn_search_handler();
  }
}

let index = new IndexInitialData();
index.init();
