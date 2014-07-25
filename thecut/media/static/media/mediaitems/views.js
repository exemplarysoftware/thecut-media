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

        childViewContainer: '@ui.itemList',

        collectionEvents: {
            'reset': 'render'
        },

        events: {
            'click @ui.controls .previous': 'onClickNext',
            'click @ui.controls .next': 'onClickPrevious'
        },

        initialize: function(options) {
            this.collection = new collections.MediaItemCollection([], {
                url: options.collectionUrl
            });
        },

        template: 'script[type="text/template"][data-name="mediaitem_list"]',

        ui: {
            'itemList': 'ol',
            'controls': '.controls'
        },

        onClickPrevious: function() {
            this.collection.getNextPage();
        },

        onClickNext: function() {
            this.collection.getPreviousPage();
        },

        serializeData: function() {
            data = MediaItemCollectionView.__super__.serializeData.call(this);
            data['hasPreviousPage'] = this.collection.hasPreviousPage();
            data['hasNextPage'] = this.collection.hasNextPage();
            return data;
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView
    };


});
