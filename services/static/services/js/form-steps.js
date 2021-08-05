$(document).ready(function() {
    /* ======================================================
    Form steps
    ----------

    The code used is based upon
    the following source:
    'https://www.w3schools.com/howto/howto_js_form_steps.asp'

    ====================================================== */

    // Prevent form submission when pressing enter to avoid missing steps
    $('form').on('keypress', function(e) {
        return e.which !== 13;
    });

    // Set current tab to first tab
    var currentTab = 0;
    // Display the current tab
    showTab(currentTab);

    $('.next-btn').on('click', function() {
        if (currentTab === 0) {
            if ($('.active-category .subcategory .category-box').hasClass('selected-category')) {
                next();
            }
        } else {
            next()
        }
    });

    $('.prev-btn').on('click', function() {
        prev();
    });

    $('.skip-section').on('click', function() {
        skipSection();
    });
    
    // Display the specified tab of the the form
    function showTab(n) {
        var x = document.getElementsByClassName("tab");
        x[n].style.display = "block";

        if (n == 0) {
            nextForCategorySection()
            $('.btn-cancel').parent().removeClass('hide');
            $('.next-btn').parent().addClass('hide');
            $('.prev-btn').parent().addClass('hide');
        } else {
            $('.next-btn').parent().removeClass('hide');
            $('.prev-btn').parent().removeClass('hide');
            $('.btn-cancel').parent().addClass('hide');
        };

        // if you have reached the end of the form... :
        if (n == (x.length - 1)) {
            // show the submit to submit the form
            $('.next-btn').parent().addClass('hide');
            $('.submit-btn').parent().removeClass('hide');
        };
    };

    function nextForCategorySection() {
        /* Show form steps next button once a category box is clicked
        and the subcategory overlay is active  */
        $('.subcategory .category-box').on('click', function() {
            if ($('body').hasClass('category-overlay-active')) {
                $('.next-btn').parent().removeClass('hide');
                $('.next-btn').addClass('for-category-overlay');
            };
        });

        /* Hide the next button and remove its 'for-category-overlay'
        class when the close button is clicked */
        $('.close-category').on('click', function() {
            $('.next-btn').removeClass('for-category-overlay');
            $('.next-btn').parent().addClass('hide');
        });

        /* Remove the 'for-category-overlay' class once the next button 
        is clicked to reset it to its default behaviour. 
        Only trigger the next form step if 
        a category has been chosen. */
        $('.next-btn').on('click', function() {
            if ($('.active-category .subcategory .category-box').hasClass('selected-category')) {
                $('.next-btn').removeClass('for-category-overlay');
                $('.close-category').addClass('hide');
            };
        });
    };
    
    // Display the next tab
    function next() {
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
    };

    // Display the previous tab
    function prev() {
        var x = document.getElementsByClassName("tab");
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase or decrease the current tab by 1:
        currentTab = currentTab - 1;
        // if you have reached the end of the form... :
        if (currentTab >= x.length) {
            return false;
        }
        // Otherwise, display the correct tab:
        showTab(currentTab);
    };
    
    // An option to skip tabs
    function skipSection(n) {
        var x = document.getElementsByClassName("tab");
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase current tab by 1:
        currentTab = currentTab + 1;
        // Display the correct tab:
        showTab(currentTab);
    };
    
    // Ensure input fields are filled before moving to the next tab
    function validateForm() {
        var x, y, i, valid = true;
        x = $('.tab');

        currentFields = $(x[currentTab]).find('input');

        // Check if required fields are filled
        if ($(currentFields).attr('required')) {
            for (i = 0; i < currentFields.length; i++) {
                if ($(currentFields[i]).val() === '') {
                    valid = false;
                };
            };
            if (valid === false) {
                alert('Please complete all required fields!');
            };
        };
        // If the valid status is true, mark the step as finished and valid:
        return valid;
    };
});