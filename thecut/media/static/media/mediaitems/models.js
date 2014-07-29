define(['backbone'], function(Backbone) {


    var MediaItem = Backbone.Model.extend({

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
