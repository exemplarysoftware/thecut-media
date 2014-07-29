var attachedMediaItemRequire = requirejs.config({

    baseUrl: '/static/media',
    context: 'attachedmediaitem',

    paths: {
        'backbone': 'lib/backbone',
        'backbone.babysitter': 'lib/backbone.babysitter',
        'backbone.marionette': 'lib/backbone.marionette',
        'backbone.paginator': 'lib/backbone.paginator',
        'backbone.wreqr': 'lib/backbone.wreqr',
        'jquery': 'lib/jquery',
        'json2': 'lib/json2',
        'underscore': 'lib/underscore'
    },

    shim: {
        'backbone': {
            deps: ['json2', 'jquery', 'underscore'],
            exports: 'Backbone'
        },
        'backbone.babysitter': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.ChildViewContainer'
        },
        'backbone.marionette': {
            deps: ['json2', 'jquery', 'underscore', 'backbone',
                   'backbone.wreqr' ,'backbone.babysitter'],
            exports: 'Backbone.Marionette'
        },
        'backbone.paginator': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.PageableCollection'
        },
        'backbone.wreqr': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.Wreqr'
        },
        'jquery': {
            exports: 'jQuery',
            init: function () {return this.jQuery.noConflict();}
        },
        'json2': {
            exports: 'JSON'
        },
        'underscore': {
            exports: '_'
        }
    }

});


attachedMediaItemRequire(['jquery', 'vent', 'backbone.marionette', 'contenttypes/views', 'mediaitems/views', 'attachedmediaitems/views'], function(jQuery, vent, Marionette, contenttypesViews, mediaitemsViews, attachedmediaitemsViews) {


    jQuery(document).ready(function($) {

        var $manager = $('.attachedmediaitem.manager');  // We just say manager
        var application = new Marionette.Application();

        // Define regions
        application.addRegions({
            'manager': $manager,
            'contenttypes': $manager.find('.contenttypes'),
            'picker': $manager.find('.picker'),
            'attachments': $manager.find('.attachments'),

            // TODO
            'managementForm': $manager.find('.inline-group'),
            'test': $manager.find('#media-attachedmediaitem-parent_content_type-parent_object_id-0')
        });

        // Initialise contenttypes region
        application.addInitializer(function(options) {
            var contenttypeCollectionView = new contenttypesViews.ContentTypeCollectionView({
                'collectionUrl': this.getRegion('contenttypes').$el.attr('data-api-href')
            });
            this.getRegion('contenttypes').show(contenttypeCollectionView);
            contenttypeCollectionView.collection.fetch();
        });

        vent.on('contenttype:selected', function(contenttype) {
            var mediaItemCollectionView = new mediaitemsViews.MediaItemCollectionView({
                'collectionUrl': contenttype.get('objects')
            });
            application.getRegion('picker').show(mediaItemCollectionView);
            mediaItemCollectionView.collection.fetch();
        });

        // Start
        application.start();

        window.attachedmediaitemsViews = attachedmediaitemsViews;

        // Debug
        $manager.data('application', application);

    });


});
