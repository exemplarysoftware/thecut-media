$(document).ready(function() {
  $('select.image_select_multiple').removeClass('image_select_multiple').parent().addClass('image_select_multiple js-enabled');
  
  /* image picker initiation */
  $('.image_select_multiple .action.initiate_image_picker').click(function (event) {
    var image_picker_url = $(this).attr('href')
    $(this).closest('.image_select_multiple').find('.image_picker').load(image_picker_url);
    event.preventDefault();
    return false;
  });
  
  /* image picker close */
  $('.image_select_multiple .image_picker .action.close').live('click', function (event) {
    $(this).closest('.image_picker').empty();
    event.preventDefault();
    return false;
  });
  
  /* add image selection */
  $('.image_select_multiple .image_picker li').live('click', function (event) {
    var item = $(this)//.closest('li');
    var image_select = item.closest('.image_select_multiple');
    var select = image_select.find('select');
    var selected_images_ul = image_select.find('.selected_images ul');
    var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
    select.children('option[value="' + photo_value + '"]').attr('selected', 'selected');
    item.addClass('selected');
    if (!$(selected_images_ul).children('#' + item.attr('id')).length) {
      item.clone().appendTo(selected_images_ul);
    }
    event.preventDefault();
    return false;
  });
  
  /* remove image selection */
  $('.image_select_multiple .selected_images .action.remove').live('click', function (event) {
    var item = $(this).closest('li');
    var image_select = item.closest('.image_select_multiple');
    var select = image_select.find('select');
    var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
    select.children('option[value="' + photo_value + '"]').removeAttr('selected');
    item.remove();
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
  
  /* pagination */
  $('.image_select_multiple .image_picker .action.paginate').live('click', function (event) {
    $(this).closest('.image_picker').load($(this).attr('href'));
    event.preventDefault();
    return false;
  });
  
  /* filter */
  $('.image_select_multiple .image_picker .filter input').live('change', function () {
    var image_select = $(this).closest('.image_select_multiple');
    var image_picker_url = image_select.find('.action.initiate_image_picker').attr('href');
    var q = $(this).val();
    image_select.find('.image_picker').load(image_picker_url, {'q': q});
  });
  
  /* prevent parent form submission when pressing enter in filter field */
  $('.image_select_multiple .image_picker .filter input').live('keypress', function (event) {
    if(event.keyCode == 13) {
      $(this).change();
      event.preventDefault();
      return false;
    }
  });
  
  /* filter button */
  $('.image_select_multiple .image_picker .action.filter').live('click', function (event) {
    var image_select = $(this).closest('.image_select_multiple');
    image_select.find('.image_picker .filter input').change();
    event.preventDefault();
    return false;
  });
  
  /* reset */
  $('.image_select_multiple .image_picker .action.reset').live('click', function (event) {
    var image_select = $(this).closest('.image_select_multiple');
    image_select.find('.action.initiate_image_picker').click();
    event.preventDefault();
    return false;
  });
  
});
