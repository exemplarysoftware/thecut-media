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


attachedMediaItemRequire(['jquery', 'vent', 'backbone.marionette', 'contenttypes/views'], function(jQuery, vent, Marionette, contenttypeViews) {


    jQuery(document).ready(function($) {

        var $manager = $('.attachedmediaitem.manager');  // We just say manager
        var application = new Marionette.Application();

        // Define regions
        application.addRegions({
            'manager': $manager,
            'contenttypes': $manager.find('.contenttypes'),
            'picker': $manager.find('.picker'),
            'attachments': $manager.find('.attachments')
        });

        // Initialise contenttypes region
        application.addInitializer(function(options) {
            var contenttypeCollectionView = new contenttypeViews.ContentTypeCollectionView({
                'collectionUrl': this.getRegion('contenttypes').$el.attr('data-api-href')
            });
            this.getRegion('contenttypes').show(contenttypeCollectionView);
            contenttypeCollectionView.collection.fetch();
        });

        vent.on('contenttype:selected', function(contenttype) {alert('contenttype: ' + contenttype.get('verbose_name'))});

        // Start
        application.start();

        // Debug
        $manager.data('application', application);

    });


});
