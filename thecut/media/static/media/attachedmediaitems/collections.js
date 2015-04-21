define(['backbone', 'attachedmediaitems/models'], function (Backbone, models) {


    'use strict';


    var AttachedMediaItemCollection = Backbone.Collection.extend({

        model: models.AttachedMediaItem

    });


    return {
        'AttachedMediaItemCollection': AttachedMediaItemCollection
    };


});
