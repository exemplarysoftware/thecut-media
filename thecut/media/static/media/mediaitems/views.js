define(['backbone.marionette', 'mediaitems/collections', 'mediaitems/models', 'attachedmediaitems/models'], function(Marionette, collections, models, attachedmediaitemsModels) {


    var MediaItemView = Marionette.ItemView.extend({

        tagName: 'li',

        modelEvents: {
            'change': 'render',
        },

        onRender: function() {
            if (this.model.get('attachment')) {
                this.$el.addClass('attached');
            } else {
                this.$el.removeClass('attached');
            }
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

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_list"]',

        ui: {
            'itemList': 'ol'
        }

    });


    var PaginatedMediaItemCollectionView = MediaItemCollectionView.extend({

        associateAttachment: function(mediaitem) {
            var attachment = this.options.attachmentsCollection.findWhere({
                'content_type': mediaitem.get('contenttype').get('id'),
                'object_id': mediaitem.get('id')
            });
            mediaitem.set({'attachment': attachment ? attachment : null});
            this.render();  // Needed to render pagination controls
        },

        collectionEvents: {
            'add': 'associateAttachment',
            'remove': 'associateAttachment'
        },

        childEvents: {
            'select': 'childViewSelected'
        },

        childViewSelected: function(childView) {
            if (!childView.model.get('attachment')) {
                var attachment = new attachedmediaitemsModels.AttachedMediaItem({
                    'object_id': childView.model.get('id'),
                    'content_type': childView.model.get('contenttype').get('id')
                });
                childView.model.set('attachment', attachment);
            }
            this.options.attachmentsCollection.add(childView.model.get('attachment'));
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

            var modelDefaults = _.extend(models.MediaItem.prototype.defaults, {contenttype: options.contenttype})
            this.collection = new collections.MediaItemPickerCollection([], {
                model: models.MediaItem.extend({'defaults': modelDefaults}),
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

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="paginated_mediaitem_list"]',

        ui: _.extend({
            'display': '.display.controls',
            'pagination': '.pagination.controls'
        }, MediaItemCollectionView.prototype.ui)

    });


    var MediaItemAttachmentsCollectionView = MediaItemCollectionView.extend({

        addMediaItemFromAttachment: function(attachment) {
            // Only add attachment if it matches the selected contenttype, is not flagged for deletion
            if (attachment.get('content_type') == this.options.contenttype.get('id') && !(attachment.has('delete') && attachment.get('delete'))) {

                var mediaitem = new models.MediaItem({
                    'id': attachment.get('object_id'),
                    'contenttype': this.options.contenttype,
                    'attachment': attachment
                });

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
            var attachment = model.get('attachment');
            attachment.delete();
        }

    });


    return {
        'MediaItemCollectionView': MediaItemCollectionView,
        'PaginatedMediaItemCollectionView': PaginatedMediaItemCollectionView,
        'MediaItemAttachmentsCollectionView': MediaItemAttachmentsCollectionView
    };


});
