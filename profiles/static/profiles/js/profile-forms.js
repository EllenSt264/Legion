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
    Form steps
    ----------

    The code used is based upon
    the following source:
    'https://www.w3schools.com/howto/howto_js_form_steps.asp'

    ====================================================== */

    // Set current tab to first tab
    var currentTab = 0;
    // Display the current tab
    showTab(currentTab);

    $('.next-btn').on('click', function() {
        nextPrev(1);
    });

    $('.prev-btn').on('click', function() {
        nextPrev(-1);
    });

    $('.skip-section').on('click', function() {
        skipSection();
    });

    $('.skip-section-2').on('click', function() {
        skipSection2();
    });

    $('#skipEducation').on('click', function() {
        makeEducationOptional();
    });

    $('#skipWorkExperience').on('click', function() {
        makeWorkExperienceOptional();
    });
    
    // Display the specified tab of the the form
    function showTab(n) {
        var x = document.getElementsByClassName("tab");
        x[n].style.display = "block";

        if (n == 0) {
            $('#cancelBtn').removeClass('hide');
            $('.prev-btn').addClass('hide');
        } else {
            $('.prev-btn').removeClass('hide');
            $('#cancelBtn').addClass('hide');
        }

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
        currentTab = currentTab + n;
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

    // For skipping the Education and/or Work Experience tabs
    function skipSection2(n) {
        var x = document.getElementsByClassName("tab");
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase current tab by 1:
        currentTab = currentTab + 2;
        // Display the correct tab:
        showTab(currentTab);
    }

    // Update Education fields as optional
    function makeEducationOptional() {
        var educationForm = $('#AddEducation');
        var inputFields = $(educationForm).find('input:required');

        inputFields.prop('required', false);
    }

    // Update Work Experience fields as optional
    function makeWorkExperienceOptional() {
        var workexperienceForm = $('#AddWorkExperience');
        var inputFields = $(workexperienceForm).find('input:required');

        inputFields.prop('required', false);
    }
    
    // Ensure input fields are filled before moving to the next tab
    function validateForm() {
        var x, y, i, valid = true;
        x = $('.tab')
        y = x[currentTab].getElementsByTagName("input");

        currentFields = $(x[currentTab]).find('input');

        // Check if required fields are filled

        for (i = 0; i < currentFields.length; i++) {
            if (($(currentFields[i]).is('required') && $(currentFields[i]).value === '') || ($(currentFields[i]).is('required') && currentFields[i].is(':checked') !== true)) {
                alert('Please complete all required fields');
            }
        }


        if ($(currentFields).attr('required')) {
            for (i = 0; i < currentFields.length; i++) {
                if (($(currentFields[i]).val() === '') || ($(currentFields).is(':checked') !== true)) {
                    valid = false;
                }
            }

            if (valid === false) {
                alert('Please complete all required fields!');
            }
        }

        // If the valid status is true, mark the step as finished and valid:
        return valid;
    }


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
                };
                // Refresh value of input field
                skills.val('');
            }
        });
    };
    addChips();

    // Add chips to hidden form
    function chipsToForm() {
        $('#nextBtn-creator').on('click', function() {
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

        // Add close button for fullscreen overlay
        $(`#${categoryTypes[i]}Categories`).prepend('<li><a href="#!"><i class="far fa-times-circle close-category"></i></a></li>');
    };

    // Trigger category fullscreen overlay
    for (let i in categoryTypes) {
        $(`#${categoryTypes[i]}Container h6`).on('click', function() {
            // Trigger fullscreen overlay
            $(`#${categoryTypes[i]}Container .category-overlay`).css('visibility', 'visible').css('opacity', '1');
            // Change content container to mimic a fullscreen overlay
            $('.container.content').css('top', '0').css('height', '100%').css('overflow', 'hidden').css('border-radius', '0');
        });
    }

    // Close overlay
    $('.close-category').on('click', function() {
        // Hide fullscreen overlay
        $(this).parent().parent().parent().css('visibility', 'hidden').css('opacity', '0');
        // Change content container back to default
        $('.container.content').css('top', '6%').css('height', '94%').css(
            'overflow', 'auto').css('border-top-left-radius', '40px').css('border-top-right-radius', '40px');
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
});