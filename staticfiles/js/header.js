$(document).ready(function() {
    $('#logout-btn').on('click', function(e) {
      e.preventDefault();
      $.ajax({
        url: '/accounts/logout/',
        type: 'POST',
        headers: { // Change 'header' to 'headers'
          'X-CSRFToken': csrftoken
        },
        success: function(response) {
          if (response.success) { // Change 'if response.success()' to 'if (response.success)'
            $('#logged_in').hide();
          }
        }
      });
    });
  });


