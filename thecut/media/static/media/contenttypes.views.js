define(['backbone.marionette', 'contenttypes.collections'], function(Marionette, collections) {


    var ContentTypeItemView = Backbone.Marionette.ItemView.extend({

        tagName: 'li',

        events: {
            'click': 'onClick'
        },

        onClick: function(event) {alert(this.model.get('verbose_name'));},

        // TODO: We should find the template within the inline admin container
        template: 'script[type="text/template"][data-name="contenttype_detail"]'

    });


    var ContentTypeCollectionView = Backbone.Marionette.CollectionView.extend({

        childView: ContentTypeItemView,

        initialize: function() {
            this.collection = new collections.ContentTypeCollection([], {
                url: this.$el.attr('data-api-href')
            });
        }

    });


    return {

            'ContentTypeCollectionView': ContentTypeCollectionView

    };


});
