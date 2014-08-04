define(['backbone', 'attachedmediaitems/models'], function(Backbone, models) {


    var AttachedMediaItemCollection = Backbone.Collection.extend({

        addFromMediaItem: function(mediaitem) {
            this.add({'object_id': mediaitem.get('id'),
                      'content_type': mediaitem.get('contenttype').get('id')});
        },

        initialize: function(options) {
            this.contenttypesCollection = options.contenttypesCollection
        },

        model: models.AttachedMediaItem

    });


    return {
        'AttachedMediaItemCollection': AttachedMediaItemCollection
    };


});
