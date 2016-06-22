///<reference path="../../typings/typings/tsd.d.ts"/>
define(["require", "exports"], function (require, exports) {
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
        Course.prototype.find = function () {
            return new Promise(function (resolve, reject) {
                $.get('/course/templates/cursos.html', function (templates) {
                    // Fetch the <script /> block from the loaded external
                    // template file which contains our greetings template.
                    var template = $(templates).filter('#cursos-template').html();
                    var rendered = Mustache.render(template, { "cursos": [{}, {}, {}, {}, {}, {}, {}] });
                    resolve(rendered);
                });
            });
        };
        return Course;
    }());
    exports.Course = Course;
});
