define(['backbone'], function (Backbone) {


    'use strict';


    var Tag = Backbone.Model.extend({

        defaults: {
            'is_selected': false
        },

        toggleSelected: function () {
            this.set('is_selected', !this.get('is_selected'));
        }

    });


    return {
        'Tag': Tag
    };


});
