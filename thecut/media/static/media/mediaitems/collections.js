define(['djangorestframework', 'mediaitems/models', 'tags/collections'], function(djangorestframework, models, tagsCollections) {


    var MediaItemAttachmentsCollection = Backbone.Collection.extend({

        comparator: function(model) {
            return model.get('attachment').get('order');
        },

        model: models.MediaItem

    });


    var MediaItemPickerCollection = djangorestframework.PageableCollection.extend({

        initialize: function(models, options) {
            this.url = options['url'];
            this.queryParams.tag = [];
            this.tagsCollection = new tagsCollections.TagCollection();
        },

        fetch: function(options) {
            // Ensure we always set ajax 'traditional' to true when fetching.
            options = options ? _.clone(options) : {};
            options.traditional = true;
            return MediaItemPickerCollection.__super__.fetch.call(this, options);
        },

        model: models.MediaItem,

        parse: function(data) {
            var results = MediaItemPickerCollection.__super__.parse.call(this, data);

            var tags = []
            _.each(data.tags, function(tag) {
                tags.push({'id': tag, 'name': tag});
            });
            this.tagsCollection.set(tags);

            return results;
        },

        state: {
            pageSize: 5
        }

    });


    return {
        'MediaItemAttachmentsCollection': MediaItemAttachmentsCollection,
        'MediaItemPickerCollection': MediaItemPickerCollection
    };


});
