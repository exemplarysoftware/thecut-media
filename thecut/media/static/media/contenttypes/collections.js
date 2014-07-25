define(['djangorestframework', 'contenttypes/models'], function(djangorestframework, models) {


    var ContentTypeCollection = djangorestframework.PageableCollection.extend({

        model: models.ContentType,

        initialize: function(models, options) {
            this.url = options['url'];
        },

    });


    return {
        'ContentTypeCollection': ContentTypeCollection
    };


});
