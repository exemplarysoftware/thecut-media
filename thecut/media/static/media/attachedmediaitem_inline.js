require(['jquery', 'contenttypes.views'], function(jQuery, views) {


    jQuery(document).ready(function($) {

        var $manager = $('.attachedmediaitem.manager');
        var $contenttypes = $manager.find('.contenttypes');

        window.view = new views.ContentTypeCollectionView({
            'el': $contenttypes
        });

        window.view.collection.fetch();

    });


});
