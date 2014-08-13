define(['djangorestframework', 'contenttypes/models'], function (djangorestframework, models) {


    'use strict';


    var ContentTypeCollection = djangorestframework.PageableCollection.extend({

        model: models.ContentType,

        initialize: function (models, options) {
            this.url = options.url;
        }

    });


    return {
        'ContentTypeCollection': ContentTypeCollection
    };


});
