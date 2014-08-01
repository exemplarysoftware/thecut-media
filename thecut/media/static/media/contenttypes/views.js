define(['backbone.marionette', 'contenttypes/collections'], function(Marionette, collections) {


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

        onRender: function() {
            if (this.model.get('is_selected')) {
                this.$el.addClass('selected');
            } else {
                this.$el.removeClass('selected');
            }
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_detail"]'

    });


    var ContentTypeCollectionView = Marionette.CompositeView.extend({

        childSelected: function(selectedModel) {
            _.each(this.collection.where({'is_selected': true}), function(model) {
                if (selectedModel != model) {
                    model.set('is_selected', false);
                }
            });
        },

        childView: ContentTypeItemView,

        childViewContainer: 'ol',

        collectionEvents: {
            'selected': 'childSelected'
        },

        // TODO onFetch: function() {alert('fetch')},

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_list"]'

    });


    return {
        'ContentTypeCollectionView': ContentTypeCollectionView
    };


});
