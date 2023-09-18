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

### JavaScript Validation

### Python Validation

### CSS Validation

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

### Unresolved/Known Bugs