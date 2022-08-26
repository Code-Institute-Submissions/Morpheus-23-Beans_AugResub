# Testing

## Table of Contents
- [Testing](#testing)
  - [Table of Contents](#table-of-contents)
  - [Code Validation](#code-validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)


## Code Validation

### HTML Validation
All HTML pages were tested using [W3C Markup Validation](https://validator.w3.org/). 
- Page source were passed through the validator 
  - Landing Page : No Errors
  - Product pages: 

    ```
    Error: Duplicate ID user-options.

        From line 138, column 9; to line 138, column 151

        >↩        <a class="text-orange nav-link d-block d-lg-none" href="#" id="user-options" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">↩     

        Warning: The first occurrence of ID user-options was here.

        From line 76, column 29; to line 77, column 75

                <a class="text-orange nav-link" href="#" id="user-options" data-toggle="dropdown"↩                                aria-haspopup="true" aria-expanded="false">↩     
    ```
  - Product List pages: No Errors 
  - Shopping Bag:

    ```
    Error: An img element must have an alt attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.

        From line 281, column 29; to line 281, column 103

          <img class="img-fluid rounded" src="/media/beans-arabica-colombia-B02.jpg">↩     

    Error: An img element must have an alt attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.

        From line 338, column 29; to line 338, column 96

          <img class="img-fluid rounded" src="/media/cup-chino-green-C04.jpg">↩     
    ```
  - Checkout Bag:

    ```
        Error: Attribute placeholder not allowed on element select at this point.

        From line 656, column 29; to line 656, column 153

          <select name="country" placeholder="Postal Code" class="stripe-style-input lazyselect form-control" required id="id_country">↩  <op

            Attributes for element select:
            Global attributes
            autocomplete — Hint for form autofill feature
            disabled — Whether the form control is disabled
            form — Associates the element with a form element
            multiple — Whether to allow multiple values
            name — Name of the element to use for form submission and in the form.elements API
            required — Whether the control is required for form submission
            size — Size of the control
            Warning: Empty heading.

            From line 1224, column 9; to line 1224, column 57

          <h1 class="text-light logo-font loading-spinner">↩   
    ``` 

  - Order Completed: No Errors
  

### CSS Validation 
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the base.css 

- base.css: No Errors
 
  
 
### JavaScript Validation 

[JSHint Validator](https://jshint.com/) was used:
- stripe-elements.js


    ```
    Two warnings
    34	'template literal syntax' is only available in ES6 (use 'esversion: 6').
    98	'template literal syntax' is only available in ES6 (use 'esversion: 6').

    ``` 

- countryfields.js
  
    ```
    Two warnings
    1	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    4	Unnecessary semicolon.

    ``` 

### Python Validation 

Python Flake8 validator was used to test the python files
```
./beans/settings.py:141:80: E501 line too long (91 > 79 characters)
./beans/settings.py:144:80: E501 line too long (81 > 79 characters)
./beans/settings.py:147:80: E501 line too long (82 > 79 characters)
./beans/settings.py:150:80: E501 line too long (83 > 79 characters)
./beans/settings.py:218:51: W292 no newline at end of file
./bag/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./bag/models.py:1:1: F401 'django.db.models' imported but unused
./bag/admin.py:1:1: F401 'django.contrib.admin' imported but unused
./bag/views.py:38:27: E225 missing whitespace around operator
./bag/views.py:40:80: E501 line too long (128 > 79 characters)
./bag/views.py:41:80: E501 line too long (83 > 79 characters)
./bag/views.py:44:21: E128 continuation line under-indented for visual indent
./bag/views.py:44:80: E501 line too long (88 > 79 characters)
./bag/views.py:45:21: E128 continuation line under-indented for visual indent
./bag/views.py:48:21: E128 continuation line under-indented for visual indent
./bag/views.py:49:21: E128 continuation line under-indented for visual indent
./bag/views.py:50:21: E128 continuation line under-indented for visual indent
./bag/views.py:53:80: E501 line too long (94 > 79 characters)
./bag/views.py:55:17: E128 continuation line under-indented for visual indent
./bag/views.py:55:80: E501 line too long (84 > 79 characters)
./bag/views.py:56:17: E128 continuation line under-indented for visual indent
./bag/views.py:60:80: E501 line too long (97 > 79 characters)
./bag/views.py:63:80: E501 line too long (85 > 79 characters)
./bag/views.py:85:9: E265 block comment should start with '# '
./bag/views.py:91:25: E128 continuation line under-indented for visual indent
./bag/views.py:91:80: E501 line too long (83 > 79 characters)
./bag/views.py:92:25: E128 continuation line under-indented for visual indent
./bag/views.py:100:25: E128 continuation line under-indented for visual indent
./bag/views.py:100:80: E501 line too long (83 > 79 characters)
./bag/views.py:101:25: E128 continuation line under-indented for visual indent
./bag/views.py:105:22: E225 missing whitespace around operator
./bag/views.py:109:80: E501 line too long (97 > 79 characters)
./bag/views.py:112:80: E501 line too long (80 > 79 characters)
./bag/views.py:143:25: E128 continuation line under-indented for visual indent
./bag/views.py:143:80: E501 line too long (83 > 79 characters)
./bag/views.py:144:25: E128 continuation line under-indented for visual indent
./bag/views.py:150:80: E501 line too long (80 > 79 characters)
./bag/views.py:157:41: W292 no newline at end of file
./bag/urls.py:9:2: W292 no newline at end of file
./bag/templatetags/bag_tools.py:6:1: E302 expected 2 blank lines, found 1
./bag/templatetags/bag_tools.py:8:28: W292 no newline at end of file
./profiles/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./profiles/models.py:15:80: E501 line too long (81 > 79 characters)
./profiles/models.py:16:80: E501 line too long (84 > 79 characters)
./profiles/models.py:17:80: E501 line too long (84 > 79 characters)
./profiles/models.py:18:80: E501 line too long (81 > 79 characters)
./profiles/models.py:21:80: E501 line too long (80 > 79 characters)
./profiles/models.py:35:32: W292 no newline at end of file
./profiles/admin.py:1:1: F401 'django.contrib.admin' imported but unused
./profiles/forms.py:33:80: E501 line too long (98 > 79 characters)
./profiles/forms.py:34:45: W292 no newline at end of file
./products/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./products/models.py:8:1: W293 blank line contains whitespace
./products/models.py:20:80: E501 line too long (94 > 79 characters)
./products/models.py:26:80: E501 line too long (87 > 79 characters)
./products/views.py:42:80: E501 line too long (83 > 79 characters)
./products/views.py:45:80: E501 line too long (80 > 79 characters)
./products/views.py:69:68: W292 no newline at end of file
./products/migrations/0001_initial.py:18:80: E501 line too long (117 > 79 characters)
./products/migrations/0001_initial.py:20:80: E501 line too long (91 > 79 characters)
./products/migrations/0001_initial.py:26:80: E501 line too long (117 > 79 characters)
./products/migrations/0001_initial.py:27:80: E501 line too long (81 > 79 characters)
./products/migrations/0001_initial.py:31:80: E501 line too long (103 > 79 characters)
./products/migrations/0001_initial.py:32:80: E501 line too long (87 > 79 characters)
./products/migrations/0001_initial.py:33:80: E501 line too long (82 > 79 characters)
./products/migrations/0001_initial.py:34:80: E501 line too long (141 > 79 characters)
./home/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./home/models.py:1:1: F401 'django.db.models' imported but unused
./home/admin.py:1:1: F401 'django.contrib.admin' imported but unused
./home/urls.py:1:1: F401 'django.contrib.admin' imported but unused
./checkout/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./checkout/__init__.py:1:52: W292 no newline at end of file
./checkout/models.py:16:80: E501 line too long (82 > 79 characters)
./checkout/models.py:27:80: E501 line too long (94 > 79 characters)
./checkout/models.py:28:80: E501 line too long (93 > 79 characters)
./checkout/models.py:29:80: E501 line too long (93 > 79 characters)
./checkout/models.py:31:80: E501 line too long (86 > 79 characters)
./checkout/models.py:44:80: E501 line too long (102 > 79 characters)
./checkout/models.py:46:80: E501 line too long (95 > 79 characters)
./checkout/models.py:66:80: E501 line too long (113 > 79 characters)
./checkout/models.py:67:80: E501 line too long (91 > 79 characters)
./checkout/models.py:71:80: E501 line too long (113 > 79 characters)
./checkout/models.py:82:76: W292 no newline at end of file
./checkout/signals.py:6:1: E302 expected 2 blank lines, found 1
./checkout/signals.py:13:1: E302 expected 2 blank lines, found 1
./checkout/signals.py:18:34: W292 no newline at end of file
./checkout/forms.py:39:45: W292 no newline at end of file
./checkout/views.py:1:80: E501 line too long (87 > 79 characters)
./checkout/views.py:16:1: E302 expected 2 blank lines, found 1
./checkout/views.py:83:80: E501 line too long (88 > 79 characters)
./checkout/views.py:90:80: E501 line too long (83 > 79 characters)
./checkout/views.py:97:80: E501 line too long (80 > 79 characters)
./checkout/views.py:165:46: W292 no newline at end of file
./checkout/urls.py:7:80: E501 line too long (93 > 79 characters)
./checkout/urls.py:8:80: E501 line too long (88 > 79 characters)
./checkout/webhooks.py:10:1: E302 expected 2 blank lines, found 1
./checkout/webhooks.py:25:9: E122 continuation line missing indentation or outdented
./checkout/webhooks.py:27:5: F841 local variable 'e' is assigned to but never used
./checkout/webhooks.py:30:5: F841 local variable 'e' is assigned to but never used
./checkout/webhooks.py:42:80: E501 line too long (86 > 79 characters)
./checkout/webhooks.py:54:20: W292 no newline at end of file
./checkout/apps.py:8:9: F401 'checkout.signals' imported but unused
./checkout/apps.py:8:32: W292 no newline at end of file
./checkout/webhook_handler.py:10:1: E302 expected 2 blank lines, found 1
./checkout/webhook_handler.py:19:19: F821 undefined name 'render_to_string'
./checkout/webhook_handler.py:22:16: F821 undefined name 'render_to_string'
./checkout/webhook_handler.py:24:47: F821 undefined name 'settings'
./checkout/webhook_handler.py:25:1: W293 blank line contains whitespace
./checkout/webhook_handler.py:26:9: F821 undefined name 'send_mail'
./checkout/webhook_handler.py:29:13: F821 undefined name 'settings'
./checkout/webhook_handler.py:31:10: W291 trailing whitespace
./checkout/webhook_handler.py:69:80: E501 line too long (80 > 79 characters)
./checkout/webhook_handler.py:70:80: E501 line too long (80 > 79 characters)
./checkout/webhook_handler.py:100:80: E501 line too long (107 > 79 characters)
./checkout/webhook_handler.py:150:80: E501 line too long (93 > 79 characters)
./checkout/webhook_handler.py:159:24: W292 no newline at end of file
./checkout/migrations/0001_initial.py:28:80: E501 line too long (82 > 79 characters)
./checkout/migrations/0001_initial.py:33:80: E501 line too long (85 > 79 characters)
./checkout/migrations/0001_initial.py:40:80: E501 line too long (85 > 79 characters)
./checkout/migrations/0001_initial.py:44:80: E501 line too long (83 > 79 characters)
./checkout/migrations/0001_initial.py:48:80: E501 line too long (84 > 79 characters)
./checkout/migrations/0001_initial.py:52:80: E501 line too long (84 > 79 characters)
./checkout/migrations/0001_initial.py:79:80: E501 line too long (88 > 79 characters)
./checkout/migrations/0002_order_original_bag_order_stripe_pid_alter_order_id_and_more.py:27:80: E501 line too long (87 > 79 characters)
./checkout/migrations/0002_order_original_bag_order_stripe_pid_alter_order_id_and_more.py:34:80: E501 line too long (87 > 79 characters)

```

