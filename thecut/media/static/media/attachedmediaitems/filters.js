define([], function () {


    'use strict';


    var activeAttachmentsFilter = function (attachment) {
        return !(attachment.has('delete') && attachment.get('delete'));
    };


    return {
        'activeAttachmentsFilter': activeAttachmentsFilter
    };


});
