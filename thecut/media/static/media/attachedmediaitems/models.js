define(['backbone', 'mediaitems/models'], function(Backbone, mediaitemsModels) {


    var AttachedMediaItem = Backbone.Model.extend({

        getContentObject: function() {
            // TODO
            //var url = '../media/api/contenttypes/' + this.get('content_type') + '/objects/' + this.get('object_id') + '/';
            var url = this.collection.contenttypesCollection.url + this.get('content_type') + '/objects/' + this.get('object_id') + '/';
            return new mediaitemsModels.MediaItem({url: url});
        }

    });


    return {
        'AttachedMediaItem': AttachedMediaItem
    };


});
