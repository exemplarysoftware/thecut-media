define(['backbone'], function (Backbone) {


    'use strict';


    var ContentType = Backbone.Model.extend({

        defaults: {
            'is_selected': false
        },

        onSelectedChange: function () {
            if (this.get('is_selected')) {
                this.trigger('selected', this);
            }
        },

        initialize: function () {
            this.on('change:is_selected', this.onSelectedChange);
        }

    });


    return {
        'ContentType': ContentType
    };


});
