django.jQuery(document).ready(function($) {

    $('#content-main form').submit(function() {
        $('body').addClass('uploading');
    });

});
