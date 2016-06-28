///<reference path="../../typings/typings/tsd.d.ts"/>
///<reference path="../../conf/conf.ts"/>
define(["require", "exports", "../../conf/conf"], function (require, exports, conf_1) {
    "use strict";
    var Course = (function () {
        function Course() {
            console.log("creating a course");
        }
        Course.prototype.addTemplateHandlers = function () {
            $(".booking-course").click(function () {
                console.log("reservando curso");
            });
        };
        Course.prototype.find = function (category, level, country, max_price) {
            return new Promise(function (resolve, reject) {
                var c = new conf_1.Conf();
                $.get(c.get()['server'] + "cursos/categoria/" + category + "/nivel/" + level + "/pais/" + country + "/precio_max/" + max_price, function (resp) {
                    if (resp['code'] == "404") {
                        reject(resp);
                    }
                    else {
                        $.get('/course/templates/cursos.html', function (templates) {
                            // Fetch the <script /> block from the loaded external
                            // template file which contains our greetings template.
                            var template = $(templates).filter('#cursos-template').html();
                            var rendered = Mustache.render(template, { "cursos": resp });
                            var response = [];
                            response['rendered'] = rendered;
                            response['cursos'] = resp;
                            resolve(response);
                        });
                    }
                });
            });
        };
        return Course;
    }());
    exports.Course = Course;
});
