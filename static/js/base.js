$(document).ready(function () {
    /* ======================================================
    Sidenav and fullscreen overlay
    ====================================================== */

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

    /* ======================================================
    Materialize switch
    ====================================================== */
    
    // Grab checkboxes
    var checkbox = $('input[type=checkbox]');
    var recruiterSwitch = $('#id_is_recruiter');
    var workingHereSwitch = $('#id_currently_working_here');
    var packageSwitch = $('#id_enable_all_packages');

    // Add materalize switch classes to checkbox
    checkbox.parent().parent().addClass('switch');
    checkbox.next().addClass('lever');
    recruiterSwitch.after("I'm a Recruiter");
    workingHereSwitch.after("I'm currently working here");
    packageSwitch.after('3 Packages');


    /* ======================================================
    Materialize chips
    ====================================================== */

    var chips = $('.chips-input');

    // Add materialize chips class to input field
    chips.parent().addClass('chips');
    chips.parent().removeClass('col s12');
    chips.removeClass('validate');

    // Add focus class
    chips.parent().on('click', function() {
        chips.parent().toggleClass('focus');
        chips.focus();
    });

    // Add chips
    function addChips() {
        $(chips).on('keypress', function(e) {
            let keycode = (event.keyCode ? event.keyCode : event.which);
            // Get text value from input field
            let value = chips.val();
            if(keycode == '13') {
                // Prevent string with only whitespace and/or special characters
                var regExp = /[a-zA-Z]/g;

                // Grab chips from html container to prevent duplicate chips from being added
                var current_container = $('.chips-container').text();

                if (regExp.test(value) && !current_container.includes(value)) {
                    container = $('.chips-container');
                    html_code = `<div class="chip">${value}<i class="close material-icons">close</i></div>`;
                    container.append(html_code);
                };
                // Refresh value of input field
                chips.val('');
            }
        });
    };
    addChips();

    // Add chips to hidden form
    function chipsToForm() {
        $('.next-btn').on('click', function() {
            // Grab chips from html container
            var container = $('.chips-container').text();
    
            // Add to array
            chipsString = container.toString();
            $.trim(chipsString);
            chips_arr = chipsString.split('close');
    
            // Remove empty string fields
            i = 0
            for (i=0; i < chips_arr.length; i++) {
                if (chips_arr[i] === '') {
                    chips_arr.splice(i, 1);
                };
            };
    
            // Update hidden input field value with the chips array
            $('.chips-hidden-input').val(chips_arr);
        });
    };
    chipsToForm();


    /* ======================================================
    Radio buttons - Expertise level
    ====================================================== */

    var expertiseRadios = $('input[name=expertise_level]');

    $(expertiseRadios).parent().addClass('btn btn-large')

    // Toggle checked for expertise level radio buttons
    $(expertiseRadios).on('click', function() {
        expertiseRadios.parent().css('backgroundColor', 'rgba(108, 92, 231, 75%)');
        expertiseRadios.attr('checked', false);
        $(this).attr('checked', true);
        $(this).parent().css('backgroundColor', '#0ACF83');
    });

    // Add additional text to the expertise level radio buttons

    $('input#id_expertise_level_0').parent().contents().filter(function() {
        return this.nodeType == 3; // Node.TEXT_NODE
    }).after('<span>I’m relatively new to this field</span>');

    $('input#id_expertise_level_1').parent().contents().filter(function() {
        return this.nodeType == 3; // Node.TEXT_NODE
    }).after('<span>I’ve had substantial experience in this field</span>');

    $('input#id_expertise_level_2').parent().contents().filter(function() {
        return this.nodeType == 3; // Node.TEXT_NODE
    }).after('<span>I’ve had comprehensive and detailed expertise in this field</span>');


    /* ======================================================
    Category Sections
    ====================================================== */

    // Update category id names
    $('#id_category_name_0').attr('id', 'DevCategories');
    $('#id_category_name_1').attr('id', 'CreativeCategories');
    $('#id_category_name_2').attr('id', 'WritingCategories');
    $('#id_category_name_3').attr('id', 'TranslationCategories');

    var categoryTypes = ['Dev', 'Creative', 'Writing', 'Translation']

    // Add id attributes to category list elements
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Categories`).parent().attr('id', `${categoryTypes[i]}Container`);
    };

    // Wrap heading text inside a header element
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Container`).contents().filter(function() {
            return this.nodeType == 3; // Node.TEXT_NODE
        }).wrap('<h6 class="center title smaller"></h6>');
    };

    // Add icons to radio list items
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Categories label`).before('<i class="fas fa-check"></i>');
    };

    // Add fullscreen overlay class and close button to each category
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Categories`).addClass('category-overlay');  
    };

    // Trigger category fullscreen overlay
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Container h6`).on('click', function() {
            $(this).siblings().addClass('active-category');
            // Trigger fullscreen overlay
            $(`#${categoryTypes[i]}Container .category-overlay`).css('visibility', 'visible').css('opacity', '1');
            // Change content container to mimic a fullscreen overlay
            $('.container.content').css('top', '0').css('height', '100%').css('overflow', 'hidden').css('border-radius', '0');
        
            // Show close button for fullscreen overlay
            $('.close-category').removeClass('hide');
        });
    };

    // Close overlay
    $('.close-category').on('click', function() {
        // Hide fullscreen overlay
        $('.active-category').css('visibility', 'hidden').css('opacity', '0');

        // Change content container back to default
        $('.container.content').css('top', '6%').css('height', '94%').css(
            'overflow', 'auto').css('border-top-left-radius', '40px').css('border-top-right-radius', '40px');
        
        // Hide close button for fullscreen overlay
        $('.close-category').addClass('hide');
    });

    /* ======================================================
    Radio buttons - Categories
    ====================================================== */

    var categoryRadios = $('input[name=category_name]');

    // Toggle checked for category radio buttons
    $(categoryRadios).on('click', function() {
        categoryRadios.parent().siblings('i').css('color', 'white');
        categoryRadios.attr('checked', false);
        $(this).attr('checked', true);
        $(this).parent().siblings('i').css('color', '#0ACF83');
    });


    /* ======================================================
    Toggle FAQ section
    ====================================================== */

    var showFAQ = $('#showFAQBtn');
    var cancelFAQ = $('#cancelFAQ'); 

    showFAQ.on('click', function() {
        $('#FAQSection').removeClass('hide');
    });

    cancelFAQ.on('click', function() {
        $('#FAQSection').addClass('hide');
    });


    /* ======================================================
    Toggle Package sections
    ====================================================== */

    var packageContainer = $('#ScopePricing');

    var showBasic = $('#basicBtn');
    var showStandard = $('#standardBtn');
    var showPremium = $('#premiumBtn');
    
    var basicPackage = $('#basicPackage');
    var standardPackage = $('#standardPackage');
    var premiumPackage = $('#premiumPackage');

    showBasic.on('click', function() {
        basicPackage.removeClass('hide');
        packageContainer.addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    showStandard.on('click', function() {
        standardPackage.removeClass('hide');
        packageContainer.addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    showPremium.on('click', function() {
        premiumPackage.removeClass('hide');
        packageContainer.addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    $('.cancel-package').on('click', function() {
        $(this).parent().parent().parent().addClass('hide');
        packageContainer.removeClass('hide');
        $('.next-btn').removeClass('hide');
        $('.prev-btn').removeClass('hide');
    });

    $('.save-package').on('click', function() {
        $(this).parent().parent().parent().addClass('hide');
        packageContainer.removeClass('hide');
        $('.next-btn').removeClass('hide');
        $('.prev-btn').removeClass('hide');
    });


    /* ======================================================
    Toggle required for packages
    ====================================================== */

    if ($('#id_enable_all_packages').is(':checked')) {
        var inputFields = $('.packages-smscreen').find('input');
        inputFields.prop('required', false);
    };
});