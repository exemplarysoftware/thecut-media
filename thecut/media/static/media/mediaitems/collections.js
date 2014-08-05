define(['djangorestframework', 'mediaitems/models'], function(djangorestframework, models) {


    var MediaItemAttachmentsCollection = Backbone.Collection.extend({

        comparator: function(model) {
            return model.get('attachment').get('order');
        },

        model: models.MediaItem

    });


    var MediaItemPickerCollection = djangorestframework.PageableCollection.extend({

        model: models.MediaItem,

        initialize: function(models, options) {
            this.url = options['url'];
        },

        state: {
            pageSize: 5
        }

    });


    return {
        'MediaItemAttachmentsCollection': MediaItemAttachmentsCollection,
        'MediaItemPickerCollection': MediaItemPickerCollection
    };


});
