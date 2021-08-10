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
        $('#sidenav-main > li').css({
            marginLeft: '50px'
        });
        // Trigger profile sidenav
        $('#sidenav-main').sidenav({
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
    Remove placeholders and label active class from 
    log in and sign up form input fields
    ====================================================== */

    $(function(){
        var fields = $("#signup_form").find('input');
        var labels = $("#signup_form").find('label');
        $(fields).removeAttr('placeholder');
        $(labels).removeClass('active');
    });

    /* ======================================================
    Add 'filled in' class to Log in checkbox 
    ====================================================== */

    $('#id_remember').addClass('filled-in');
    $('#id_remember').siblings('span').addClass('checkbox-label');


    /* ======================================================
    Add 'text-field' class to all textarea form inputs 
    ====================================================== */
    
    $('textarea').parent().addClass('text-field');


    /* ======================================================
    Hide all hidden input types
    ====================================================== */

    $('.input-field input[type="hidden"]').parent().css('display', 'none');


    $('input').each(function() {
        if ($(this).length && $(this).val().length) {
            $(this).siblings('label').addClass('force-active');
        };
    });
    
    /* ======================================================
    Add character count to input fields
    ====================================================== */

    allInputs = $('.input-field').find('input[type="text"], textarea');

    for (i=0; i < allInputs.length; i++) {
        if ($(allInputs[i]).attr('maxlength')) {
            var maxlength = $(allInputs[i]).attr('maxlength');
            $(allInputs[i]).attr('data-length', maxlength);
        };
    };

    // Remove character counter from select fields
    $('.select-wrapper').children('.character-counter').remove();

    /* ======================================================
    Materialize switch
    ====================================================== */

    // Grab checkboxes
    var checkbox = $('input[type=checkbox]');
    var recruiterSwitch = $('#id_is_recruiter');
    var workingHereSwitch = $('#id_currently_working_here');
    var packageSwitch = $('#id_enable_all_packages');
    var clientRequirementsSwitch = $('#id_include_client_requirements');
    var requirementSameSwitch = $('#id_requirements_same_for_all');
    var shippingRequiredSwitch = $('#id_shipping_required');

    // Add materalize switch classes to checkbox
    if (checkbox.attr('id') !== 'id_remember') {
        // Ignore Sign up form checkbox
        checkbox.parent().parent().addClass('switch');
        checkbox.next().addClass('lever');
    }
    recruiterSwitch.after("I'm a Recruiter");
    workingHereSwitch.after("I'm currently working here");
    packageSwitch.after('enable 3 packages');
    clientRequirementsSwitch.after('Include client requirements');
    requirementSameSwitch.after('Same requirements for all packages');
    shippingRequiredSwitch.after('Product Shipping required');



    /* ======================================================
    Materialize chips
    ====================================================== */

    /* =======================================
    Hide and show current tags container
    depending on whether or not a 
    user has added any tags
    ======================================= */

    function isChipsContainerEmpty() {
        if ($('.chips-container').is(':empty')) {
            $('.current-tags').fadeOut(100);
        } else {
            $('.current-tags').fadeIn(100);
        };
    };
    isChipsContainerEmpty();


    /* =======================================
    Add functionality to chips
    ======================================= */

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
            if (keycode == '13') {
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

                isChipsContainerEmpty();
            }
        });
    };
    addChips();


    // Trigger isChipsContainerEmpty function on delete chip
    $('.chips-container').on('click', '.chip .close', function() {
        setTimeout(() => {
            isChipsContainerEmpty();
        }, 100);
    });

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

    // Hides subcategory options
    $('#id_category').removeClass('radio-btn')
    $('.subcategory-selection .radio-btn').addClass('hide');

    //  Add and remove radio, category-overlay and hide classes to category radios

    $('#id_dev_categories').removeClass('radio-btn');
    $('#id_dev_categories').addClass('category-overlay');
    $('#id_dev_categories .radio-btn').removeClass('hide');

    $('#id_creative_categories').removeClass('radio-btn');
    $('#id_creative_categories').addClass('category-overlay');
    $('#id_creative_categories .radio-btn').removeClass('hide');

    $('#id_writing_categories').removeClass('radio-btn');
    $('#id_writing_categories').addClass('category-overlay');
    $('#id_writing_categories .radio-btn').removeClass('hide');

    $('#id_translation_categories').removeClass('radio-btn');
    $('#id_translation_categories').addClass('category-overlay');
    $('#id_translation_categories .radio-btn').removeClass('hide');

    // Wrap category list items in a category box div
    $('#id_category li').wrapInner('<div class="category-box"></div>');
    $('.category-overlay li').wrapInner('<div class="category-box"></div>');

    // Add materialize rows and collumns to make the radios more responsive
    $('.category-overlay').wrapInner('<div class="row"></div>');
    $('.category-overlay li').addClass(' col s6 m4');
    
    // Make other category radios not required to fix form validation error
    $('#ServiceCategory .radio-btn').prop('required', false);

    // Subcategory fullscreen overlay
            
    $('.subcategory-selection .radio-btn').addClass('category-overlay');

    var categoryNames = [
        'dev', 'creative',
        'writing', 'translation'
    ];

    // Update category id names
    $('#id_category_0').attr('id', 'dev_category');
    $('#id_category_1').attr('id', 'creative_category');
    $('#id_category_2').attr('id', 'writing_category');
    $('#id_category_3').attr('id', 'translation_category');

    

    // Trigger category fullscreen overlay
    for (let i in categoryNames) {
        $(`#${categoryNames[i]}_category`).parent().on('click', function() {
            $(`#id_${categoryNames[i]}_categories`).removeClass('hide');
            $(`#id_${categoryNames[i]}_categories`).addClass('active-category');
            $(`#id_${categoryNames[i]}_categories`).css('visibility', 'visible').css('opacity', '1');
            $('body').addClass('category-overlay-active');
            // Show close button for fullscreen overlay
            $('.close-category').removeClass('hide');
        });
    };

    // Click effect 
    function categoryClickEffect() {
        var clicks = 0
        $('.category-overlay li.col.s6').on('click', function() {
            // Increment click count
            clicks += 1

            // Remove selected class from previously selected category
            $('.category-overlay li').children().removeClass('selected-category');

            // Add selected class
            if ($(this).children('input').attr('checked', true)) {
                $(this).children().addClass('selected-category');
            };

            // Remove selected class and checked attribute from the default checked radio value
            if ($(this).attr('id') === 'id_desktop' && clicks === 1) {
                $(this).children().removeClass('selected-category');
                $(this).children().children().children().attr('checked', false);
            };
        });

        // Reset click count
        $('.close-category').on('click', function() {
            clicks = 0;
        });
    };

    categoryClickEffect();

    // Close overlay
    $('.close-category, .exit-overlay').on('click', function() {
        // Hide fullscreen overlay
        $('.active-category').css('visibility', 'hidden').css('opacity', '0');

        // Change content container back to default
        $('.container.content').css('top', '6%').css('height', '94%').css(
            'overflow', 'auto').css('border-top-left-radius', '40px').css('border-top-right-radius', '40px');

        $('body').removeClass('category-overlay-active');
        // Hide close button for fullscreen overlay
        $('.close-category').addClass('hide');
        $('.exit-overlay').parent().addClass('hide');
    });

    /* ======================================================
    Toggle Package sections
    ====================================================== */

    var showBasic = $('#basicBtn');
    var showStandard = $('#standardBtn');
    var showPremium = $('#premiumBtn');

    var basicPackage = $('#basicPackage');
    var standardPackage = $('#standardPackage');
    var premiumPackage = $('#premiumPackage');

    showBasic.on('click', function() {
        basicPackage.removeClass('hide-on-med-and-down');
        $('.packages').removeClass('hide-on-med-and-down');
        $('.info-row').addClass('hide');
        $('#id_enable_all_packages').parent().parent().parent().addClass('hide');
        $('.package-btns').addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    showStandard.on('click', function() {
        standardPackage.removeClass('hide-on-med-and-down');
        $('.info-row').addClass('hide');
        $('#id_enable_all_packages').parent().parent().parent().addClass('hide');
        $('.package-btns').addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    showPremium.on('click', function() {
        premiumPackage.removeClass('hide-on-med-and-down');
        $('.info-row').addClass('hide');
        $('#id_enable_all_packages').parent().parent().parent().addClass('hide');
        $('.package-btns').addClass('hide');
        $('.next-btn').addClass('hide');
        $('.prev-btn').addClass('hide');
    });

    $('.cancel-package').on('click', function() {
        $(this).parent().parent().parent().parent().parent().addClass('hide-on-med-and-down');
        $('.info-row').removeClass('hide');
        $('#id_enable_all_packages').parent().parent().parent().removeClass('hide');
        $('.package-btns').removeClass('hide');
        $('.next-btn').removeClass('hide');
        $('.prev-btn').removeClass('hide');
    });

    $('.save-package').on('click', function() {
        $(this).parent().parent().parent().parent().parent().addClass('hide-on-med-and-down');
        $('.info-row').removeClass('hide');
        $('#id_enable_all_packages').parent().parent().parent().removeClass('hide');
        $('.package-btns').removeClass('hide');
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


    /* ======================================================
    Disable / enable packages
    ====================================================== */

    $('#id_enable_all_packages').on('click', function() {
        if ($('#id_enable_all_packages').is(':checked') == false) {
            $('#standardBtn').addClass('disabled');
            $('#premiumBtn').addClass('disabled');
        } else {
            $('#standardBtn').removeClass('disabled');
            $('#premiumBtn').removeClass('disabled');
        }
    });

    /* ======================================================
    Chips container - Freelance Service
    ====================================================== */

    /* =======================================
    Define skills for each cateogory
    ======================================= */

    /* WEB, MOBILE & SOFTWARE DEVELOPMENT */
    var desktopArr = [
        'MySQL', 'API', 'Windows Forms', 'PostgreSQL', 'SQL',
        '.NET Framework', 'Mac OS App Development', 'Azure Cosmos DB',
        'Multithreading Programming', 'MongoDB', 'Microsoft SQL Server',
        'XML', 'Application Installer', 'Apache CouchDB'
    ];
    var mobileArr = [
        'MySQL', 'Social Media Account Integration', 'Swift', 'Tablet', 'SQLite',
        'In-App Purchases', 'React Native', 'Firebase', 'User Authentication',
        'Objective-C', 'MongoDB', 'Microsoft SQL Server',
        'In-App Advertising', 'Map Integration'
    ];
    var gameArr = [
        'HTML', 'Game Programming', 'UX', 'Python', 'AR', 'Unity',
        'Web Design', 'iOS Development', 'Graphic Design',
        '.io Game', 'Animation', 'Prototypes',
        'Game Design', '3D Modeling', 'VR'
    ];
    var otherArr = [
        'RTOS', 'Embedded Systems', 'Arduino', 'Embedded Linux', 'ESP32',
        'PIC', 'BLE', 'Device Firmware', 'Zigbee', 'WiFi', 'NFC',
    ];
    var testingArr = [
        'Mobile App Testing', 'Usability Testing', 'User Experience Design',
        'Visual Communication', 'JUnit', 'DevTools', 'Automated Testing',
    ];
    var uxArr = [
        'Visual Communication', 'Web Design', 'Usability Testing', 'Axure RP',
        'User Interface Desgin', 'Software Design', 'User Experience Design',
        'Webflow', 'Competitive Analysis', 'Adobe XD', 'Mobile App Design',
        'Game Design', 'iPhone UI Design', 'Figma', 'Adobe Photoshop'
    ];
    var webArr = [
        'MySQL', 'API', 'Hibernate', 'Python', 'SQL', 'PostgreSQL', 'CI/CD',
        'Business Logic Layer', 'Automatic Deployment Pipeline', 'PHP',
        'AngularJS', 'Microsoft SQL Server', 'Spring Framework',
        'Requirements Specification', 'MongoDB'
    ];

    /* DESIGN & CREATIVE */
    var artArr = [
        '2D Animation', 'Freestyle Drawing', 'Caricature Drawing', 'Drawing',
        'Graphic Design', 'Digital Painting', 'Storyboarding', 'Manga',
        'Clip Studio Paint', 'Facebook Games Development', 'Anime',
        '2D Design', 'Animation', 'Adobe Illustrator', 'Cartoons'
    ];
    var audioArr = [
        'Jazz', 'Guitar Compostion', 'Percussion', 'MIDI', 'Piano',
        'Guitar Performance', 'Sibelius', 'Adobe Audition', 'Rock',
        'Musical Composition', 'Vocals', 'Musical Transcription',
    ];
    var videoArr = [
        'Animation', 'Adobe Character Animator', 'Flipbook',
        'Blender', 'Adobe Animate', 'Dragonframe',
        'Luminar AI', 'Lightworks'
    ];
    var designArr = [
        'Adobe Photoshop', 'Figma', 'Adobe Illustrator',
        'Design Wizard', 'Adobe InDesign', 'Canva',
        'Microsoft Office'
    ];
    var artsArr = [
        'Translation', 'Musical Composition',
        'Voice Talent', 'Creative Writing', 'Vocals',
    ];
    var photoArr = [
        'Adobe Photoshop', 'Lightworks', 'Graphic Design',
        'Adobe Lightroom', 'Good Communication',
    ];
    var brandingArr = [
        'HTML', 'Brand Positioning', 'Layout Design', 'Web Design',
        'Graphic Design', 'Drawing', 'Adobe Creative Suite',
        'Print Marketing Materials', 'Brand Guidelines',
        'Print Advertising', 'User Experience Design',
        'Adobe Illustrator', 'Business Card Design',
        'Packaging'
    ];
    var gamingArr = [
        'Fusion 360', 'Substance Painter', 'MarvelousDesigner', 'Adobe After Effects',
        'The Foundry NUKE', 'Autodesk 3ds Max', 'Graphic Design', 'Virtual Reality',
        'Motion Graphics', 'Adobe Illustrator', '3D Animation', 'Animation',
        'Game Design', '3D Modeling', 'VFX Animation', 'UV Mapping'
    ];

    /* WRITING */
    var contentArr = [
        'Media & Entertainment', 'Article Writing', 'Website Content', 'Education',
        'Business Services', 'Art', 'Copywriting', 'Research', 'Fact-Checking',
        'About Us Page', 'Creative Writing', 'Product Page', 'Landing Page',
    ];
    var creativeArr = [
        'Fiction Writing', 'Explainer Video', 'Screencast', 'Trailer',
        'Screenwriting', 'Microsoft Word', 'Copywriting', 'Feature',
        'Proofreading', 'Broadcast Journalism', 'Commercial',
        'Documentary', 'Final Draft'
    ];
    var editingArr = [
        'Error Checking', 'English Spelling', 'Document Version Control', 'Editing',
        'Text Formatting', 'Microsoft Word', 'Copywriting', 'Research', 'Markup',
        'Proofreading', 'English Punctuation', 'English Grammar'
    ];
    var resumesArr = [
        'Media & Entertainment', 'Operations Management', 'Proofreading', 'Life Coaching',
        'Business Services', 'Arts', 'AccountAbility', 'Interview Preparation',
        'Management Skills', 'Resume Design', 'Data Entry', 'Education',
    ];
    var technicalArr = [
        'IT', 'Quantitative Research', 'Proofreading', 'Tutorial', 'Content Management',
        'Technical Editing', 'Article', 'FAQ', 'Instruction Manual', 'Statistics',
        'Software', 'SEO Audit', 'Qualitative Research', 'Technical Writing'
    ];

    /* TRANSLATION */
    var generalArr = [
        'Microsoft Word', 'Translation', 'Spanish - Latin American', 'Engish Tutoring', 'German',
        'French', 'Spanish - Mexico', 'Chinese - Mandarin', 'Chinese - Cantonese', 'Education',
        'Korean', 'Japanese', 'Russian', 'Ukrainian', 'Editing', 'Proofreading', 'Dutch'
    ];
    var legalArr = [
        'Microsoft Word', 'Translation', 'Official Correspondence Translation', 'Documentation', 'Writing',
        'Contract Translations', 'Product Documentation', 'Article Rewriting', 'Transcription', 'Editing',
        'Technical Manuals', 'Agreements', 'Official Documents Translation', 'Proofreading',
    ];
    var medicalArr = [
        'Translation', 'Data Analysis', 'Stata', 'Documentation', 'Medical',
        'Contract Translations', 'Product Documentation', 'Adobe Acrobat',
        'Technical Manuals', 'Medical Terminology', 'Technical Editing'
    ];

    /* =======================================
    Add skills of chosen category
    to popular search tags
    ======================================= */

    var categoryRadios = $('#ServiceCategory input[type="radio"]');
    var categorySelection;

    categoryRadios.on('change', function() {
        // Define value for category selection variable
        if ($(categoryRadios).is(':checked')) {
            var categorySelection = $(this).val();
        };

        // Grab popular search tags container
        var popularTagsContainer = $('.popular-tags');


        // Ensure that the container is empty before adding chips
        if ($(popularTagsContainer).is(':empty')) {
            setPopularTags();
        } else {
            $(popularTagsContainer).empty();
            setPopularTags();
        };

        /* =======================================
        Add appropriate chips to popular search
        tags container by iterating through
        the category skills array and
        adding the html as chips
        ======================================= */

        function setPopularTags() {
            if (categorySelection == 1) {
                // Iterate through category skills array and add to html as chips
                for (i in desktopArr) {
                    chip_html = `<div class="chip">${desktopArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 2) {
                // Iterate through category skills array and add to html as chips
                for (i in mobileArr) {
                    chip_html = `<div class="chip">${mobileArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 4) {
                // Iterate through category skills array and add to html as chips
                for (i in gameArr) {
                    chip_html = `<div class="chip">${gameArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 5) {
                // Iterate through category skills array and add to html as chips
                for (i in otherArr) {
                    chip_html = `<div class="chip">${otherArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 6) {
                // Iterate through category skills array and add to html as chips
                for (i in testingArr) {
                    chip_html = `<div class="chip">${testingArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 7) {
                // Iterate through category skills array and add to html as chips
                for (i in uxArr) {
                    chip_html = `<div class="chip">${uxArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 8) {
                // Iterate through category skills array and add to html as chips
                for (i in webArr) {
                    chip_html = `<div class="chip">${webArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 9) {
                // Iterate through category skills array and add to html as chips
                for (i in artArr) {
                    chip_html = `<div class="chip">${artArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 10) {
                // Iterate through category skills array and add to html as chips
                for (i in audioArr) {
                    chip_html = `<div class="chip">${audioArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 11) {
                // Iterate through category skills array and add to html as chips
                for (i in videoArr) {
                    chip_html = `<div class="chip">${videoArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 12) {
                // Iterate through category skills array and add to html as chips
                for (i in designArr) {
                    chip_html = `<div class="chip">${designArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 13) {
                // Iterate through category skills array and add to html as chips
                for (i in photoArr) {
                    chip_html = `<div class="chip">${photoArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 14) {
                // Iterate through category skills array and add to html as chips
                for (i in brandingArr) {
                    chip_html = `<div class="chip">${brandingArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 15) {
                // Iterate through category skills array and add to html as chips
                for (i in gamingArr) {
                    chip_html = `<div class="chip">${gamingArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 16) {
                // Iterate through category skills array and add to html as chips
                for (i in contentArr) {
                    chip_html = `<div class="chip">${contentArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 17) {
                // Iterate through category skills array and add to html as chips
                for (i in creativeArr) {
                    chip_html = `<div class="chip">${creativeArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 18) {
                // Iterate through category skills array and add to html as chips
                for (i in editingArr) {
                    chip_html = `<div class="chip">${editingArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 19) {
                // Iterate through category skills array and add to html as chips
                for (i in resumesArr) {
                    chip_html = `<div class="chip">${resumesArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 20) {
                // Iterate through category skills array and add to html as chips
                for (i in technicalArr) {
                    chip_html = `<div class="chip">${technicalArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 21) {
                // Iterate through category skills array and add to html as chips
                for (i in generalArr) {
                    chip_html = `<div class="chip">${generalArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 22) {
                // Iterate through category skills array and add to html as chips
                for (i in legalArr) {
                    chip_html = `<div class="chip">${legalArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            } else if (categorySelection == 23) {
                // Iterate through category skills array and add to html as chips
                for (i in medicalArr) {
                    chip_html = `<div class="chip">${medicalArr[i]}<i class="fas fa-plus-circle"></i></div>`;
                    popularTagsContainer.append(chip_html);
                };
            };
        };


        /* =======================================
        Add functionality to allow users to
        add chips from the popular search
        tags container to the hidden
        chips input form
        ======================================= */

        function addChipsFromPopularTags() {
            // Grab the tags from popular tags div and add to array
            var tagsText = $('.popular-tags').text();
            var popularTagsArr = tagsText.split(' ');

            // Remove empty fields from array
            // ! Work around for a minor bug
            for (i=0; i < popularTagsArr.length; i++) {
                if (popularTagsArr[i] === '') {
                    popularTagsArr.splice(i, 1);
                };
            };

            var popularChip = $('.popular-tags .chip');

            popularChip.on('click', function() {
                // Grab chips from html container to prevent duplicate chips from being added
                var current_container = $('.chips-container').text();

                // Add chip to container if it does not already exist
                if (!current_container.includes($(this).text())) {
                    container = $('.chips-container');
                    html_code = `<div class="chip">${$(this).text()}<i class="close material-icons">close</i></div>`;
                    container.append(html_code);
                };
                // Refresh value of input field
                chips.val('');

                /* Remove chip from popular tags container once
                added to the current tags container */
                $(this).remove();

                isChipsContainerEmpty();
            });
        };

        addChipsFromPopularTags();


        /* =======================================
        Add the chip back into the popular tags
        container if the chip was removed
        from current tags
        ======================================= */

        function deleteSuggestedChip() {
            $('.chips-container').on('click', '.chip .close', function() {
                // Add the value of the removed tag to a variable
                var removedTag = $(this).parent().text()
                // Remove the close text from the times button
                removedTag = removedTag.replace('close', '');

                var popularContainer = $('.popular-tags').text();

                // Grab the appropriate popular tags for the chosen category
                let chosenCategory = categorySelection
                let textValue;

                if (chosenCategory == 1) {
                    textValue = 'desktop';
                } else if (chosenCategory == 2) {
                    textValue = 'mobile';
                } else if (chosenCategory == 4) {
                    textValue = 'game';
                } else if (chosenCategory == 5) {
                    textValue = 'other';
                } else if (chosenCategory == 6) {
                    textValue = 'testing';
                } else if (chosenCategory == 7) {
                    textValue = 'ux';
                } else if (chosenCategory == 8) {
                    textValue = 'web';
                } else if (chosenCategory == 9) {
                    textValue = 'art';
                } else if (chosenCategory == 10) {
                    textValue = 'audio';
                } else if (chosenCategory == 11) {
                    textValue = 'video';
                } else if (chosenCategory == 12) {
                    textValue = 'design';
                } else if (chosenCategory == 13) {
                    textValue = 'photo';
                } else if (chosenCategory == 14) {
                    textValue = 'branding';
                } else if (chosenCategory == 15) {
                    textValue = 'gaming';
                } else if (chosenCategory == 16) {
                    textValue = 'content';
                } else if (chosenCategory == 17) {
                    textValue = 'creative';
                } else if (chosenCategory == 18) {
                    textValue = 'editing';
                } else if (chosenCategory == 19) {
                    textValue = 'resumes';
                } else if (chosenCategory == 20) {
                    textValue = 'technical';
                } else if (chosenCategory == 21) {
                    textValue = 'general';
                } else if (chosenCategory == 22) {
                    textValue = 'legal';
                } else if (chosenCategory == 23) {
                    textValue = 'medical';
                }

                let categoryTags = eval(`${textValue}Arr`);

                /* Add chip to container if it does not already exist and
                if it is in the chosen category's tags array */
                if (!popularContainer.includes(removedTag) && categoryTags.includes(removedTag)) {
                    container = $('.popular-tags');
                    html_code = `<div class="chip">${removedTag} <i class="fas fa-plus-circle"></i></div>`;
                    container.append(html_code);
                };
            });
        };

        deleteSuggestedChip();

    });
});