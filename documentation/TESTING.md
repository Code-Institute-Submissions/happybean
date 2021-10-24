# Happy Bean Website - Testing details

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

## **Test User Stories Test Images**
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

### User story images
<details>
<summary>Home</summary>

![Home](/documentation/images/general_doc_img/landing_home_page.png)
</details>

<details>
<summary>Footer</summary>

![Footer](/documentation/images/general_doc_img/footer.png)
</details>

<details>
<summary>Shop: Product filter, sort and search</summary>

![Shop: Products](/documentation/images/general_doc_img/product_filter_sort_search.png)
</details>

<details>
<summary>Shop: Pagination</summary>

![Shop: Pagination](/documentation/images/general_doc_img/products_view_pagination.png)
</details>

<details>
<summary>Product detail</summary>

![Product detail](/documentation/images/general_doc_img/product_detail.png)
</details>

<details>
<summary>Cart: Empty</summary>

![Cart: Empty](/documentation/images/general_doc_img/cart_app_empty.png)
</details>

<details>
<summary>Cart: With Products</summary>

![Cart: With Products](/documentation/images/general_doc_img/cart_app_products.png)
</details>

<details>
<summary>Checkout</summary>

![Checkout](/documentation/images/general_doc_img/checkout_app.png)
</details>

<details>
<summary>Checkout Success</summary>

![Checkout Success](/documentation/images/general_doc_img/checkout_success.png)
</details>

<details>
<summary>Profile</summary>

![Profile](/documentation/images/general_doc_img/profile_app.png)
</details>

<details>
<summary>Coffee Corner</summary>

![Coffee Corner](/documentation/images/general_doc_img/coffee_corner.png)
</details>

<details>
<summary>About App</summary>

![About App](/documentation/images/general_doc_img/about_app.png)
</details>

<details>
<summary>Contact Us</summary>

![Contact Us](/documentation/images/general_doc_img/contact_us.png)
</details>

<details>
<summary>FAQ</summary>

![FAQ](/documentation/images/general_doc_img/faq.png)
</details>

<details>
<summary>Coffee Forum</summary>

![Coffee Forum](/documentation/images/general_doc_img/coffee_forum_app.png)
</details>

<details>
<summary>Coffee Forum: Thread & Comments</summary>

![Coffee Forum: Thread & Comments](/documentation/images/general_doc_img/threads_comments_forum_app.png)
</details>

<details>
<summary>Login</summary>

![Login](/documentation/images/general_doc_img/login.png)
</details>

<details>
<summary>Register</summary>

![Login](/documentation/images/general_doc_img/register.png)
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
- All issues were resolved except the below:
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored.

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CSS code of the project pasting code in by direct input method.
- All issues were resolved.


<br>

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- All issues were resolved except for 2 errors relating to Django crispy forms (see image below for more detail)
<details>
<summary>Checklist for checking all HTMl pages</summary>

![Checklist for checking all HTMl pages](/documentation/images/general_doc_img/html_validator.png)
</details>
<br>
    
### [Python: PEP8 Online](http://pep8online.com/)

- To validate the Python code of the project to check if it is PEP8 compliant. It was done by pasting code on the site by the direct input method.
- I have resolved the Pylint issues as far as I can, there are still a few warnings, but because it is close to submission I will not edit those as it might break something in the app. Also, I kept a few empty python files such as models.py in the about and coffee corner apps, because I could use them later for future development.

<br>

### Lighthouse (Google dev tool)
- To test the accessibility and performance of the website. 
- After testing the site on Lighthouse, there were minor changes that needed to be made, for example, some buttons did not have aria labels, which was added. Another aspect that was fixed was link text styling, the colour needed to be changed to make it more accessible. Lastly, some heading tags were not in order, which was changed as well. 
- After the above changes were made, the overall performance and accessibility have increased. 
- Additional future changes can be made in optimising images in next-generation formats.

<br>

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
- Note: Email verification message - The allauth template was amended as well as the admin dashboard site settings to reflect Happy bean in the email subject line but it still refers to "example.com" in the email the user receives when they sign up. This could be further investigated in the future but because of time constraints, this could not be solved.
<br>
<hr>

## **Bugs and Fixes**
<details>
<summary>Development Phase: Bugs & Fixes</summary>

![Development Phase: Bugs & Fixes](/documentation/images/general_doc_img/bugs_fixes_development.png)
</details>

<details>
<summary>Deployment Phase: Bugs & Fixes</summary>

![Deployment Phase: Bugs & Fixes](/documentation/images/general_doc_img/bugs_fixes_deployment.png)
</details>

<br>
<hr>

## **Further testing**
- Usability tests were done with two users to analyse the User Experience. The feedback from the users was very helpful to determine what works, what can be improved and determine future features.  
- Asked fellow students, friends and family to look at the site on their devices and report any issues they find.
- Review all functionality and responsiveness on different desktop browsers and the website displayed correctly in all browsers including Safari, Chrome, Edge, Firefox and Opera browsers. (see Browser Compatibility section for detail)

<br>
<hr>

## **Deployment**
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable is set to False.
- Confirmed that there is no difference between the deployed version and the development version.


<br>
<hr>
