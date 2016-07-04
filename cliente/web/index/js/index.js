var Index = {

  loadFiltersData(){

    var coruse_types = [
      "Tipo 1",
      "Tipo 2",
      "Tipo 3",
      "Tipo 4",
      "Tipo 5",

    ];

    $( "#category" ).autocomplete({
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
    $( "#country" ).autocomplete({
      source: coruse_cities
    });

    var coruse_max_price = [
      "Price 1",
      "Price 2",
      "Price 3",
      "Price 4",

    ];
    $("#max_price" ).autocomplete({
      soure: coruse_max_price
    });

  },


  btn_search_handler: function(){
    $(".src-btn").click(function(){
      console.log("ok");
      var category = $("#category").val() == '' ? "null" :  $("#category").val();
      var level = $("#level").val() == '' ? "null" :  $("#level").val();
      var country = $("#country").val() == '' ? "null" :  $("#country").val();
      var max_price = $("#max_price").val() == '' ? "0" :  $("#max_price").val();

      var promise = Curso.find(category, level, country, max_price);

      promise.then(function(response){
        $("#intereactive-container").html(response['rendered']);
        $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
        console.log(response['cursos']);        
        return false;

      }, function(err){ alert("no se encontraron cursos")});

      return false;
    });
  }
}

Index.loadFiltersData();
Index.btn_search_handler();
