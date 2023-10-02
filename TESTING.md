# Testing

This is the TESTING file for the [everneed]() website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Score](#wave-accessibility-score)
  - [Automated Testing](#automated-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Testing](#javascript-testing)
  - [Manual Testing](#manual-testing)
    - [User Input](#user-input)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsiveness](#responsiveness)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Unresolved/Known Bugs](#unresolvedknown-bugs)


## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation](docs/testing_images/html_validation.png)  

All HTML pages were validated and received a 'No errors or warning to show' for code that I had written, result as shown above.

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| Log In | 0 | 0 |
| Register | 0 | 0 |
| Account | 0 | 0 |
| Wishlist | 0 | 0 |
| Admin Dashboard | 0 | 0 |
| Add Article |  |  |
| Edit Article |  |  |
| Delete Article |  |  |
| Add Product |  |  |
| Edit Product |  |  |
| Delete Product | 0 | 0 |
| All Products | 0 | 0 |
| Wear| 0 | 0 |
| Care | 0 | 0 |
| Eat | 0 | 0 |
| Travel | 0 | 0 |
| Read | 0 | 0 |
| Forgot Password | 0 | 0 |
| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap, jQuery and Fontawesome purposes were not validated through JSHint.

| Page | Screenshot | Errors | Warnings |
| ---- | ---------- | ------ | -------- |
| base.html | ![js from base.html](docs/g) | none | none |


### Python Validation

### CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files. External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css) was not tested.

![css validation](docs/testing_images/css_valid.png)

| CSS File | Errors | Warnings |
| ---- | ------ | -------- |
| Article | 0 | 0 |
| Checkout | 0 | 0 |
| Admin Products | 0 | 0 |
| Profiles | 0 | 0 |
| Base CSS | 0 | 0 |

### Lighthouse Scores

### Wave Accessibility Score

## Automated Testing

### Python Testing

### JavaScript Testing

## Manual Testing

### User Input

### Browser Compatibility

### Responsiveness

### Testing User Stories

### Dev Tools/Real World Device Testing

## Bugs

- JavaScript dropdown menu fix, moving the mouseleave function outside of the main code seems to fix the 'dropdown menu randomly not appearing on hover' issue. Commit -> No.e27b7a5 This did not fix it, 2nd fix was to update to Bootstrap 4.6 and add 'ease' to menu hover transitions. Currently working consistently. Commit -> No. 2aab065 03/09/2023 - 'pb-2' added to'all' fully fixed it *faceplam*
- UnboundLocalError:Local variable 'categories' referenced before assignment & navbar active item styling. 'All' products option not displaying due to category = None when it was necessary for it to be categories. Changed to categories = [] to initialize as empty list and added 'not request.GET.category' to 'all' nav-item li tag to remove bold styling when other product categories selected. Fix credit -> Stackoverflow <https://tinyurl.com/26a5ksrd> & CareerKarma <https://tinyurl.com/yc847kb7>. Commit -> No.76e8ef8
- Checkout form info not saving to Profile/Account form on checkout success. The 'save_info' section of checkout_success did not save the changed user info to the user's profile. I considered that I may have caused an issue with my Wishlist app signals/contexts but after debugging their was no issue. Debugging with print statements to the terminal showed that the checkout form data was not being saved. I tried several fixes. First was to clear the site data via Dev Tools->Application->Clear Site Data and restart the server. No positive fix. I then backtracked to some earlier commits and removed the 'full_name' field that I had added to my UserProfile models and changed the '_' in checkout.html name='save_info' to name='save-info'. Tested my code with superuser and created a new user to find the issue resolved and no issue with Wishlist app. Fix credit -> Gemma from Tutor Support for helping me to confirm my debugging process was correct and the 'Clear SiteData' tip, and a strong coffee for the second pass at spotting and fixing the bug. Commit no -> 7659ada
- Email Confirmation for order displaying multiple zeros at the end of the totals. Fixed with '|floatformat:2' in confimration_email.txt. Commit -> 

### Unresolved/Known Bugs