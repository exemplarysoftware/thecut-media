define(['backbone'], function (Backbone) {


    'use strict';


    var MediaItem = Backbone.Model.extend({

        defaults: {
            'attachment': null,
            'contenttype': null
        },

        initialize: function (attributes) {
            if (attributes.id && attributes.contenttype) {
                this.url = attributes.contenttype.get('objects') + attributes.id + '/';
            }
        }

    });


    return {
        'MediaItem': MediaItem
    };


});
