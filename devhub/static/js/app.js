// Initialise Bootstrap tooltips
let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});

// mobile nav
if ($(window).width() < 992) {
  $('.burger-button').click(function() {
    let sidebar = $('#sidebar');
    let burgerButton = $(this);
    let body = $('body');
  
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
  })
}

// add/edit project form - show name of file to upload
$('#projectimage, #profileimage').change(function() {
  $('.filename').text(this.files[0].name);
  $('#filename').val(this.files[0].name);
})

// add/edit project form - custom checkboxes
$('.projecttags').each(function() {
  let currentInput = $(this);
  let currentContainer = currentInput.closest('.checkbox-container');

  currentInput.change(function() {
    if (currentInput.is(':checked')) {
      currentContainer.addClass('checked');
      currentInput.attr('name', 'checked');
    } else {
      currentContainer.removeClass('checked');
      currentInput.attr('name', '');
    }
  })
});

// limit the amount of checkboxes it is possible to select
let limit = 3;
$('.projecttags').change(function() {
  if ($('input[type=checkbox]:checked').length > limit) {
    $(this).prop('checked', false);
    $(this).closest('.checkbox-container').removeClass('checked');
  }
})