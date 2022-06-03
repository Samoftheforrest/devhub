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

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()