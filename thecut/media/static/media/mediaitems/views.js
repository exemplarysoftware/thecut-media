define(['vent', 'backbone.marionette', 'mediaitems/collections', 'mediaitems/models'], function(vent, Marionette, collections, models) {


    var MediaItemView = Marionette.ItemView.extend({

        tagName: 'li',

        modelEvents: {
            'change': 'render',
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_detail"]'

    });


    var MediaItemPickerView = MediaItemView.extend({

        events: {
            'click': 'select',
        },

        select: function() {
            vent.trigger('picker:mediaitem:selected', this.model);
        }

    });


    var MediaItemCollectionView = Marionette.CompositeView.extend({

        childView: MediaItemPickerView,

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
                // TODO
                model: models.MediaItem.extend({defaults: _.extend(models.MediaItem.prototype.defaults, {contenttype: options.contenttype})}),
                url: options.contenttype.get('objects')
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

        addMediaItemFromAttachment: function(attachment) {
            // Only add attachment if it matches the selected contenttype, and is not flagged for deletion
            if (attachment.get('content_type') == this.collection.contenttype && (!attachment.get('delete'))) {
                var mediaitem = attachment.getMediaItem();
                var collection = this.collection;
                mediaitem.fetch({
                    success: function() {
                        collection.add(mediaitem);
                    }
                });
            }
        },

        childView: MediaItemAttachmentView,

        initialize: function(options) {
            this.collection = new collections.MediaItemCollection();
            this.collection.contenttype = options.contenttype.get('id');
            options.attachmentsCollection.each(function(attachment) {
                this.addMediaItemFromAttachment(attachment)
            }, this);
            options.attachmentsCollection.on('add', this.addMediaItemFromAttachment, this);
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
