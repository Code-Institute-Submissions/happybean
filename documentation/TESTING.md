# The Growth Club Website - Testing details

[Main README.md file](/README.md)

[View live version of website via Heroku](https://happybean.herokuapp.com/)
___
<br>

<a></a>
## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Manual testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)
___
<br>

## **Test User Stories**
Testing user stories from the UX section with corresponding features, styles and content.

<details>
<summary>Guest User</summary>

![Guest User](/documentation/images/general_doc_img/test_user_stories_guest.png)
</details>

<details>
<summary>Registered User</summary>

![Registered User](/documentation/images/general_doc_img/test_user_stories_registered.png)
</details>

<details>
<summary>Admin User</summary>

![Admin User](/documentation/images/general_doc_img/test_user_stories_admin.png)
</details>

<br>
<hr>

## **Testing and Validation**
### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- The report did not have any issues in final testing.
<br>


### [Responsinator](http://www.responsinator.com/)
- To test the responsiveness of the live website and functionalities on different size mobile devices.
- The allauth templates were styled to ensure they are responsive after testing.
- All pages are now responsive.

<br>

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
<details>
<summary>Am I Responsive</summary>

![Am I Responsive](/documentation/images/general_doc_img/mockup.png)
</details>
<br>

### [JavaScript: JSHint](https://jshint.com/)
- JSHint was used to test javascript code in this project. 
- All issues where resolved except the below:
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored. 

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CCS code of the project pasting code in by direct input method.
- All issues where resolved.

<br>

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- All issues where resolved except for 2 errors relating to Django cripspy forms (see image below for more detail)
<details>
<summary>Checklist for checking all HTMl pages</summary>

![Checklist for checking all HTMl pages](/documentation/images/general_doc_img/html_validator.png)
</details>
<br>
    
### Python
- [Extendsclass](https://extendsclass.com/python-tester.html) - No syntax errors
   - [Final Python Validated](#)
- [PEP8 Online](#) - Python file is PEP8 compliant
   - [Final Python Validated](#)

### Google Dev Tool 
- To check for errors in JavaScript code


### Browser Compatibility
To ensure a broad range of users can successfully use this site, I tested it across the 4 major browsers in both desktop and mobile configuration. See the Browser Compatibility Table below for more detail. The following browsers were tested:
- Chrome
- Firefox 
- Safari
- Edge

<details>
<summary>Browser Compatibility detail</summary>

![Browser Compatibility detail](/documentation/images/general_doc_img/browser_compatibility.png)
</details>


<br>
<hr>

## **Manual testing**
<details>
<summary>Manual testing for features</summary>

![Manual testing for features](/documentation/images/general_doc_img/manual_feature_testing.png)
</details>

<br>
<hr>

## **Bugs and Fixes**
<details>
<summary>Development Phase: Bugs & Fixes</summary>

![Development Phase: Bugs & Fixes](/documentation/images/general_doc_img/bugs_fixes_development.png)
</details>

<details>
<summary>Deployment Phase: Bugs & Fixes</summary>

![<summary>Deployment Phase: Bugs & Fixes</summary>
 Phase: Bugs & Fixes](/documentation/images/general_doc_img/bugs_fixes_deployment.png)
</details>
<br>
<hr>

## **Further testing**
- Usability tests were done with two users to analyse the User Experience. The feedback from the users were very helpful to determine what works, what can be improved and determine future features.  
- Asked fellow students, friends and family to look at the site on their devices and report any issues they find.
- Review all functionality and responsiveness on different desktop browsers and the website displayed correctly in all browsers including Safari, Chrome, Edge, Firefox and Opera browsers. (see Browser Compatibility section for detail)

## **Deployment**
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable in app.py file is set to False.
- Confirmed that there is no difference between the deployed version and the development version.


<br>
<hr>
