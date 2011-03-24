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
    
    
    function getSeletedContentType() {
        return inline_group.find('.media-content_type_list li.active a').attr('rel');
    }
    
    
    function getObjectPksForContentType(content_type_pk) {
        var object_pks = new Array();
        inline_group.find('.inline-related .form-row.content_type select option[value="' + content_type_pk + '"]:selected').each(function(index, Element) {
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
        
        var selected_content_type = inline_group.find('.media-content_type_list li.active:first a');
        inline_group.find('.action.select').remove();
        var select = $('<a class="action select" rel="' + selected_content_type.attr('rel') + '" href="' + selected_content_type.attr('href') + '">Select ' + selected_content_type.text() + '</a>');
        object_list.after(select);
    };
    
    
    function getInlineRelatedForObject(content_type_pk, object_pk) {
        var result = false;
        inline_group.find('.inline-related .form-row.content_type select option[value="' + content_type_pk + '"]:selected').each(function(index, Element) {
            var inline_related = $(Element).closest('.inline-related');
            inline_related.find('.form-row.object_id input').each(function(index, input) {
            if ($(input).val() == object_pk) {
                /* we have a match */
                result = inline_related;
            }
            });
        });
        return result;
    }
    
    function getFormFieldsForObject(content_type_pk, object_pk) {
        var fields = new Array();
        var inline_related = getInlineRelatedForObject(content_type_pk, object_pk);
        fields.del = inline_related.find('.delete input');
        fields.content_type = inline_related.find('.form-row.content_type select');
        fields.object_id = inline_related.find('.form-row.object_id input');
        fields.order = inline_related.find('.form-row.order input');
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
        
        // Nasty hack - come back and fix this
        var empty_inline_related = inline_group.find('.inline-related.empty-form');
        fields.content_type.closest('.inline-related').insertBefore(empty_inline_related);
    }
    
    
    function removeObject(content_type_pk, object_pk) {
        var fields = getFormFieldsForObject(content_type_pk, object_pk);
        if (fields.del.length) {
            fields.del.attr('checked', 'checked');
        }
        else {
            getInlineRelatedForObject(content_type_pk, object_pk).remove();
            var total_forms = inline_group.find('#id_media-attachedmediaitem-parent_content_type-parent_object_id-TOTAL_FORMS');
            total_forms.val(parseInt(total_forms.val()) - 1);
        }
        hideObjectInList(content_type_pk, object_pk);
    }
    
    
    function hideObjectInList(content_type_pk, object_pk) {
        inline_group.find('.media-object_list li#' + content_type_pk + '-' + object_pk + ':visible:first').fadeOut();
    }
    
    function showObjectInList(content_type_pk, object_pk) {
        inline_group.find('.media-object_list li#' + content_type_pk + '-' + object_pk + ':hidden:first').fadeIn();
    }
    
    
    function markSelectedObjects() {
        var content_type_pk = getSeletedContentType();
        var object_pks = getObjectPksForContentType(content_type_pk);
        $.each(object_pks, function(index, object_pk) {
            $('.media-attachedmediaitems .media-picker .media-available_object_list').find('#' + content_type_pk + '-' + object_pk).addClass('selected');
        });
        $('.media-attachedmediaitems .media-picker .media-selected_object_list li').each(function(index, Element) {
            $('.media-attachedmediaitems .media-picker .media-available_object_list').find('#' + $(Element).attr('id')).addClass('selected');
        });
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
    
    $('.action.select').live('click', function(event) {
      var content_type_pk = $(this).attr('rel');
      
      $.ajax({
          url: $(this).attr('href'),
          //type: 'POST',
          success: function(data, textStatus, jqXHR) {
              var div = $('<div class="media-picker" />');
              div.html(data);
              div.dialog({
              dialogClass: 'media-attachedmediaitems',
                  draggable: false,
                  modal: true,
                  height: 540,
                  width: 960,
                  open: function(event, ui) {
                      markSelectedObjects();
                      $('.media-attachedmediaitems .media-picker .media-filter_objects form input').first().focus();
                  },
                  close: function(event, ui) {
                      $('.media-attachedmediaitems .media-picker').remove();
                  },
              });
          },
      });
      
      event.preventDefault();
      return false;
    });
    
    $('.media-attachedmediaitems .media-picker .media-filter_objects form').live('submit', function(event) {
        form = $(this);
        var available_objects = form.closest('.media-picker').find('.media-available_objects');
        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),
            success: function(data, textStatus, jqXHR) {
                var picker = $('<div />').html(data);
                form.html(picker.find('form').html());
                available_objects.html(picker.find('.media-available_objects').html());
                markSelectedObjects();
                form.find('input[type="checkbox"]:checked').closest('li').addClass('active');
                form.find('input').first().focus();
            },
        });
        event.preventDefault();
        return false;
    });
    
    $('.media-attachedmediaitems .media-picker .media-filter_objects form input[type="checkbox"]').live('click', function(event) {
        $(this).closest('form').submit();
    });
    
    $('.media-attachedmediaitems .media-picker .media-available_objects .pagination a').live('click', function(event) {
        var a = $(this);
        var available_objects = a.closest('.media-available_objects');
        $.ajax({
            url: a.attr('href'),
            //type: 'POST',
            success: function(data, textStatus, jqXHR) {
                var picker = $('<div />').html(data);
                available_objects.html(picker.find('.media-available_objects').html());
                markSelectedObjects();
            },
        });
        event.preventDefault();
        return false;
    });
    
    $('.media-attachedmediaitems .media-picker .media-available_object_list li .action.add').live('click', function() {
        $(this).closest('li').clone().appendTo('.media-attachedmediaitems .media-picker .media-selected_object_list');
        $(this).closest('li').addClass('selected');
    });
    
    $('.media-attachedmediaitems .media-picker .media-selected_object_list li .action.remove').live('click', function() {
        var li = $(this).closest('li');
        li.closest('.media-picker').find('.media-available_object_list li#' + li.attr('id')).removeClass('selected');
        li.remove();
    });
    
    $('.media-attachedmediaitems .media-picker .action.confirm').live('click', function() {
        $(this).closest('.media-picker').find('.media-selected_object_list li').each(function(index, Element) {
            var content_type_pk = parseInt($(Element).attr('id').match(/(\d+)\-(\d+)/)[1]);
            var object_pk = parseInt($(Element).attr('id').match(/(\d+)\-(\d+)/)[2]);
            var order = getObjectPksForContentType(content_type_pk).length
            addObject(content_type_pk, object_pk, order);
        });
        $(this).closest('.media-picker').dialog('close');
        inline_group.find('.media-content_type_list li.active a').click();
    });
    
    $('.media-attachedmediaitems .media-picker .action.cancel').live('click', function() {
        $(this).closest('.media-picker').dialog('close');
    });
    
    inline_group.addClass('media-attachedmediaitems');
    loadContentTypeList();
    
});
