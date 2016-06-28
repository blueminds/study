define(["require", "exports", "../../course/js/course"], function (require, exports, course_1) {
    "use strict";
    var IndexInitialData = (function () {
        function IndexInitialData() {
        }
        IndexInitialData.prototype.loadFiltersData = function () {
            var coruse_types = [
                "Tipo 1",
                "Tipo 2",
                "Tipo 3",
                "Tipo 4",
                "Tipo 5",
            ];
            $("#type").autocomplete({
                source: coruse_types
            });
            var coruse_levels = [
                "Nivel 1",
                "Nivel 2",
                "Nivel 3",
                "Nivel 4",
            ];
            $("#level").autocomplete({
                source: coruse_levels
            });
            var coruse_cities = [
                "Ciudad 1",
                "Ciudad 2",
                "Ciudad 3",
                "Ciudad 4",
            ];
            $("#citie").autocomplete({
                source: coruse_cities
            });
            var coruse_max_price = [
                "Price 1",
                "Price 2",
                "Price 3",
                "Price 4",
            ];
            $("#max_price").autocomplete({
                source: coruse_max_price
            });
        };
        IndexInitialData.prototype.btn_search_handler = function () {
            $(".src-btn").click(function () {
                var c = new course_1.Course();
                var category = $("#category").val() == '' ? "null" : $("#category").val();
                var level = $("#level").val() == '' ? "null" : $("#level").val();
                var country = $("#country").val() == '' ? "null" : $("#country").val();
                var max_price = $("#max_price").val() == '' ? "0" : $("#max_price").val();
                var promise = c.find(category, level, country, max_price);
                promise.then(function (response) {
                    $("#intereactive-container").html(response['rendered']);
                    $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
                    IndexInitialData.cursos = response['cursos'];
                    c.addTemplateHandlers();
                    return false;
                }, function (err) { alert("no se encontraron cursos"); });
            });
        };
        IndexInitialData.prototype.init = function () {
            console.log("starting index");
            this.loadFiltersData();
            this.btn_search_handler();
        };
        IndexInitialData.cursos = [];
        return IndexInitialData;
    }());
    var index = new IndexInitialData();
    index.init();
});
