define(['backbone', 'tags/models'], function (Backbone, models) {


    'use strict';


    var TagCollection = Backbone.Collection.extend({

        comparator: 'name',

        model: models.Tag

    });


    return {
        'TagCollection': TagCollection
    };


});
