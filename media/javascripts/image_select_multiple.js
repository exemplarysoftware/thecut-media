$(document).ready(function() {
  $('select.image_select_multiple').removeClass('image_select_multiple').parent().addClass('image_select_multiple js-enabled');
  
  $('.image_select_multiple .action.initiate_image_picker').each(function() {
    var image_select = $(this).closest('.image_select_multiple');
    var select = image_select.find('select');
    var selected_images = image_select.find('.selected_images');
    var image_picker = $('#fancybox-inner');
    var image_picker_url = image_select.find('.action.initiate_image_picker').attr('href');
    
    /* initiate image picker / fancybox*/
    $(this).fancybox({
      'onComplete': function() {
        $.fancybox.resize();
        $('#fancybox-outer').addClass('image_select_multiple');
        $('#fancybox-inner').addClass('image_picker');
        
        /* add image to selection */
        image_picker.find('li').live('click', function (event) {
          var item = $(this);
          var selected_images_ul = selected_images.find('ul');
          var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
          select.children('option[value="' + photo_value + '"]').attr('selected', 'selected');
          item.addClass('selected');
          if (!$(selected_images_ul).children('#' + item.attr('id')).length) {
            item.clone().appendTo(selected_images_ul);
          }
          event.preventDefault();
          return false;
        });
      },
      
      'onClosed': function() {
        image_picker.find('li').die('click');
      },
      
    });
    
    /* pagination */
    image_picker.find('a.action.paginate').live('click', function (event) {
      image_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
    
    /* filter */
    image_picker.find('.filter input').live('change', function () {
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
    /*image_picker.find('.action.filter').live('click', function (event) {
      image_picker.find('.filter input').change();
      event.preventDefault();
      return false;
    });*/
    
    /* reset */
    image_picker.find('.action.reset').live('click', function (event) {
      image_picker.load(image_picker_url);
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
      selected_images.load(image_picker_url, {'ids': ids});
    }
    else {
      selected_images.empty().append('<ul></ul>');
    }
  });
  
  $('.image_select_multiple select').change();
  
});
