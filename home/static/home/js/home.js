$(window).on('load', function() {
    /* ======================================================
    Detect when the carousel keyfrfame animation ends
    ====================================================== */

    /* Taken from the following source:
    'https://jonsuh.com/blog/detect-the-end-of-css-animations-and-transitions-with-javascript/' */

    function whichAnimationEvent() {
        var t,
        el = document.createElement("fakeelement");

        var animations = {
            animation: "animationend",
            OAnimation: "oAnimationEnd",
            MozAnimation: "animationend",
            WebkitAnimation: "webkitAnimationEnd",
        };

        for (t in animations) {
            if (el.style[t] !== undefined) {
                return animations[t];
            };
        };
    };

    var animationEvent = whichAnimationEvent();

    /* ======================================================
    Load carousel and images
    ====================================================== */

    $('#homeCarousel').carousel({
        fullWidth: true,
        indicators: true,
        duration: 600,
        onCycleTo : function($current_item, dragged) {
            stopAutoplay();
            startAutoplay();
            carouselFadeIn($current_item);
        }
    });

    function carouselFadeIn($current_item) {
        $('.carousel-content').removeClass('fade-out');
        $('.home-carousel-imgs').removeClass('fade-out');
        $($current_item).children('.carousel-content').addClass('fade-in');
        $($current_item).children('.carousel-content').css('opacity', '1');
        $($current_item).children('.home-carousel-imgs').addClass('slide-in');
        $($current_item).children('.home-carousel-imgs').one(animationEvent, function (event) {
            // Do something when the animation ends
            $(this).css('opacity', '1');
        });
    };

    function carouselFadeOut() {
        $('.carousel-content').removeClass('fade-in');
        $('.home-carousel-imgs').removeClass('fade-in');
        $('.home-carousel-imgs').removeClass('slide-in');
        $('.carousel-content').css('opacity', '0');
        $('.home-carousel-imgs').css('opacity', '0');
    };

    $('#homeCarousel .indicators').addClass('fade-in');
    $('#homeCarousel .indicators').css('opacity', '1');

    var autoplay
    function startAutoplay() {
        autoplay = setInterval(function() {
            $('#homeCarousel').carousel('next');
        }, 5000);
    };

    function stopAutoplay() {
        if (autoplay) {
            carouselFadeOut();
            clearInterval(autoplay);
        };
    };
});