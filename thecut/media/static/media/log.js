define([], function () {


    'use strict';


    var enableLogging = false;


    var log = function (input) {
        if (enableLogging && window.console) {
            window.console.log(input);
        }
    };


    return log;


});
