var require = {

    baseUrl: '/static/media',

    paths: {
        'json2': 'lib/json2',
        'jquery': 'lib/jquery',
        'underscore': 'lib/underscore',
        'backbone': 'lib/backbone',
        'backbone.paginator': 'lib/backbone.paginator',
        'backbone.wreqr': 'lib/backbone.wreqr',
        'backbone.babysitter': 'lib/backbone.babysitter',
        'backbone.marionette': 'lib/backbone.marionette'
    },

    shim: {
        'json2': {
            exports: 'JSON'
        },
        'jquery': {
            exports: 'jQuery',
            //init: function () {return this.jQuery.noConflict();}
        },
        'underscore': {
            exports: '_'
        },
        'backbone': {
            deps: ['json2', 'jquery', 'underscore'],
            exports: 'Backbone'
        },
        'backbone.paginator': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.PageableCollection'
        },
        'backbone.wreqr': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.Wreqr'
        },
        'backbone.babysitter': {
            deps: ['json2', 'backbone'],
            exports: 'Backbone.ChildViewContainer'
        },
        'backbone.marionette': {
            deps: ['json2', 'jquery', 'underscore', 'backbone',
                   'backbone.wreqr' ,'backbone.babysitter'],
            exports: 'Backbone.Marionette'
        }
    }

};
