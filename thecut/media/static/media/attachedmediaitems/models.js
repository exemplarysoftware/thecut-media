define(['log', 'backbone'], function (log, Backbone) {


    'use strict';


    var AttachedMediaItem = Backbone.Model.extend({

        defaults: {
            'order': 0
        },

        delete: function () {
            log(['Deleting attachment', this.toJSON()])
            // When deleting an attachment, either flag it for deletion (if
            // pre-existing), or just remove it from it's collection.
            if (this.has('delete')) {
                this.set('delete', true);
            } else if (this.collection) {
                this.collection.remove(this);
            }
            this.trigger('delete');
        }

    });


    return {
        'AttachedMediaItem': AttachedMediaItem
    };


});
