define(['vent', 'backbone.marionette', 'contenttypes/collections'], function(vent, Marionette, collections) {


    var ContentTypeItemView = Marionette.ItemView.extend({

        tagName: 'li',

        events: {
            'click': 'onClick'
        },

        modelEvents: {
            'change': 'render',
        },

        onClick: function(event) {
            this.model.set('is_selected', true);
        },

        onRender: function(event) {
            if(this.model.get('is_selected')) {
                this.$el.addClass('selected');
            }
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_detail"]'

    });


    var ContentTypeCollectionView = Marionette.CompositeView.extend({

        childSelected: function(selectedModel) {
            this.collection.each(function(model) {
                if (selectedModel != model && model.get('is_selected')) {
                    model.set('is_selected', false);
                }
            });
            vent.trigger('contenttype:selected', selectedModel);
            this.render();  // TODO: Don't know why this isn't happening automatically from the model's 'change' event
        },

        childView: ContentTypeItemView,

        childViewContainer: 'ol',

        collectionEvents: {
            'selected': 'childSelected'
        },

        initialize: function(options) {
            this.collection = new collections.ContentTypeCollection([], {
                url: options.collectionUrl
            });
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_list"]'

    });


    return {
        'ContentTypeCollectionView': ContentTypeCollectionView
    };


});
