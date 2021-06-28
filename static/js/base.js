$(document).ready(function () {
    // Fullscreen overlay for service categories
    $(function () {
        $('.toggle-overlay').click(function () {
            $('aside').toggleClass('open');
        });
    });
    
    var profileSidenav = true;

    // Trigger profile sidenav with mobile nav
    if (profileSidenav) {
        // Fix sidenav aligment
        $('#mobile-sidenav--main > li').css({
            marginLeft: '50px'
        });
        // Trigger profile sidenav
        $('#mobile-sidenav--main').sidenav({
            onOpenStart: function () {
                $('#profile-sidenav').css({
                    opacity: 1,
                    transform: 'translateX(0%)',
                    transition: 'opacity 0.3s ease'
                });
            },
            onCloseStart: function () {
                $('#profile-sidenav').css({
                    opacity: 0,
                    transform: 'translateX(-105%)'
                });
            }
        });
    };
});