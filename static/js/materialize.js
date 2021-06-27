$(document).ready(function () {
    // Initialize sidenav
    $('.sidenav').sidenav();
    // Profile sidenav for desktop
    $('#slide-out').sidenav({edge: 'right'})
    // Initialize carousel
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
    // Initialize collapsible
    $('.collapsible').collapsible();
    // Initialize data picker
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    // Initialize select input form field
    $('select').formSelect();
});