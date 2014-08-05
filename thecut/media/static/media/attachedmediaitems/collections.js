define(['backbone', 'attachedmediaitems/models'], function(Backbone, models) {


    var AttachedMediaItemCollection = Backbone.Collection.extend({

        model: models.AttachedMediaItem

    });


    return {
        'AttachedMediaItemCollection': AttachedMediaItemCollection
    };


});
