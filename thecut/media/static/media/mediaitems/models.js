define(['backbone'], function(Backbone) {


    var MediaItem = Backbone.Model.extend({

        defaults: {
            'attachment': null,
            'contenttype': null
        },

        initialize: function(attributes, options) {
            if (attributes['url']) {
                this.url = attributes['url'];
            }
        }

    });


    return {
        'MediaItem': MediaItem
    };


});
