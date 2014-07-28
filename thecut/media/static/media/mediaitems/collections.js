define(['djangorestframework', 'mediaitems/models'], function(djangorestframework, models) {


    var MediaItemCollection = djangorestframework.PageableCollection.extend({

        model: models.MediaItem,

        initialize: function(models, options) {
            this.url = options['url'];
        },

        state: {
            pageSize: 5
        }

    });


    return {
        'MediaItemCollection': MediaItemCollection
    };


});
