$(document).ready(function () {
    // Initialize sidenav
    $('.sidenav').sidenav({
        inDuration: 350,
    });

    // Profile sidenav for desktop
    $('#slide-out').sidenav({edge: 'right'});
    
    // Initialize carousel
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });

    $('.carousel').carousel({indicators: true});

    // Initialize collapsible
    $('.collapsible').collapsible();

    // Initialize data picker
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
        yearRange: 20,
        showClearBtn: true,
    });

    // Initialize select input form field
    $('select').formSelect();

    $('.tooltipped').tooltip();

    // Initialize chips
    $('.chips').chips();

    // Initialize tabs
    $('.tabs').tabs();

    // Initialize character counter 
    $('input[type="text"], textarea').characterCounter();
});