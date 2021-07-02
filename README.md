# Legion


## Contents 

- [UX](#ux)

    - [User Stories](#user-stories)

- [Contents](#contents)

    - [credits](#credits)

        - [Code](#code)



-----

## UX


### User Stories

The full spreedsheet that defines all of the user stories can be accessed [here](https://docs.google.com/spreadsheets/d/1KYb3yVm8IIQM_jBeD-Tyxuno-kC5TYOTrA6sQpfI36Y/edit?usp=sharing)

#### Viewing and Navigation

![User stories spreadsheet](documentation/media/user-stories-1.png)


#### Registration and User Accounts

![User stories spreadsheet](documentation/media/user-stories-1.png)


#### Purchasing a Service

![User stories spreadsheet](documentation/media/user-stories-1.png)


#### Admin and Store Management

![User stories spreadsheet](documentation/media/user-stories-1.png)


-----

## Contents


### Credits

#### Code

- I followed [this official documentation](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) to create my own custom user model, which included removing the username from Allauth's registration functionality and adding my own required fields.

- When creating the custom user model, I had to reset the database in order to make migrations work correctly. To do that I used [Django Extensions](https://django-extensions.readthedocs.io/en/latest/), which allowed me to use the command line to easily reset the database. [This source](https://stackoverflow.com/questions/2289187/complete-django-db-reset) led me to use such a method.

- I used [this source](https://www.fullstackpython.com/django-utils-timezone-now-examples.html) to set a default for DateField in my models.

- I used [this source](https://github.com/Tivix/django-rest-auth/issues/261) to fix 'NoModuleError' for user. Adding `ACCOUNT_USER_DISLAY = lambda user: user.get_username()` to settings.py fixed this error and got Allauth's confirmation email functionality working correctly.

- The code above would throw a PEP8 violation warning due to the use of a lambda. I used [this source](https://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def) to change it to `def ACCOUNT_USER_DISPLAY(user): return user.get_username()`

- To add placeholders to the custom user models for the account registration/login forms, I looked to [this source](https://izziswift.com/how-do-i-add-a-placeholder-on-a-charfield-in-django/)

- For handling background images, I based my CSS code from [this source](https://www.sitepoint.com/css3-transform-background-image/) and also [this source](https://css-tricks.com/almanac/properties/b/background-position/)

- I used [this source](https://www.geeksforgeeks.org/custom-field-validations-in-django-models/) to make a custom validation error for the date of birth input field on the registration form.

- I used [this source](https://www.tutorialsrack.com/articles/205/how-to-get-the-year-month-and-day-from-a-datetime-in-python) for help on using the date and time python modules, which was used to create the custom validation error for the date of birth input field.