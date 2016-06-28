define(["require", "exports"], function (require, exports) {
    "use strict";
    var Conf = (function () {
        function Conf() {
        }
        Conf.prototype.get = function () {
            return {
                server: "http://localhost:10000/api/dev/"
            };
        };
        return Conf;
    }());
    exports.Conf = Conf;
    var Storage = (function () {
        function Storage() {
        }
        Storage.prototype.add = function (key, value) {
            localStorage.setItem(key, value);
        };
        Storage.prototype.load = function (key) {
            return localStorage.getItem(key);
        };
        return Storage;
    }());
    exports.Storage = Storage;
});
