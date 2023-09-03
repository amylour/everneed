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
- UnboundLocalError:Local variable 'categories' referenced before assignment & navbar active item styling. 'All' products option not displaying due to category = None when it was necessary for it to be categories. Changed to categories = [] to initialize as empty list and added 'not request.GET.category' to 'all' nav-item li tag to remove bold styling when other product categories selected. Fix credit -> Stackoverflow <https://tinyurl.com/26a5ksrd> & CareerKarma <https://tinyurl.com/yc847kb7>. Commit -> No.

### Unresolved/Known Bugs