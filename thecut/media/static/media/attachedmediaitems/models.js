define(['backbone'], function(Backbone) {


    var AttachedMediaItem = Backbone.Model.extend({

        defaults: {
            'order': 0
        },

        delete: function() {
            // When deleting an attachment, either flag it for deletion (if
            // pre-existing), or just remove it from it's collection.
            if (this.has('delete')) {
                this.set('delete', true);
            }
            else if (this.collection) {
                this.collection.remove(this);
            }
            this.trigger('delete');
        }

    });


    return {
        'AttachedMediaItem': AttachedMediaItem
    };


});
