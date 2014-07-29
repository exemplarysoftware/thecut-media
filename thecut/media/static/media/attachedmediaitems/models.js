define(['backbone', 'mediaitems/models'], function(Backbone, mediaitemsModels) {


    var AttachedMediaItem = Backbone.Model.extend({

        getContentObject: function() {
            var url = 'http://127.0.0.1:8000/django-admin/site/homepage/media/api/contenttypes/' + this.get('content_type') + '/objects/' + this.get('object_id') + '/';
            return new mediaitemsModels.MediaItem({url: url});
        }

    });


    return {
        'AttachedMediaItem': AttachedMediaItem
    };


});
