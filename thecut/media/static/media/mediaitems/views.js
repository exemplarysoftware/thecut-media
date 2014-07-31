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

        displayClose: function() {
            this.$el.removeClass('opened').addClass('closed');
        },

        displayOpen: function() {
            this.$el.removeClass('closed').addClass('opened');
        },

        events: {
            'click @ui.display .close': 'displayClose',
            'click @ui.display .open': 'displayOpen',
            'click @ui.pagination .previous': 'paginateNext',
            'click @ui.pagination .next': 'paginatePrevious'
        },

        initialize: function(options) {
            this.displayClose();
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
            'display': '.display.controls',
            'pagination': '.pagination.controls'
        }, MediaItemCollectionView.prototype.ui)

    });


    var MediaItemAttachmentView = MediaItemView.extend({

        events: {
            'click @ui.remove': 'removeFromCollection',
        },

        removeFromCollection: function() {
            this.model.collection.remove(this.model);
        },

        ui: {
            'remove': '.remove'
        }

    });


    var MediaItemAttachmentsCollectionView = MediaItemCollectionView.extend({

        childView: MediaItemAttachmentView,

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
        },

        collectionEvents: {
            'remove': 'deleteAttachment',
            'change': 'render'
        },

        deleteAttachment: function(model) {
            model.get('attachment').set('delete', true);
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView,
        'PaginatedMediaItemCollectionView': PaginatedMediaItemCollectionView,
        'MediaItemAttachmentsCollectionView': MediaItemAttachmentsCollectionView
    };


});
