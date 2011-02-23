$(document).ready(function() {
  $('select.document_select_multiple').removeClass('document_select_multiple').parent().addClass('document_select_multiple js-enabled');
  
  $('.document_select_multiple .action.initiate_document_picker').each(function() {
    var document_select = $(this).closest('.document_select_multiple');
    var select = document_select.find('select');
    var selected_documents = document_select.find('.selected_documents');
    var document_picker = $('#fancybox-inner');
    var document_picker_url = document_select.find('.action.initiate_document_picker').attr('href');
    
    /* initiate document picker / fancybox */
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
        $('#fancybox-outer').addClass('document_select_multiple');
        $('#fancybox-inner').addClass('document_picker');
      },
      
      'onComplete': function() {
        /* add document to selection */
        document_picker.find('li').live('click', function (event) {
          var item = $(this);
          var selected_documents_ul = selected_documents.find('ul');
          var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
          select.children('option[value="' + photo_value + '"]').attr('selected', 'selected');
          item.addClass('selected');
          if (!$(selected_documents_ul).children('#' + item.attr('id')).length) {
            item.clone().appendTo(selected_documents_ul);
          }
          event.preventDefault();
          return false;
        });
        
        document_picker.find('.action.close').live('click', function(event) {
          $.fancybox.close();
        });
      },
      
      'onClosed': function() {
        document_picker.find('li').die('click');
      },
      
    });
    
    /* initiate document upload / fancybox */
    document_select.find('.action.initiate_document_upload').fancybox({
      'autoDimensions': false,
      'height': 504,
      'padding': 20,
      'scrolling': 'no',
      'showCloseButton': false,
      'width': 750,
      'overlayColor': '#000000',
      'overlayOpacity': '0.8',
      
      'onStart': function() {
        $('#fancybox-outer').addClass('document_select_multiple');
        $('#fancybox-inner').addClass('document_picker');
      },
      
      'onComplete': function() {
        /* add document to selection */
        document_picker.find('.action.close').live('click', function(event) {
          $.fancybox.close();
        });
      },
      
    });
    
    /* pagination */
    document_picker.find('a.action.paginate').live('click', function (event) {
      document_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
    
    /* filter */
    document_picker.find('.filter input[type="text"]').live('change', function () {
      var q = $(this).val();
      var form = $(this).closest('form');
      document_picker.load(form.attr('action') + '?q=' + q);
    });
    
    /* prevent parent form submission when pressing enter in filter field */
    document_picker.find('.filter input').live('keypress', function (event) {
      if(event.keyCode == 13) {
        $(this).change();
        event.preventDefault();
        return false;
      }
    });
    
    /* filter button */
    document_picker.find('.action.filter').live('click', function (event) {
      document_picker.find('.filter input[type="text"]').change();
      event.preventDefault();
      return false;
    });
    
    /* reset */
    document_picker.find('.action.reset').live('click', function (event) {
      document_picker.load(document_picker_url);
      event.preventDefault();
      return false;
    });
    
    /* upload */
    document_picker.find('.action.new').live('click', function (event) {
      document_picker.load($(this).attr('href'));
      event.preventDefault();
      return false;
    });
    
    // Upload form
    $('form[name="document_upload"]').live('submit', function(event) {
      $(this).ajaxSubmit({
        success: function(data) {
          document_picker.html(data);
          if (!(document_picker.find('form').length)) {
            item = document_picker.find('li');
            var document_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
            var document_name = item.find('img').attr('alt');
            select.append('<option value="' + document_value + '" selected="selected">' + document_name + '</option>')
            select.change();
            $.fancybox.close();
          }
        },
      });
      event.preventDefault();
      return false;
    });
    
  });
  
  /* remove document selection */
  $('.document_select_multiple .selected_documents .action.remove').live('click', function (event) {
    var item = $(this).closest('li');
    var document_select = item.closest('.document_select_multiple');
    var select = document_select.find('select');
    var photo_value = parseInt(item.attr('id').match(/.*-(\d+)/)[1]);
    select.children('option[value="' + photo_value + '"]').removeAttr('selected');
    item.fadeOut(function(){item.remove();});
    event.preventDefault();
    return false;
  });
  
  /* select change - load selected documents */
  $('.document_select_multiple select').change(function(){
    var select = $(this);
    var document_select = select.closest('.document_select_multiple');
    var selected_documents = document_select.find('.selected_documents');
    var document_picker_url = document_select.find('.action.initiate_document_picker').attr('href');
    if (select.val()) {
      var ids = select.val().toString();
      $.ajax({
        url: document_picker_url,
        data: {'ids': ids},
        success: function(data, textStatus, jqXHR) {
          selected_documents.html(data);
        },
      });
    }
    else {
      selected_documents.empty().append('<ul></ul>');
    }
  });
  
  $('.document_select_multiple select').change();
  
});
