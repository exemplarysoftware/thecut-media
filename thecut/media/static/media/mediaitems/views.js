define(['backbone.marionette', 'mediaitems/collections'], function(Marionette, collections) {


    var MediaItemView = Marionette.ItemView.extend({

        tagName: 'li',

        modelEvents: {
            'change': 'render',
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_detail"]'

    });


    var MediaItemCollectionView = Marionette.CompositeView.extend({

        childView: MediaItemView,

        childViewContainer: 'ol',

        initialize: function(options) {
            this.collection = new collections.MediaItemCollection([], {
                url: options.collectionUrl
            });
        },

        template: 'script[type="text/template"][data-name="mediaitem_list"]'

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView
    };


});
