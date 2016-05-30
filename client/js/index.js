(function(){
  $( "#datapicker" ).datepicker();
  $(".filter-popup").click(function(){

    var left_input = $(this).position().left;
    console.log($(this).attr("id"));


    $("#search-result").css({"top":48, "display": "block", "left":left_input});
  });
})();
