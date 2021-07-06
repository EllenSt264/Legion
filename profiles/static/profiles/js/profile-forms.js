$(document).ready(function() {
    /* ======================================================
    Materialize switch
    ====================================================== */

    var checkbox = $('#id_is_recruiter');

    // Add materalize switch classes to checkbox
    checkbox.parent().parent().addClass('switch');
    checkbox.next().addClass('lever');
    checkbox.after("I'm a Recruiter");


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

    $('#nextBtn').on('click', function() {
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
            $('#nextBtn').addClass('hide');
            $('#submitBtn').removeClass('hide');
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
        x = document.getElementsByClassName("tab");
        y = x[currentTab].getElementsByTagName("input");
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