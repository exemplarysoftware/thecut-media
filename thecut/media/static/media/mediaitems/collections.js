define(['djangorestframework', 'mediaitems/models'], function(djangorestframework, models) {


    var MediaItemCollectionMixin = {

        model: models.MediaItem,

        initialize: function(models, options) {
            if (options && options['url']) {
                this.url = options['url'];
            }
        }

    }


    var MediaItemCollection = Backbone.Collection.extend({

    });
    _.extend(MediaItemCollection.prototype, MediaItemCollectionMixin);


    var PageableMediaItemCollection = djangorestframework.PageableCollection.extend({

        state: {
            pageSize: 5
        }

    });
    _.extend(PageableMediaItemCollection.prototype, MediaItemCollectionMixin);


    return {
        'MediaItemCollection': MediaItemCollection,
        'PageableMediaItemCollection': PageableMediaItemCollection
    };


});
