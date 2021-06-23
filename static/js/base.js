$(document).ready(function () {
    // Fullscreen overlay for service categories
    $(function () {
        $('.toggle-overlay').click(function () {
            $('aside').toggleClass('open');
        });
    });

    var profileSidenav = true;

    if (profileSidenav) {
        // Fix sidenav aligment
        $('.sidenav > li').css({
            marginLeft: '50px'
        });
        // Trigger profile sidenav
        $('.sidenav').sidenav({
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
    }
});