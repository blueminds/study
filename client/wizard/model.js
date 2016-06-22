define(["require", "exports"], function (require, exports) {
    "use strict";
    var Usuario = (function () {
        function Usuario() {
        }
        Usuario.prototype.getName = function () {
            return "jhon";
        };
        return Usuario;
    }());
    exports.Usuario = Usuario;
});
