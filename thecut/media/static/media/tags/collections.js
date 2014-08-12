define(['tags/models'], function(models) {


    var TagCollection = Backbone.Collection.extend({

        comparator: 'name',

        model: models.Tag

    });


    return {
        'TagCollection': TagCollection
    };


});
