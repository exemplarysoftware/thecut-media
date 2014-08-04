define(['backbone.marionette', 'mediaitems/collections', 'mediaitems/models'], function(Marionette, collections, models) {


    var MediaItemView = Marionette.ItemView.extend({

        tagName: 'li',

        modelEvents: {
            'change': 'render',
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_detail"]'

    });


    var MediaItemPickerView = MediaItemView.extend({

        triggers: {
            'click': 'select'
        },

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

        childEvents: {
            'render': 'childViewRendered',
            'select': 'childViewSelected'
        },

        childViewRendered: function(childView) {
            var attachments = this.options.attachmentsCollection.findWhere({
                'content_type': this.options.contenttype.get('id'),
                'object_id': childView.model.get('id')
            });
            if (attachments) {
                childView.$el.addClass('selected');
            }
        },

        childViewSelected: function(childView) {
            this.options.attachmentsCollection.addFromMediaItem(childView.model);
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
            this.collection.fetch();
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


    var MediaItemAttachmentsCollectionView = MediaItemCollectionView.extend({

        addMediaItemFromAttachment: function(attachment) {
            // Only add attachment if it matches the selected contenttype, is not flagged for deletion
            if (attachment.get('content_type') == this.collection.contenttype && !(attachment.has('delete') && attachment.get('delete'))) {
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
            this.collection = new collections.MediaItemAttachmentsCollection();
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
            // When deleting an attachment, either flag it for deletion (if
            // existing), or just remove it from the collection.
            var attachment = model.get('attachment');
            if (attachment.has('delete')) {
                attachment.set('delete', true);
            }
            else {
                attachment.collection.remove(attachment);
            }
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView,
        'PaginatedMediaItemCollectionView': PaginatedMediaItemCollectionView,
        'MediaItemAttachmentsCollectionView': MediaItemAttachmentsCollectionView
    };


});
