$(document).ready(function() {
  $('select.image_select_multiple').removeClass('image_select_multiple').parent().addClass('image_select_multiple js-enabled');
  
  $('.image_select_multiple .action.initiate_image_picker').each(function() {
    var image_select = $(this).closest('.image_select_multiple');
    var select = image_select.find('select');
    var selected_images = image_select.find('.selected_images');
    var image_picker = $('#fancybox-inner');
    var image_picker_url = image_select.find('.action.initiate_image_picker').attr('href');
    var image_upload_url = image_select.find('.action.initiate_image_upload').attr('href');
    
    /* initiate image picker / fancybox */
    $(this).fancybox({
      'autoDimensions': false,
      'height': 504,
      'padding': 20,
      'scrolling': 'no',
      'showCloseButton': false,
      'width': 750,
      'overlayColor': '#000000',
      'overlayOpacity': '0.8',
      
      'onStart': function() {
        $('#fancybox-outer').addClass('image_select_multiple');
        $('#fancybox-inner').addClass('image_picker');
      },
      
      'onComplete': function() {
        /* add image to selection */
        image_picker.find('li').live('click', function (event) {
          var item = $(this);
          var selected_images_ul = selected_images.find('ul');
          var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
          // select option, and place at end of list.
          select.children('option[value="' + photo_value + '"]').remove().appendTo(select).attr('selected', 'selected');
          item.addClass('selected');
          if (!$(selected_images_ul).children('#' + item.attr('id')).length) {
            if ($(selected_images_ul).children('li').length) {
              item.clone().appendTo(selected_images_ul);
              $('.image_order input').val(select.val());
            }
            else {
              // ensure sortable is bound to list
              select.change();
            }
          }
          event.preventDefault();
          return false;
        });
        
        image_picker.find('.action.close').live('click', function(event) {
          $.fancybox.close();
        });
      },
      
      'onClosed': function() {
        image_picker.find('li').die('click');
      },
      
    });
    
    /* initiate image upload / fancybox */
    image_select.find('.action.initiate_image_upload').fancybox({
      'autoDimensions': false,
      'height': 504,
      'padding': 20,
      'scrolling': 'no',
      'showCloseButton': false,
      'width': 750,
      'overlayColor': '#000000',
      'overlayOpacity': '0.8',
      
      'onStart': function() {
        $('#fancybox-outer').addClass('image_select_multiple');
        $('#fancybox-inner').addClass('image_picker');
      },
      
      'onComplete': function() {
        /* add image to selection */
        image_picker.find('.action.close').live('click', function(event) {
          $.fancybox.close();
        });
      },
      
    });
    
    /* pagination */
    image_picker.find('a.action.paginate').live('click', function (event) {
      image_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
    
    /* filter */
    image_picker.find('.filter input[type="text"]').live('change', function () {
      var q = $(this).val();
      var form = $(this).closest('form');
      image_picker.load(form.attr('action'), {'q': q});
    });
    
    /* prevent parent form submission when pressing enter in filter field */
    image_picker.find('.filter input').live('keypress', function (event) {
      if(event.keyCode == 13) {
        $(this).change();
        event.preventDefault();
        return false;
      }
    });
    
    /* filter button */
    image_picker.find('.action.filter').live('click', function (event) {
      image_picker.find('.filter input[type="text"]').change();
      event.preventDefault();
      return false;
    });
    
    /* reset */
    image_picker.find('.action.reset').live('click', function (event) {
      image_picker.load(image_picker_url);
      event.preventDefault();
      return false;
    });
    
    /* upload */
    image_picker.find('.action.new').live('click', function (event) {
      //alert('Not implemented.');
      image_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
  
    // Upload form
    $('form[name="image_upload"]').live('submit', function(event) {
      $(this).ajaxSubmit({
        success: function(data) {
          image_picker.html(data);
          if (!(image_picker.find('form').length)) {
            item = image_picker.find('li');
            var image_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
            var image_name = item.find('img').attr('alt');
            select.append('<option value="' + image_value + '" selected="selected">' + image_name + '</option>')
            //select.val(image_value);
            $('.image_order input').val(select.val());
            select.change();
            $.fancybox.close();
          }
        },
      });
      event.preventDefault();
      return false;
    });
    
  });
  
  /* remove image selection */
  $('.image_select_multiple .selected_images .action.remove').live('click', function (event) {
    var item = $(this).closest('li');
    var image_select = item.closest('.image_select_multiple');
    var select = image_select.find('select');
    var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
    select.children('option[value="' + photo_value + '"]').removeAttr('selected');
    item.fadeOut(function(){item.remove();});
    event.preventDefault();
    return false;
  });
  
  /* select change - load selected images */
  $('.image_select_multiple select').change(function(){
    var select = $(this);
    var image_select = select.closest('.image_select_multiple');
    var selected_images = image_select.find('.selected_images');
    var image_picker_url = image_select.find('.action.initiate_image_picker').attr('href');
    if (select.val()) {
      var ids = select.val().toString();
      selected_images.load(image_picker_url, {'ids': ids}, function() {
        selected_images.find('ul').sortable({
          cursor: 'move',
          
          update: function(event, ui) {
            // Update option order in select.
            var order = $(this).sortable('toArray');
            $.each(order.reverse(), function(index, item) {
              var photo_value = parseInt(item.match(/.*-(\d+)/)[1]);
              select.find('option[value="' + photo_value + '"]').remove().prependTo(select);
            });
            $('.image_order input').val(select.val());
          },
          
        });
      });
    }
    else {
      selected_images.empty().append('<ul></ul>');
    }
    
  });
  
  $('.image_select_multiple select').change();
  
});
