define(['vent', 'backbone', 'attachedmediaitems/models'], function(vent, Backbone, models) {


    var AttachedMediaItemCollection = Backbone.Collection.extend({

        attach: function(mediaitem) {
            this.add({'object_id': mediaitem.get('id'),
                      'content_type': mediaitem.get('contenttype').get('id')});
        },

        initialize: function(options) {
            this.contenttypesCollection = options.contenttypesCollection
            vent.on('picker:mediaitem:selected', this.attach, this)
        },

        model: models.AttachedMediaItem

    });


    return {
        'AttachedMediaItemCollection': AttachedMediaItemCollection
    };


});
