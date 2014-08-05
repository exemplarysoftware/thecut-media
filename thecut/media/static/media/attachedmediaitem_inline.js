var attachedMediaItemRequire = requirejs.config({

    baseUrl: '/static/media',
    context: 'attachedmediaitem',

    paths: {
        'backbone': 'lib/backbone',
        'backbone.babysitter': 'lib/backbone.babysitter',
        'backbone.marionette': 'lib/backbone.marionette',
        'backbone.paginator': 'lib/backbone.paginator',
        'backbone.wreqr': 'lib/backbone.wreqr',
        'domReady': 'lib/domReady',
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


attachedMediaItemRequire(

    ['jquery', 'backbone.marionette', 'attachedmediaitems/collections',
     'attachedmediaitems/views', 'contenttypes/collections',
     'contenttypes/views', 'mediaitems/views', 'domReady!'],

    function(jQuery, Marionette, attachedmediaitemsCollections,
             attachedmediaitemsViews, contenttypesCollections,
             contenttypesViews, mediaitemsViews, document) {


    var $manager = $('.attachedmediaitem.manager');  // We just say manager
    var application = new Marionette.Application();


    // Define regions
    application.addRegions({
        'manager': $manager,
        'inlineGroup': $manager.find('.inline-group'),
        'contenttypes': $manager.find('.contenttypes'),
        'picker': $manager.find('.picker'),
        'attachments': $manager.find('.attachments')
    });


    // Initialise attachments collection
    application.addInitializer(function() {
        this.attachmentsCollection = new attachedmediaitemsCollections.AttachedMediaItemCollection();
    });


    // Initialise contentypes collection
    application.addInitializer(function() {

        this.contenttypesCollection = new contenttypesCollections.ContentTypeCollection([], {
            'url': this.getRegion('contenttypes').$el.attr('data-api-href')
        });

        // Show picker on contenttype selection
        this.contenttypesCollection.on('selected', function(contenttype) {
            var region = this.getRegion('picker');
            var view = new mediaitemsViews.PaginatedMediaItemCollectionView({
                'contenttype': contenttype,
                'attachmentsCollection': this.attachmentsCollection
            });
            region.show(view);
        }, this);

        // Show attachments on contenttype selection
        this.contenttypesCollection.on('selected', function(contenttype) {
            var region = this.getRegion('attachments');
            var view = new mediaitemsViews.MediaItemAttachmentsCollectionView({
                'contenttype': contenttype,
                'attachmentsCollection': this.attachmentsCollection
            });
            region.show(view);
        }, this);

    });


    // Initialise inlineGroup region
    application.addInitializer(function() {
        var region = this.getRegion('inlineGroup');
        var view = new attachedmediaitemsViews.AttachedMediaItemManagementView({
            'el': region.el,
            'collection': this.attachmentsCollection
        })
        region.attachView(view);
    });


    // Initialise contenttypes region
    application.addInitializer(function() {
        var region = this.getRegion('contenttypes');
        var view = new contenttypesViews.ContentTypeCollectionView({
            'collection': this.contenttypesCollection
        });
        region.show(view);
    });


    // Debug
    application.addInitializer(function() {
        this.getRegion('manager').$el.data('application', this);
    });

    // Start
    application.start();

});
