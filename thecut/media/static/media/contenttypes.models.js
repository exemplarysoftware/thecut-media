define(['backbone'], function(Backbone) {


    var ContentType = Backbone.Model.extend({

        defaults: {
            'is_selected': false,
        }

    });


    return {

        'ContentType': ContentType

    };


});
