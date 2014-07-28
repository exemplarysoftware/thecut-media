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
            'click @ui.pagination .previous': 'paginateNext',
            'click @ui.pagination .next': 'paginatePrevious'
        },

        initialize: function(options) {
            this.collection = new collections.MediaItemCollection([], {
                url: options.collectionUrl
            });
        },

        paginatePrevious: function() {
            this.collection.getNextPage();
        },

        paginateNext: function() {
            this.collection.getPreviousPage();
        },

        template: 'script[type="text/template"][data-name="mediaitem_list"]',

        ui: {
            'itemList': 'ol',
            'pagination': '.pagination'
        },

        serializeData: function() {
            data = MediaItemCollectionView.__super__.serializeData.call(this);
            data['hasPreviousPage'] = this.collection.hasPreviousPage();
            data['hasNextPage'] = this.collection.hasNextPage();
            data['state'] = this.collection.state;
            console.log(this.collection.state);
            return data;
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView
    };


});
