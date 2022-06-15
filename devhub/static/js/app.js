// Initialise Bootstrap tooltips
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
const tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

// mobile nav
if ($(window).width() < 992) {
  $('.burger-button').click(function() {
    const sidebar = $('#sidebar');
    const burgerButton = $(this);
    const body = $('body');
  
    // add/remove active class to burger button
    if (burgerButton.hasClass('__active')) {
      burgerButton.removeClass('__active');
    } else {
      burgerButton.addClass('__active');
    }
  
    // add/remove active class to nav
    if (sidebar.hasClass('__active')) {
      sidebar.removeClass('__active');
      body.removeClass('__active');
    } else {
      sidebar.addClass('__active');
      body.addClass('__active');
    }
  });
}

// add/edit project form - show name of file to upload
$('#projectimage, #profileimage').change(function() {
  $('.filename').text(this.files[0].name);
  $('#filename').val(this.files[0].name);
});

// add/edit project form - custom checkboxes
$('.projecttags').each(function() {
  const currentInput = $(this);
  const currentContainer = currentInput.closest('.checkbox-container');

  currentInput.change(function() {
    if (currentInput.is(':checked')) {
      currentContainer.addClass('checked');
      currentInput.attr('name', 'checked');
    } else {
      currentContainer.removeClass('checked');
      currentInput.attr('name', '');
    }
  });
});

// animate flash messages
$(document).ready(function() {
  setTimeout(function() {
    $('.flashes').addClass('animateout');
  }, 2500);
});