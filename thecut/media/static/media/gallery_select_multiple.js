$(document).ready(function() {
  $('select.gallery_select_multiple').removeClass('gallery_select_multiple').parent().addClass('gallery_select_multiple js-enabled');
  
  $('.gallery_select_multiple .action.initiate_gallery_picker').each(function() {
    var gallery_select = $(this).closest('.gallery_select_multiple');
    var select = gallery_select.find('select');
    var selected_galleries = gallery_select.find('.selected_galleries');
    var gallery_picker = $('#fancybox-inner');
    var gallery_picker_url = gallery_select.find('.action.initiate_gallery_picker').attr('href');
    
    /* initiate gallery picker / fancybox */
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
        $('#fancybox-outer').addClass('gallery_select_multiple');
        $('#fancybox-inner').addClass('gallery_picker');
      },
      
      'onComplete': function() {
        /* add gallery to selection */
        gallery_picker.find('li').live('click', function (event) {
          var item = $(this);
          var selected_galleries_ul = selected_galleries.find('ul');
          var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
          select.children('option[value="' + photo_value + '"]').attr('selected', 'selected');
          item.addClass('selected');
          if (!$(selected_galleries_ul).children('#' + item.attr('id')).length) {
            item.clone().appendTo(selected_galleries_ul);
          }
          event.preventDefault();
          return false;
        });
        
        gallery_picker.find('.action.close').live('click', function(event) {
          $.fancybox.close();
        });
      },
      
      'onClosed': function() {
        gallery_picker.find('li').die('click');
      },
      
    });
    
    /* pagination */
    gallery_picker.find('a.action.paginate').live('click', function (event) {
      gallery_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
    
    /* filter */
    gallery_picker.find('.filter input[type="text"]').live('change', function () {
      var q = $(this).val();
      var form = $(this).closest('form');
      gallery_picker.load(form.attr('action') + '?q=' + q);
    });
    
    /* prevent parent form submission when pressing enter in filter field */
    gallery_picker.find('.filter input').live('keypress', function (event) {
      if(event.keyCode == 13) {
        $(this).change();
        event.preventDefault();
        return false;
      }
    });
    
    /* filter button */
    gallery_picker.find('.action.filter').live('click', function (event) {
      gallery_picker.find('.filter input[type="text"]').change();
      event.preventDefault();
      return false;
    });
    
    /* reset */
    gallery_picker.find('.action.reset').live('click', function (event) {
      gallery_picker.load(gallery_picker_url);
      event.preventDefault();
      return false;
    });
    
  });
  
  /* remove gallery selection */
  $('.gallery_select_multiple .selected_galleries .action.remove').live('click', function (event) {
    var item = $(this).closest('li');
    var gallery_select = item.closest('.gallery_select_multiple');
    var select = gallery_select.find('select');
    var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
    select.children('option[value="' + photo_value + '"]').removeAttr('selected');
    item.fadeOut(function(){item.remove();});
    event.preventDefault();
    return false;
  });
  
  /* select change - load selected galleries */
  $('.gallery_select_multiple select').change(function(){
    var select = $(this);
    var gallery_select = select.closest('.gallery_select_multiple');
    var selected_galleries = gallery_select.find('.selected_galleries');
    var gallery_picker_url = gallery_select.find('.action.initiate_gallery_picker').attr('href');
    if (select.val()) {
      var ids = select.val().toString();
      $.ajax({
        url: gallery_picker_url,
        data: {'ids': ids},
        success: function(data, textStatus, jqXHR) {
          selected_galleries.html(data);
        },
      });
    }
    else {
      selected_galleries.empty().append('<ul></ul>');
    }
  });
  
  $('.gallery_select_multiple select').change();
  
});
