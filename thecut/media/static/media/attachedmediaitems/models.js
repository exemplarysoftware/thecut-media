define(['backbone', 'mediaitems/models'], function(Backbone, mediaitemsModels) {


    var AttachedMediaItem = Backbone.Model.extend({

        getMediaItem: function() {
            var contenttype = this.collection.contenttypesCollection.get(this.get('content_type'));
            var url = contenttype.get('objects') + this.get('object_id') + '/';
            return new mediaitemsModels.MediaItem({url: url});
        }

    });


    return {
        'AttachedMediaItem': AttachedMediaItem
    };


});
