define(['backbone.marionette', 'mediaitems/collections', 'mediaitems/models', 'attachedmediaitems/filters', 'attachedmediaitems/models', 'tags/views'], function(Marionette, collections, models, filters, attachedmediaitemsModels, tagsViews) {


    var PaginationControlsView = Marionette.ItemView.extend({

        collectionEvents: {
            'add': 'render',
            'remove': 'render'
        },

        events: {
            'click @ui.previous': 'paginateNext',
            'click @ui.next': 'paginatePrevious',
        },

        paginatePrevious: function() {
            this.collection.getNextPage();
        },

        paginateNext: function() {
            this.collection.getPreviousPage();
        },

        serializeData: function() {
            var data = PaginationControlsView.__super__.serializeData.call(this);
            return _.extend(data, {
                'hasPreviousPage': this.collection.hasPreviousPage(),
                'hasNextPage': this.collection.hasNextPage(),
                'state': this.collection.state,
                'firstResultIndex': this.firstResultIndex(),
                'lastResultIndex': this.lastResultIndex()
            });
        },

        firstResultIndex: function() {
            // 1-based index for the first result in the current page.
            return (this.collection.state.pageSize * (this.collection.state.currentPage - 1)) + 1;
        },

        lastResultIndex: function() {
            // 1-based index for the last result in the current page.
            return this.firstResultIndex() + this.collection.length - 1;
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="pagination_controls"]',

        ui: {
            'previous': '.action.previous',
            'next': '.action.next'
        }

    });


    var FilterControlsView = Marionette.ItemView.extend({

        initialize: function(options) {
            FilterControlsView.__super__.initialize.call(this);
            this.bindUIElements();  // Bind UI elements to existing HTML

            this.tagCollectionView = new tagsViews.TagCollectionView({
                'collection': this.collection.tagsCollection,
                'el': this.ui.tags
            });

            this.collection.tagsCollection.on('change', this.change, this);

        },

        change: function(event) {
            var tags = _(this.collection.tagsCollection.where({'is_selected': true})).chain().pluck('attributes').pluck('name').value();
            this.collection.queryParams.tag = tags;
            this.collection.queryParams.q = this.ui.q.val();
            this.collection.getFirstPage({fetch: true});
        },

        events: {
          'keydown @ui.q': 'keydown',
          'keyup @ui.q': 'keypress',
          'click @ui.reset': 'reset'
        },

        keydown: function(event) {
            // Prevent enter from submitting the admin form
            if (event.keyCode == 10 || event.keyCode == 13) {
                event.preventDefault();
                this.change(event);
            }
        },

        keypress: _.debounce(function(event) {
            this.change(event);
        }, 800),

        reset: function(event) {
            this.collection.tagsCollection.reset();
            this.ui.q.val('');
            this.change(event);
        },

        ui: {
            'q': '[type="search"]',
            'reset': '.action.reset',
            'tags': '.tags'
        }

    });


    var MediaItemView = Marionette.ItemView.extend({

        deleteAttachment: function() {
            this.model.get('attachment').delete();
        },

        events: {
            'click @ui.remove': 'deleteAttachment'
        },

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

        tagName: 'li',

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_detail"]',

        triggers: {
            'click @ui.select': 'select'
        },

        ui: {
            'remove': '.action.remove',
            'select': '.action.select'
        }

    });


    var MediaItemCollectionView = Marionette.CompositeView.extend({

        childView: MediaItemView,

        childViewContainer: '@ui.itemList',

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="mediaitem_list"]',

        ui: {
            'itemList': 'ol'
        }

    });


    var PaginatedMediaItemCollectionView = MediaItemCollectionView.extend({

        associateAttachment: function(mediaitem, attachment) {
            attachment.on('delete', function() {mediaitem.set({'attachment': null});});
            mediaitem.set({'attachment': attachment});
        },

        collectionEvents: {
            'add': 'findAttachment'
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
                this.associateAttachment(childView.model, attachment);
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
            'click @ui.display .action.close': 'displayClose',
            'click @ui.display .action.open': 'displayOpen'
        },

        findAttachment: function(mediaitem) {
            // Find an active
            var activeAttachments = _.filter(this.options.attachmentsCollection.where({
                'content_type': mediaitem.get('contenttype').get('id'),
                'object_id': mediaitem.get('id')
            }), filters.activeAttachmentsFilter);
            var attachment = _.first(activeAttachments);

            if (attachment) {
                this.associateAttachment(mediaitem, attachment);
            }
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

        onShow: function() {
            this.paginationControlsView = new PaginationControlsView({
                'collection': this.collection,
                'el': this.ui.pagination
            });
            this.filterControlsView = new FilterControlsView({
                'collection': this.collection,
                'el': this.ui.filter
            });
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="paginated_mediaitem_list"]',

        ui: _.extend({
            'display': '.display.controls',
            'filter': '.filter.controls',
            'pagination': '.pagination.controls'
        }, MediaItemCollectionView.prototype.ui)

    });


    var MediaItemAttachmentsCollectionView = MediaItemCollectionView.extend({

        addMediaItemFromAttachment: function(attachment) {
            // Only add attachment if it matches the selected contenttype, is not flagged for deletion
            if (attachment.get('content_type') == this.options.contenttype.get('id') && filters.activeAttachmentsFilter(attachment)) {

                var mediaitem = new models.MediaItem({
                    'id': attachment.get('object_id'),
                    'contenttype': this.options.contenttype,
                    'attachment': attachment
                });

                attachment.on('delete', function() {mediaitem.collection.remove(mediaitem);});

                var collection = this.collection;
                mediaitem.fetch({
                    success: function() {
                        collection.add(mediaitem);
                    }
                });

            }
        },

        childView: MediaItemView,

        events: {
            'sortupdate': 'onSortUpdate'
        },

        initialize: function(options) {
            this.collection = new collections.MediaItemAttachmentsCollection();
            options.attachmentsCollection.each(function(attachment) {
                this.addMediaItemFromAttachment(attachment)
            }, this);

            options.attachmentsCollection.on('add', this.addMediaItemFromAttachment, this);
        },

        collectionEvents: {
            'change': 'render'
        },

        onRender: function() {
            this.ui.itemList.sortable();
        },

        onSortUpdate: function(event, ui) {
            this.children.each(function(childView) {
                childView.model.get('attachment').set('order', childView.$el.index());
            });
        }

    });


    return {
        'PaginatedMediaItemCollectionView': PaginatedMediaItemCollectionView,
        'MediaItemAttachmentsCollectionView': MediaItemAttachmentsCollectionView
    };


});
