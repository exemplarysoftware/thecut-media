$(document).ready(function() {
  
  $('form[name="image_upload"]').live('submit', function(event) {
    var form = $(this);
    
    $(this).ajaxSubmit({
      success: function(data) {
        form.html(data);
        if (!(new_form.find('form').length)) {
          item = form.find('li');
          var image = item.find('img');
          var image_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
          select.append('<option value="' + image_value + '">' + image.attr('alt') + '</option>')
          select.val(image_value);
          select.change();
          $.fancybox.close();
        }
      },
    });
    
    event.preventDefault();
    return false;
  });
  
});
