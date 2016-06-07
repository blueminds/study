(function(){
  $( "#datapicker" ).datepicker();

  function filterFormValidation( precio_min, precio_max ){
    console.log("returning validation");
    return true;
  }

  $(".btn-search").click(function(){

    if(filterFormValidation( $("#precio_minimo").val(),  $("#precio_maximo").val() )){
      var filter = {
        "precio_minimo": ( $("#precio_minimo").val() === '') ? 0 : $("#precio_minimo").val() ,
        "precio_maximo": ( $("#precio_maximo").val() === '') ? 0 : $("#precio_maximo").val()
      };

      Storage.add("filter", JSON.stringify(filter));


    }else{
      console.log("validation failed");
      return false;
    }

  });
  //Storage.addStorage("precio_minimo", JSON.stringify(json));

})();
