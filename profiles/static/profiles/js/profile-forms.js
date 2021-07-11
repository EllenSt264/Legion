$(document).ready(function() {
    /* ======================================================
    Materialize switch
    ====================================================== */
    
    // Grab checkboxes
    var checkbox = $('input[type=checkbox]');
    var recruiterSwitch = $('#id_is_recruiter');
    var workingHereSwitch = $('#id_currently_working_here');

    // Add materalize switch classes to checkbox
    checkbox.parent().parent().addClass('switch');
    checkbox.next().addClass('lever');
    recruiterSwitch.after("I'm a Recruiter");
    workingHereSwitch.after("I'm currently working here");


    /* ======================================================
    Materialize chips
    ====================================================== */

    var skills = $('#skillsChips');

    // Add materialize chips class to input field
    skills.parent().addClass('chips');
    skills.parent().removeClass('col s12');
    skills.removeClass('validate');

    // Add focus class
    skills.parent().on('click', function() {
        skills.parent().toggleClass('focus');
        skills.focus();
    });

    // Prevent form from trying to submit when a user presses enter
    $(skills).on('keypress', function(e) {
        return e.which !== 13;
    });

    // Add chips
    function addChips() {
        $(skills).on('keypress', function(e) {
            let keycode = (event.keyCode ? event.keyCode : event.which);
            // Get text value from input field
            let value = skills.val();
            if(keycode == '13') {
                // Prevent string with only whitespace and/or special characters
                var regExp = /[a-zA-Z]/g;

                // Grab chips from html container to prevent duplicate chips from being added
                var current_container = $('.chips-container').text();

                if (regExp.test(value) && !current_container.includes(value)) {
                    container = $('.chips-container');
                    html_code = `<div class="chip">${value}<i class="close material-icons">close</i></div>`;
                    container.append(html_code);
                    console.log(current_container);
                };
                // Refresh value of input field
                skills.val('');
            }
        });
    };
    addChips();

    // Add chips to hidden form
    function chipsToForm() {
        $('#addSkills').on('click', function() {
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
            $('#id_skills').val(chips_arr);
        });
    };
    chipsToForm();


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

    var expertiseRadios = $('input[name=expertise_level]');

    /* ======================================================
    Radio buttons - Expertise level
    ====================================================== */

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

    // Add hidden classes to category radio buttons
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Categories`).addClass('hide');
        $(`#${categoryTypes[i]}Categories`).addClass('category-tab');
    };

    // Activate relevant tabs
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Container .title`).on('click', function() {
            $(`#${categoryTypes[i]}Categories`).toggleClass('hide');
        });
    };


    /* ======================================================
    Form steps
    ----------

    The code used is based upon
    the following source:
    https://www.w3schools.com/howto/howto_js_form_steps.asp'

    ====================================================== */

    // Set current tab to first tab
    var currentTab = 0;
    // Display the current tab
    showTab(currentTab);

    $('.next-btn').on('click', function() {
        nextPrev();
    });

    $('.skip-section').on('click', function() {
        skipSection();
    })
    
    // Display the specified tab of the the form
    function showTab(n) {
        var x = document.getElementsByClassName("tab");
        x[n].style.display = "block";
        // if you have reached the end of the form... :
        if (n == (x.length - 1)) {
            // show the submit to submit the form
            $('.next-btn').addClass('hide');
            $('.submit-btn').removeClass('hide');
        }
    }
    
    // Display the next or previous tab
    function nextPrev(n) {
        var x = document.getElementsByClassName("tab");
        // Exit the function if any field in the current tab is invalid:
        if (!validateForm()) return false;
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase or decrease the current tab by 1:
        currentTab = currentTab + 1;
        // if you have reached the end of the form... :
        if (currentTab >= x.length) {
            return false;
        }
        // Otherwise, display the correct tab:
        showTab(currentTab);
    }
    
    // An option to skip tabs
    function skipSection(n) {
        var x = document.getElementsByClassName("tab");
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase current tab by 1:
        currentTab = currentTab + 1;
        // Display the correct tab:
        showTab(currentTab);
    }

    // Ensure input fields are filled before moving to the next tab
    function validateForm() {
        var x, y, i, valid = true;
        x = $('.tab')
        y = x[currentTab].getElementsByTagName("input");

        currentFields = $(x[currentTab]).find('input');

        // A loop that checks every input field in the current tab:
        for (i = 0; i < y.length; i++) {
            // If a field is empty...
            // Check if required fields are filled
            // Add tooltips
            $(y[i]).addClass('tooltipped');
            $(y[i]).tooltip({delay: 50, position: 'top', isOpen: true, isHovered: false});

            // For checkboxes
            if ($(y[i]).is(':checked') != true) {
                if ($(y[i]).prop('type') == 'checkbox') {
                    // Trigger tooltip 
                    $(y[i]).attr('data-tooltip', 'Please check this');
                    $(y[i]).tooltip('open');
                    valid = false;
                }
            }
            // For text input fields
            if (y[i].value === '') {
                if ($(y[i]).hasClass('invalid')) {
                    $(y[i]).removeClass('invalid');
                } else {
                    $(y[i]).addClass('invalid');
                }
                // Trigger tooltip 
                $(y[i]).attr('data-tooltip', 'Please complete this field');
                $(y[i]).tooltip('open');
                valid = false;
            }
        }
        // If the valid status is true, mark the step as finished and valid:
        return valid;
    }
});