define(['backbone'], function(Backbone) {


    var ContentType = Backbone.Model.extend({

        defaults: {
            'is_selected': false,
        },

        onSelectedChange: function() {
            if (this.get('is_selected')) {
                this.trigger('selected', this);
            }
        },

        initialize: function(options) {
            this.on('change:is_selected', this.onSelectedChange);
        },

    });


    return {
        'ContentType': ContentType
    };


});
