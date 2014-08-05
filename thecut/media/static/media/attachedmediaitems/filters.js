define([], function() {


    var activeAttachmentsFilter = function(attachment) {
        return !(attachment.has('delete') && attachment.get('delete'))
    }


    return {
        'activeAttachmentsFilter': activeAttachmentsFilter
    };


});
