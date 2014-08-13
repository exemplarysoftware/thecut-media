define(['backbone.marionette'], function (Marionette) {


    'use strict';



    var TagItemView = Marionette.ItemView.extend({

        events: {
            'click': 'toggleSelected'
        },

        modelEvents: {
            'change': 'render'
        },

        onRender: function () {
            if (this.model.get('is_selected')) {
                this.$el.addClass('selected');
            } else {
                this.$el.removeClass('selected');
            }
        },

        tagName: 'li',

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="tag_detail"]',

        toggleSelected: function () {
            this.model.toggleSelected();
        }

    });


    var TagCollectionView = Marionette.CollectionView.extend({

        childView: TagItemView,

        initialize: function () {
            TagCollectionView.__super__.initialize.call(this);
            this.bindUIElements();  // Bind UI elements to existing HTML
        }

    });

    return {
        'TagCollectionView': TagCollectionView
    };


});
