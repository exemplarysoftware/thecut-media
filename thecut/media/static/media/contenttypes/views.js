define(['underscore', 'backbone.marionette'], function (_, Marionette) {


    'use strict';


    var ContentTypeItemView = Marionette.ItemView.extend({

        tagName: 'li',

        events: {
            'click': 'onClick'
        },

        modelEvents: {
            'change': 'render'
        },

        onClick: function () {
            this.model.set('is_selected', true);
        },

        onRender: function () {
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

        ajaxStart: function() {
            this.$el.addClass('loading');
        },

        ajaxStop: function() {
            this.$el.removeClass('loading');
        },

        contenttypeSelected: function (selectedModel) {
            // Ensure other models in the collection are 'unselected'.
            _.each(this.collection.where({'is_selected': true}), function (model) {
                if (selectedModel !== model) {
                    model.set('is_selected', false);
                }
            });
        },

        childView: ContentTypeItemView,

        childViewContainer: 'ol',

        collectionEvents: {
            'request': 'ajaxStart',
            'selected': 'contenttypeSelected',
            'sync': 'ajaxStop'
        },

        initialize: function () {
            var collection = this.collection;
            collection.fetch({
                'success': function () {
                    collection.first().set('is_selected', true);
                }
            });
        },

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_list"]'

    });


    return {
        'ContentTypeCollectionView': ContentTypeCollectionView
    };


});
