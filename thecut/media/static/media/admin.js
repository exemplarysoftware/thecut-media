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
            //type: 'POST',
            success: function(data, textStatus, jqXHR) {
                inline_group.find('h2:first').after(data);
                inline_group.find('.media-content_type_list a').click(function(event) {
                    $(this).closest('.media-content_type_list').find('li').removeClass('active');
                    $(this).closest('li').addClass('active');
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
            if (!($(Element).closest('.inline-related').find('.delete input').is(':checked'))) {
              object_pk = $(Element).closest('fieldset').find('.form-row.object_id input').val();
              object_pks += object_pk;
            }
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
                //type: 'POST',
                success: function(data, textStatus, jqXHR) {
                    $(data).appendTo(object_list);
                    object_list.find('li').each(function(index, Element) {
                        var object_pk = parseInt($(this).attr('id').match(/(\d+)\-(\d+)/)[2]);
                        $(this).find('.action.remove').click(function() {
                            removeObject(content_type_pk, object_pk);
                        });
                    });
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    var list_item = $('<li />');
                    list_item.html('error').appendTo(object_list);
                },
            });
        });
        
        object_list.sortable({
            cursor: 'move',
            opacity: 0.6,
            update: function(event, ui) {
                // Update option order in select.
                var order = $(this).sortable('toArray');
                $.each(order, function(index, item) {
                    var object_pk = parseInt(item.match(/(\d+)\-(\d+)/)[2]);
                    orderObject(content_type_pk, object_pk, index);
                });
            },
        });
        
        object_list.appendTo(inline_group);
        
    };
    
    
    function getFormFieldsForObject(content_type_pk, object_pk) {
        var fields = new Array()
        inline_group.find('.inline-related .form-row.content_type select option[value="' + content_type_pk + '"][selected="selected"]').each(function(index, Element) {
            var inline_related = $(Element).closest('.inline-related');
            var input = inline_related.find('.form-row.object_id input[value="' + object_pk + '"]');
            if (input.length) {
                /* we have a match */
                fields.delete = inline_related.find('.delete input');
                fields.content_type = inline_related.find('.form-row.content_type select');
                fields.object_id = inline_related.find('.form-row.object_id input');
                fields.order = inline_related.find('.form-row.order input');
            }
        });
        return fields;        
    }
    
    
    function addObject(content_type_pk, object_pk, order) {
        var empty_inline_related = inline_group.find('.inline-related.empty-form');
        var total_forms = inline_group.find('#id_media-attachedmediaitem-parent_content_type-parent_object_id-TOTAL_FORMS');
        
        var inline_related = empty_inline_related.clone();        
        inline_related.removeClass('empty-form last-related');
        
        inline_related.attr('id', inline_related.attr('id').replace('-empty', '-' + total_forms.val()));
        inline_related.html(inline_related.html().replace(/__prefix__/g, total_forms.val()));
        total_forms.val(parseInt(total_forms.val()) + 1);
        
        inline_related.find('.form-row.content_type select').val(content_type_pk);
        inline_related.find('.form-row.object_id input').val(object_pk);
        inline_related.find('.form-row.order input').val(order);
        
        inline_related.insertBefore(empty_inline_related);
    }
    
    
    function orderObject(content_type_pk, object_pk, order) {
        var fields = getFormFieldsForObject(content_type_pk, object_pk);
        fields.order.val(order);
    }
    
    function removeObject(content_type_pk, object_pk) {
        var fields = getFormFieldsForObject(content_type_pk, object_pk);
        fields.delete.attr('checked', 'checked');
        hideObjectInList(content_type_pk, object_pk);
    }
    
    
    function hideObjectInList(content_type_pk, object_pk) {
        inline_group.find('.media-object_list li#' + content_type_pk + '-' + object_pk).fadeOut();
    }
    
    function showObjectInList(content_type_pk, object_pk) {
        inline_group.find('.media-object_list li#' + content_type_pk + '-' + object_pk).fadeIn();
    }
    
    
    inline_group.find('.inline-related .delete input').live('click', function() {
        var inline_related = $(this).closest('.inline-related');
        var content_type_pk = inline_related.find('.form-row.content_type select').val();
        var object_pk = inline_related.find('.form-row.object_id input').val();
        if ($(this).is(':checked')) {
            hideObjectInList(content_type_pk, object_pk);
        }
        else {
            showObjectInList(content_type_pk, object_pk);
        }
    });
    
    inline_group.addClass('media-attachedmediaitems');
    loadContentTypeList();
    
    $('#41-1').live('click', function() {addObject('34', '1', '5');});
});
