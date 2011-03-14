media.jQuery(document).ready(function($) {
    
    var prefix = '#media-attachedmediaitem-parent_content_type-parent_object_id';
    var inline_group = $(prefix + '-group');
    
    
    $('body').ajaxSend(function() {
        $(this).addClass('ajax-loading');
    }).ajaxComplete(function() {
        $(this).removeClass('ajax-loading');
    });
    
    
    function loadContentTypeList() {
        $.ajax({
            url: 'media/contenttype/',
            type: 'POST',
            success: function(data, textStatus, jqXHR) {
                inline_group.find('h2:first').after(data);
                inline_group.find('.media-content_type_list a').click(function(event) {
                    $(this).closest('.media-content_type_list').find('li').removeClass('active');
                    $(this).closest('li').addClass('active');
                    //alert(getObjectPksForContentType());
                    var content_type_pk = $(this).attr('rel');
                    loadObjectListForContentType(content_type_pk);
                    event.preventDefault();
                    return false;
                });
                inline_group.find('.media-content_type_list a').first().click();
            },
        });
    };
    
    
    function getObjectPksForContentType(content_type_pk) {
        var object_pks = new Array();
        inline_group.find('.inline-related .form-row.content_type select option[value="' + content_type_pk + '"][selected="selected"]').each(function(index, Element) {
            object_pk = $(Element).closest('fieldset').find('.form-row.object_id input').val();
            object_pks[index] = object_pk;
        });
        return object_pks;
    };
    
    
    function loadObjectListForContentType(content_type_pk) {
        inline_group.find('.media-object_list').slideUp().remove();
        var object_list = $('<ul class="media-object_list" />');
        var base_url = 'media/contenttype/' + content_type_pk + '/';
        var object_pks = getObjectPksForContentType(content_type_pk);
        $.each(object_pks, function(index, object_pk) {
            $.ajax({
                url: base_url + object_pk,
                type: 'POST',
                success: function(data, textStatus, jqXHR) {
                    var list_item = $('<li />');
                    list_item.html(data).appendTo(object_list);
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    var list_item = $('<li />');
                    list_item.html('error').appendTo(object_list);
                },
            });
        });
        object_list.appendTo(inline_group);
    };
    
    
    inline_group.addClass('media-attachedmediaitems');
    loadContentTypeList();
    
});
