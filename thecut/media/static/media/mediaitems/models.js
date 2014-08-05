define(['backbone'], function(Backbone) {


    var MediaItem = Backbone.Model.extend({

        defaults: {
            'attachment': null,
            'contenttype': null
        },

        initialize: function(attributes, options) {
            if (attributes['id'] && attributes['contenttype']) {
                this.url = attributes['contenttype'].get('objects') + attributes['id'] + '/';
            }
        }

    });


    return {
        'MediaItem': MediaItem
    };


});
