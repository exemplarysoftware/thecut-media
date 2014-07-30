define(['backbone', 'attachedmediaitems/models'], function(Backbone, models) {


    var AttachedMediaItemCollection = Backbone.Collection.extend({

        initialize: function(options) {
            this.contenttypesCollection = options.contenttypesCollection
        },

        model: models.AttachedMediaItem

    });


    return {
        'AttachedMediaItemCollection': AttachedMediaItemCollection
    };


});
