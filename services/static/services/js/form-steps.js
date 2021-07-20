$(document).ready(function() {
    /* ======================================================
    Materialize switch
    ====================================================== */
    
    // Grab checkboxes
    var checkbox = $('input[type=checkbox]');
    var packageSwitch = $('#id_enable_all_packages');

    // Add materalize switch classes to checkbox
    checkbox.parent().parent().addClass('switch');
    checkbox.next().addClass('lever');
    packageSwitch.after('3 Packages');


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
    Materialize chips
    ====================================================== */

    var searchTags = $('#searchTags');

    // Add materialize chips class to input field
    searchTags.parent().addClass('chips');
    searchTags.parent().removeClass('col s12');
    searchTags.removeClass('validate');

    // Add focus class
    searchTags.parent().on('click', function() {
        searchTags.parent().toggleClass('focus');
        searchTags.focus();
    });

    // Prevent form from trying to submit when a user presses enter
    $(searchTags).on('keypress', function(e) {
        return e.which !== 13;
    });

    // Add chips
    function addChips() {
        $(searchTags).on('keypress', function(e) {
            let keycode = (event.keyCode ? event.keyCode : event.which);
            // Get text value from input field
            let value = searchTags.val();
            if(keycode == '13') {
                // Prevent string with only whitespace and/or special characters
                var regExp = /[a-zA-Z]/g;

                // Grab chips from html container to prevent duplicate chips from being added
                var current_container = $('.current-tags .col.s12').text();

                if (regExp.test(value) && !current_container.includes(value)) {
                    container = $('.current-tags .col.s12');
                    html_code = `<div class="chip">${value}<i class="close material-icons">close</i></div>`;
                    container.append(html_code);
                };
                // Refresh value of input field
                searchTags.val('');
            }
        });
    };
    addChips();

    // Add chips to hidden form
    function chipsToForm() {
        $('#nextBtn-service').on('click', function() {
            // Grab chips from html container
            var container = $('.current-tags .col.s12').text();
    
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
            $('#id_service_search_tags').val(chips_arr);
        });
    };
    chipsToForm();


    /* ======================================================
    Toggle required for packages
    ====================================================== */

    if ($('#id_enable_all_packages').is(':checked')) {
        var inputFields = $('.packages-smscreen').find('input');
        inputFields.prop('required', false);
    };


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
    
    // Display the specified tab of the the form
    function showTab(n) {
        var x = document.getElementsByClassName("tab");
        x[n].style.display = "block";

        if (n == 0) {
            $('.btn-cancel').removeClass('hide');
            $('.prev-btn').addClass('hide');
        } else {
            $('.prev-btn').removeClass('hide');
            $('.btn-cancel').addClass('hide');
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
    
    // Ensure input fields are filled before moving to the next tab
    function validateForm() {
        var x, y, i, valid = true;
        x = $('.tab')

        currentFields = $(x[currentTab]).find('input');

        // Check if required fields are filled

        if ($(currentFields).attr('required')) {
            for (i = 0; i < currentFields.length; i++) {
                if ($(currentFields[i]).val() === '') {
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
});