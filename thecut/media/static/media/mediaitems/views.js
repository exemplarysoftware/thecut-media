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

        template: 'script[type="text/template"][data-name="mediaitem_list"]',

        ui: {
            'itemList': 'ol'
        }

    });


    var PaginatedMediaItemCollectionView = MediaItemCollectionView.extend({

        collectionEvents: {
            'add': 'render'
        },

        events: {
            'click @ui.pagination .previous': 'paginateNext',
            'click @ui.pagination .next': 'paginatePrevious'
        },

        initialize: function(options) {
            this.collection = new collections.PageableMediaItemCollection([], {
                url: options.collectionUrl
            });
        },

        paginatePrevious: function() {
            this.collection.getNextPage();
        },

        paginateNext: function() {
            this.collection.getPreviousPage();
        },

        serializeData: function() {
            data = PaginatedMediaItemCollectionView.__super__.serializeData.call(this);
            data['hasPreviousPage'] = this.collection.hasPreviousPage();
            data['hasNextPage'] = this.collection.hasNextPage();
            data['state'] = this.collection.state;
            return data;
        },

        template: 'script[type="text/template"][data-name="paginated_mediaitem_list"]',

        ui: _.extend({
            'pagination': '.pagination'
        }, MediaItemCollectionView.prototype.ui)

    });


    var MediaItemAttachmentsCollectionView = MediaItemCollectionView.extend({

        initialize: function(options) {
            collection = new collections.MediaItemCollection();

            _.each(options.attachments, function(attachment) {
                var mediaitem = attachment.getMediaItem();
                mediaitem.fetch({
                    success: function() {
                        this.collection.add(mediaitem);
                    }
                });
            });

            this.collection = collection;
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView,
        'PaginatedMediaItemCollectionView': PaginatedMediaItemCollectionView,
        'MediaItemAttachmentsCollectionView': MediaItemAttachmentsCollectionView
    };


});
