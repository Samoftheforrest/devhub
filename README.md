# DEVHUB

![Devhub cover image](/docs/readme/cover-image.png)

Welcome to Devhub, the online platform for sharing your web development projects!

The goal of this platform is to make sharing your projects with other devs, or finding inspriation from other devs, as simple as possible.

## Table of Contents

- [DEVHUB](#devhub)
  * [Table of Contents](#table-of-contents)
  * [UX/UI](#ux-ui)
    + [User Goals](#user-goals)
    + [User Stories](#user-stories)
    + [Site Owner's Goals](#site-owner-s-goals)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
      - [Requirements](#requirements)
      - [Expectations](#expectations)
    + [Design Choices](#design-choices)
      - [Colours](#colours)
      - [Fonts](#fonts)
      - [Accessibility](#accessibility)
    + [Wireframes](#wireframes)
      - [Desktop](#desktop)
      - [Tablet](#tablet)
      - [Mobile](#mobile)
    + [UX/UI Flowchart](#ux-ui-flowchart)
  * [Features](#features)
    + [Site-wide](#site-wide)
    + [Homepage](#homepage)
    + [Add/edit project page](#add-edit-project-page)
    + [Login, Logout, Registration](#login--logout--registration)
    + [Contact page](#contact-page)
    + [Profile pages](#profile-pages)
    + [Features to be Implemented](#features-to-be-implemented)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Libraries + Frameworks](#libraries---frameworks)
    + [APIs](#apis)
    + [Design](#design)
  * [Testing](#testing)
    + [Test 1 - Site Navigation](#test-1---site-navigation)
      - [User story: '_As a user, I should be able to navigate around the site simply._'](#user-story----as-a-user--i-should-be-able-to-navigate-around-the-site-simply--)
    + [Test 2 - Add Projects](#test-2---add-projects)
      - [User story: '_As a user, I should be able to add my own projects._'](#user-story----as-a-user--i-should-be-able-to-add-my-own-projects--)
    + [Test 3 - Edit projects](#test-3---edit-projects)
      - [User story: '_As a user, I should be able to edit my projects._'](#user-story----as-a-user--i-should-be-able-to-edit-my-projects--)
    + [Test 4 - Log in/out](#test-4---log-in-out)
      - [User story: '_As a user, I should be able to log in/out._'](#user-story----as-a-user--i-should-be-able-to-log-in-out--)
    + [Test 5 - Profile customisation](#test-5---profile-customisation)
      - [User story: '_As a user, I would like to be able to customise my profile._'](#user-story----as-a-user--i-would-like-to-be-able-to-customise-my-profile--)
    + [Test 6 - Contact](#test-6---contact)
      - [User story: '_As a user, I would like to be able to contact the site's creator._'](#user-story----as-a-user--i-would-like-to-be-able-to-contact-the-site-s-creator--)
    + [Test 7 - Responsivity](#test-7---responsivity)
      - [User story: '_As a user, I should be able to access the website on a range of devices (desktop, tablet, mobile)._'](#user-story----as-a-user--i-should-be-able-to-access-the-website-on-a-range-of-devices--desktop--tablet--mobile---)
    + [Test 8 - Personal Profile](#test-8---personal-profile)
      - [User story: '_As a user, I would like to have my own profile, where I can see all of my projects._'](#user-story----as-a-user--i-would-like-to-have-my-own-profile--where-i-can-see-all-of-my-projects--)
  * [Bugs](#bugs)
    + [Project cards different sizes depending on length of description](#project-cards-different-sizes-depending-on-length-of-description)
    + [Contact form not sending emails correctly](#contact-form-not-sending-emails-correctly)
    + [Input text not sanitised on login/registration](#input-text-not-sanitised-on-login-registration)
    + [Profile nav link highlighted when on other users' profiles](#profile-nav-link-highlighted-when-on-other-users--profiles)
    + [Project cards showing static amount of project tags](#project-cards-showing-static-amount-of-project-tags)
  * [Deployment](#deployment)
    + [Local Development](#local-development)
    + [Deployment](#deployment-1)
  * [Credits](#credits)
    + [General Thanks](#general-thanks)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## UX/UI

### User Goals

- Website needs to be visually appealing.
- Ability to post your own projects.
- Ability to comment on others' projects.
- Functionality across various devices (mobile, tablet, desktop, etc.).
- Ability to register, login and logout of the website.

### User Stories
- As a user, I should be able to navigate around the site simply.
- As a user, I should be able to add my own projects.
- As a user, I should be able to edit my projects.
- As a user, I should be able to log in/out.
- As a user, I would like to be able to customise my profile.
- As a user, I would like to be able to contact the site's creator.
- As a user, I would like to be able to comment on projects: both my own, and others.
- As a user, I should be able to access the website on a range of devices (desktop, tablet, mobile).
- As a user, I would like to have my own profile, where I can see all of my projects.

### Site Owner's Goals
- I would like to create a site that allows developers to easily share their projects.
- I would like to create a web page that is visually appealing.
- I would like to create a seemless experience across multiple devices, making it as accessible as possible.
- I would like to make it as easy as possible to allow users to provide feedback about the site - allowing me to make revisions and improve the user experience.

### User Requirements and Expectations

#### Requirements
- Should be visually appealing.
- Should be easily navigable.
- Should be functional on a range of devices.
- Feed of all projects on the site.
- Login/logout functionality.

#### Expectations
- Ability to sign up for the website using a unique username.
- When username and password are entered, the user should log in.
- Certain functionality of the site should only be available when logged in.
- When a new project is added, it should appear as part of the homepage feed.
- When a profile is created, it should be customisable.

### Design Choices

#### Colours
For this project, I used the pre-made ['Enviro'](https://colorhub.vercel.app/select-palette/enviro) colour pallete from [Daniel Cranney](https://twitter.com/danielcranney)'s ['ColorHub'](https://colorhub.vercel.app/). I decided that I wanted green to be the focal brand colour of this project to symbolise growth. Also, I wanted the other colours in the pallete to be more mild shades of black, grey, and white, to make the brand green stand out.

![Devhub's Colour Pallete](/docs/readme/colour-palette.png)

The colours used were:
- `#3CB35A`: This colour was used as the brand colour, used mostly on call to action buttons/links, or anything else that I wanted to focus the user's attention to.
- `#1E293B`: This colour was used as the primary colour for text (on a white background), and to give a contrasting background to some sections - such as the sidebar.
- `#635E79`: This colour was used sparingly either as text decoration or borders - I chose this colour as I felt it is fairly subtle/understated.
- `#FFFFFF`: This colour is used as the primary background colour, and text colour on dark backgrounds.

#### Fonts
I used a pairing of two [Google Fonts](https://fonts.google.com/) - [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat) for titles and [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro?query=source+sans+pro) for regular text - based on the recommendation of [this article on Coral Nodes](https://www.coralnodes.com/best-google-font-combinations/).

#### Accessibility

### Wireframes

#### Desktop
- [Home Screen](static/docs/wireframes/homepage-desktop.png)
- [Project Page](static/docs/wireframes/individual-project-desktop.png)
- [Add/Edit Project](static/docs/wireframes/add-edit-project-desktop.png)
- [Profile Page](static/docs/wireframes/profile-page-desktop.png)
- [Edit Profile](static/docs/wireframes/edit-profile.desktop.png)
- [Login/Register](static/docs/wireframes/login-register-desktop.png)
- [Contact Page](static/docs/wireframes/contact-page-desktop.png)
- [Base Template](static/docs/wireframes/base-template.png)

#### Tablet
- [Home Screen](static/docs/wireframes/homepage-tablet.png)
- [Project Page](static/docs/wireframes/individual-project-tablet.png)
- [Add/Edit Project](static/docs/wireframes/add-edit-project-tablet.png)
- [Profile Page](static/docs/wireframes/profile-page-tablet.png)
- [Edit Profile](static/docs/wireframes/edit-profile.tablet.png)
- [Login/Register](static/docs/wireframes/login-register-tablet.png)
- [Contact Page](static/docs/wireframes/contact-page-tablet.png)
- [Menu](static/docs/wireframes/menu-tablet.png)

#### Mobile
- [Home Screen](static/docs/wireframes/homepage-mobile.png)
- [Project Page](static/docs/wireframes/individual-project-mobile.png)
- [Add/Edit Project](static/docs/wireframes/add-edit-project-mobile.png)
- [Profile Page](static/docs/wireframes/profile-page-mobile.png)
- [Edit Profile](static/docs/wireframes/edit-profile.mobile.png)
- [Login/Register](static/docs/wireframes/login-register-mobile.png)
- [Contact Page](static/docs/wireframes/contact-page-mobile.png)
- [Menu](static/docs/wireframes/menu-mobile.png)

### UX/UI Flowchart

## Features

### Site-wide
**Fixed nav**

On every page on the site, the nav is either fixed to the left-side of the screen (on desktop), or slides in from the left-side of the screen (on mobile and tablet).

![Static nav](/docs/readme/features/fixed-nav.png)

**Nav displays different links dependent on if user if logged in/out**

Depending on whether the user is logged in/out, the main nav will show different links - allowing logged in users to access more features of the website. Additionally, when a user is logged in, it shows the first letter of their username as the link to their profile - I achieved this by using using Jinja's `first` and `upper` filters, e.g.:
- `{{ session.user | first | upper }}`

Logged in version:

![Logged in version of nav](/docs/readme/features/nav-logged-in.png)

Logged out version:

![Logged out version of nav](/docs/readme/features/nav-logged-out.png)

**Current nav link active class**

Depending on which page the user is on, the appropriate nav link will be highlighted to show which page they are on. I achieved this by using a conditional statement within the base template to add the `active` class to the nav link, i.e:
```
    <li>
        <a href="{{ url_for('home_page') }}" class="main-logo {% if request.path=='/home' %} active {% endif %}" data-bs-placement="right" data-bs-toggle="tooltip" title="Home">
            <i class="fa-solid fa-house"></i>
        </a>
    </li>
```

**Update:** I updated the implementation of this feature by simply passing a variable to each page (e.g. 'home' on the homepage) which is set to True; the sidebar partial then checks which page has the true variable, and styles the nav accordingly. I decided to do it this way to make it more readable.

Nav with homepage icon active:

![Home page with active class](/docs/readme/features/nav-home-active.png)

Nav with contact page active:

![Contact page with active class](/docs/readme/features/nav-contact-active.png)

**Form validation**

Form validation has been added to the following pages: login, registration, and contact. If any information has been omitted, or does not meet the requirements of the particular form, it will display an error - and change the styling of - the particular input. I implemented this validation using the default classes provided by Bootstrap.

Successful validation:

![Successful validation](/docs/readme/features/form-validation-success.png)

Unsuccessful validation:

![Unsuccessful validation](/docs/readme/features/form-validation-failed.png)

### Homepage
**Project Cards**

There is a card containing the following information for each project:
- Name
- Creator
- Link to live site
- Link to repository
- Project description
- Project image
- Project tags

![Example of two project cards](/docs/readme/features/homepage-project-cards.png)

If a user is logged in, it will also show edit/delete buttons when the user hovers on the project cards they own and a star next to their username to signify that they own it (which also shows a tooltip saying 'You own this project'). This applies to all projects if you are logged in as the admin.

![Example of edit/delete buttons on project cards](/docs/readme/features/project-card-buttons.png)

![Ownership star on project cards](/docs/readme/features/project-card-star.png)

### Add/edit project page
**Add project**

Users are presented with a short form to complete - once the form is submitted, the information is passed to MongoDB, where it is then used to generate the project cards.

Completed add project form:

![Completed add project form](/docs/readme/features/add-project-form.png)

Outputted project cards:

![Outputted project card](/docs/readme/features/project-card-bordle.png)

**Edit project**

If the user owns a project, or is an admin, they have the option to edit the project - which will bring them to a version of the 'add project' form with all the fields filled out with the project's current information.

Edit project form

![Edit project form](/docs/readme/features/edit-project-form.png)

### Login, Logout, Registration

**Registration form**

Users can fill out a short registration form, consisting of their: first name, last name, username, password and an additional field to confirm that their password

![Registration form](/docs/readme/features/register-form.png)

**Login form**

Once a user has registered for the site - all they have to do to log in is enter their username and password to this form

![Login form](/docs/readme/features/login-form.png)

**Logout**

Once a user is logged in, to log out all they have to do it click the logout link in the nav (which then turns into the login link while there is noone logged in)

![Login/logout link](/docs/readme/features/login-logout-link.png)

### Contact page

**Contact form**

The contact page has a form, that uses [EmailJS](https://www.emailjs.com/) in order to send feedback about the site to my personal email.

Contact form:

![Contact form](/docs/readme/features/contact-form.png)

Sent email:

![Sent email](/docs/readme/features/email.png)

### Profile pages

Once a user has registered, they will have their own profile page - a page that displays the user's username, bio (once it has been created) and all projects created by that use (sorted by newest to oldest).

![Example profile page](/docs/readme/features/profile-page.png)

### Features to be Implemented
- Upvoting/Downvoting: In future iterations of this project, I would like to add up and down arrows to the project cards for (logged in) users to upvote/downvote the projects.
- Sorting project by most popular: Once the upvoting/downvoting feature (above) was implemented, I would like the users to be able to filter the projects on the homepage by popularity, seeing which have the most upvotes.
- Homepage pagination: On the homepage, rather than displaying every single project in a list, I think it would be beneficial to performace to only show a certain number of projects per page.
- Pinned comments on projects: On each individual project page, the creator of the project will have the ability to pin a comment so that it always shows as the top comment. This may be useful for comments from the creator, to inform potential users of any updates, news, etc.
- Searching by project tags: search/filtering functionality could be added that shows all projects with specific tags (i.e. React, SCSS, Python, etc).
- Edit/delete comments: I would like either the user, the owner of the project, or the admin, to be able to edit/delete comments on the project pages.

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

### Libraries + Frameworks
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://www.mongodb.com/)
- [Postgres](https://www.postgresql.org/)

### APIs
- [EmailJS API](https://www.emailjs.com/)

### Design
- [Figma](https://www.figma.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

## Testing

### Test 1 - Site Navigation

#### User story: '_As a user, I should be able to navigate around the site simply._'

Test description

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| I would like the user to have a sidebar nav that is always available, providing them with links to navigate around the site | To do this, I will include a sticky navbar - that is present on each page - with links to the main pages of the site | I will follow each of the available links 3 times each to ensure that they go to the appropriate page | Each of the links led me to the correct page on each attempt - I have deemed this test to be successful |

Demo:

A demonstration of the site's nav can be found [here](https://www.awesomescreenshot.com/video/9327096?key=5749d43e64ba5d7adb06fb872ff3ccf7)

### Test 2 - Add Projects

#### User story: '_As a user, I should be able to add my own projects._'

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| I would like the user to be able to add their own projects - when logged in - by filling out a short form, and uploading an image if they choose to | Within the `add_project` page, I have created a short form for the user to fill out about their project. The data from this form will be sent to MongoDB, and will in turn be used to display their project | I will attempt to fill out the form and upload three separate projects, from three separate accounts | After completing the form, for each of the project, the correct data was displayed on the homepage - I have considered this test a success |

Test 1:

![Bordle test project](/docs/readme/tests/add-project-form-one.png)

Test 2:

![Minefield memory test project](/docs/readme/tests/add-project-form-two.png)

Test 3:

![Devhub test project](/docs/readme/tests/add-project-form-three.png)

Result:

![Uploaded projects](/docs/readme/tests/add-project-cards.png)

### Test 3 - Edit projects

#### User story: '_As a user, I should be able to edit my projects._'

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| Once a logged in user has uploaded their project, I would like them to be able to edit that project by clicking on the project's card, or on the 'edit' button on the project page. The edit button should only be visible to the owner of the project | I have reused the form from the test above, but I have used jinja templating logic to fill out the fields with the current project data. Additionally, I have included jinja logic that only allows the user to see the edit button on the projects where the session['user'] matches with the project owner | I will attempt to edit three projects: one through the project card, one through an individual project page, and one project that is not owned by the currently logged in user. I should be able to edit the first two, but not the last. | All the editted information was outputted as expected - I have deemed this test successful |

Project one before:

![Project one before](/docs/readme/tests/edit-project-one-before.png)

Project one after:

![Project one before](/docs/readme/tests/edit-project-one-after.png)

Project two before:

![Project two before](/docs/readme/tests/edit-project-two-before.png)

Project two after:

![Project two before](/docs/readme/tests/edit-project-two-after.png)

Project three before:

![Project three before](/docs/readme/tests/edit-project-three-before.png)

Project three after:

![Project three before](/docs/readme/tests/edit-project-three-after.png)


### Test 4 - Log in/out

#### User story: '_As a user, I should be able to log in/out._'

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| I would like the user to be able to log in or out of the page (using the same button for both functions) | I will use Flask to handle the POST method's logic (for both log in and out), a Postgresql database to store the usernames and passwords, and session to track whether the user is logged in or not | I will log and out of three separate test accounts, and attempt to log into an account that does not exist: testaccount, samforrest, l.gilbert, doesnotexist | The three users logged in successfully, but when the non-existing user tried to log in, a flash error was displayed |

Successful login:

![Successful login screenshot](/docs/readme/tests/successful-login.png)

Successful logout:

![Successful logout screenshot](/docs/readme/tests/successful-logout.png)

Unsuccessful login:

![Unsuccessful login](/docs/readme/tests/unsuccessful-login.png)

### Test 5 - Profile customisation

#### User story: '_As a user, I would like to be able to customise my profile._'

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| Once a user has created an account - I would like them to be able to share some information about themselves on their personal profile, not only their projects | If the user visits the profile associated with their account, I will include an edit button, which will take them to a form where they can fill out some information about themselves | I will edit the profile of my testing account 'testaccount' three times, and check that each time the edits are displaying as intended | Each time I edited the profile, the correct information was displayed - I have deemed this test successful. |

Testaccount profile before:

![Testaccount profile (before)](/docs/readme/tests/edit-profile-before.png)

Edit one:

![Testaccount profile (before)](/docs/readme/tests/edit-profile-one.png)

Edit two:

![Testaccount profile (before)](/docs/readme/tests/edit-profile-two.png)

Edit three:

![Testaccount profile (before)](/docs/readme/tests/edit-profile-three.png)

### Test 6 - Contact

#### User story: '_As a user, I would like to be able to contact the site's creator._'

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| I would like the user to be able to complete a simple form to send a message to myself with any suggestions or queries that they may have | I will create a simple form and use EmailJS to handle the email functionality | I will complete the form myself three separate times, to see if the email is sent correctly | All three emails were sent to me correctly (see screenshots) - I have deemed this test to be a success |

Test email one:

![Contact form for test email one](/docs/readme/tests/test-email-one.png)

![Test email one received](/docs/readme/tests/test-email-one-received.png)

Test email two:

![Contact form for test email two](/docs/readme/tests/test-email-two.png)

![Test email two received](/docs/readme/tests/test-email-two-received.png)

Test email three:

![Contact form for test email three](/docs/readme/tests/test-email-three.png)

![Test email three received](/docs/readme/tests/test-email-three-received.png)

### Test 7 - Responsivity

#### User story: '_As a user, I should be able to access the website on a range of devices (desktop, tablet, mobile)._'

Test description

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| I would like the site to be aesthetically pleasing regardless of the device the user uses to view the site | To implement this, I will use a combination of Bootstrap classes and media queries to make the pages responsive | I will load each of the pages on one mobile, tablet and desktop device, and assess whether the element are in the correct layout - based on the wireframes for the pages | All of the pages sized in the expected way - I have deemed this test successful |

Homepage (desktop view):

![Homepage (desktop view)](/docs/readme/tests/homepage-desktop.png)

Homepage (tablet view):

![Homepage (desktop view)](/docs/readme/tests/homepage-tablet.png)

Homepage (mobile view):

![Homepage (desktop view)](/docs/readme/tests/homepage-mobile.png)

### Test 8 - Personal Profile

#### User story: '_As a user, I would like to have my own profile, where I can see all of my projects._'

Test description

| Plan | Implementation | Test | Result |
| ---- | -------------- | ---- | ------ |
| Once a user has registered from the site, I would like this to generate a page which shows their name, optional information about the user, and all projects associated with that user | To implement this, I will use jinja templating logic to check the username of the current session user, displaying their username on the profile page and then loop through each project in MongoDB - but only displaying those created by the session user | I will create three different accounts - testaccount, samforrest, and l.gilbert - then I will add a project for each of these accounts. Once this is done, I will login with each of these accounts and navigate to the profile page - ensuring that all the correct information is displaying | All of the accounts I have created are displaying the correct information/projects - I have deemed this test successful. |

Profile one:

![Profile one](/docs/readme/tests/profile-page-one.png)

Profile two:

![Profile two](/docs/readme/tests/profile-page-two.png)

Profile three:

![Profile three](/docs/readme/tests/profile-page-three.png)

## Bugs

### Project cards different sizes depending on length of description
- **Bug**: If the length of the project description was too long (approximately > 450 characters), it would cause the project card to expand, thus no longer aligning with its neighbouring cards (as seen in the picture below).
![Project card bug](/docs/readme/bugs/bug-one.png)
- **Fix**: I had two potential fixes in mind for this bug: either make all cards stretch to the same height using `align-items: stretch`. However, after some research, I found that you can limit the amount of characters via Jinja's `truncate` filter - which I set to 450 characters.
- **Verdict**: If the project's description exceeds 450 characters, it is successfully truncated, stopping the project card from expanding. I have deemed this fix a success.

### Contact form not sending emails correctly
- **Bug**: After refactoring the 'base.html' template, the contact page would return an error when the form was submitted.
![EmailJS bug](/docs/readme/bugs/bug-two.png)
- **Fix**: I found the issue to be that, after the base tempalte refactor, that the email.js script was no longer included on the contact page. I added `{% block scripts %}` back into the base template and the contact form began working again.
- **Verdict**: I have determined this fix to be successful.

### Input text not sanitised on login/registration
- **Bug**: On the login/registration form, the username input was being converted to lowercase - this meant that you could have many usernames that look identical, but with different capitalisation. Additionally, when trying to log in, if a user types their username, but with incorrect capitalisation, they will be denied access.
![Login bug](/docs/readme/bugs/bug-three.png)
- **Fix**: To fix this, I used the sqlalchemy function `func.lower()` to force all text inputs to be converted to lowercase when submitted.
- **Verdict**: After testing five different capitalisations of 'testaccount', and all of them successfully logging in, I have deemed this fix to be successful.

### Profile nav link highlighted when on other users' profiles
- **Bug**: When a logged in user navigates to their own profile via the nav menu, the appropriate nav link is given the 'active' class. However, this nav link is also given the active class when looking at someone else's profile - even though it was intended to only be 'active' when viewing your own.
- **Fix**: To fix this, I added an if statement to the end of the `go_to_profile` funtion within routes.py, to check if the user is logged in. When navigating to your own profile, the render_template has an argument of `profile_active=True` - but when navigating to another user's profile, it has the parameter `home_active=True`
- **Verdict**: The active class is now added to the nav links appropriately - I have determined this fix to be a success.

Profile nav link for logged in user:

![Nav link when visiting your own profile](/docs/readme/bugs/nav-link-user.png)

Nav link when visiting other user's profiles:

![Nav link when visiting another user's profile](/docs/readme/bugs/nav-link-user-2.png)

### Project cards showing static amount of project tags
- **Bug**: The project card, initially, was set to always show 3 project tags. However, after changing the functionality of the add/edit project form, the user was allowed to choose as many tags as they wanted; this would cause a problem if the user chose more - or less - than 3 tags, as it would either display tags with no text content, or so many tabs that they would overflow off the card.
    ![Project tags bug](/docs/readme/bugs/project-tags-bug.png)
- **Fix**: To fix this, I added in the following jinja logic to first check if there were more than three tags for the project. If there were more than three tags, I chose to limit it to three, and if there were less than 3 - or exactly 3 - it would only show the project tags that were there.
    ```
    {% if project.project_tags | length > 3 %}
        {% for i in range(3) %}
            <span class="project-tag">{{ project.project_tags[i] }}</span>
        {% endfor %}
    {% else %}
        {% for tag in project.project_tags %}
            <span class="project-tag">{{ tag }}</span>
        {% endfor %}
    {% endif %}
    ```
- **Verdict**: The correct amount of project tags are consistently showing now - I have deemed this fix a success.

## Deployment

### Local Development

The project can be run locally by completing the following:

1. Clone the project
    - Navigate to the [project repo](https://github.com/Samoftheforrest/devhub)
    - Click the 'code' button (highlighted on the image below) and copy the clone link:
    ![Project repo homepage](/docs/readme/deployment/github-repo.png)
2. Open a terminal and run the following command: `git clone https://www.github.com/samoftheforrest/devhub.git`
![The repository's 'code' panel](/docs/readme/deployment/github-code-window.png)
3. Navigate to, and open, the cloned/downloaded folder in your code editor, through the following steps:
    - File -> open folder
    - Navigate through your file directory to the place where the repo is cloned/downloaded
    - Select 'open folder'
4. Create config variables in the `.env` file (**Important:** make sure you add this file to your `.gitignore`)
  ```
  # flask
  os.environ.setdefault('IP', '0.0.0.0')
  os.environ.setdefault('PORT', '5000')
  os.environ.setdefault('SECRET_KEY', 'Your secret key here**')
  os.environ.setdefault("DEVELOPMENT", "True")

  # mongodb
  os.environ.setdefault('MONGO_URI', '**Your MongoDB uri here**')
  os.environ.setdefault('MONGO_DBNAME', '**Your Mongo Database name**')

  # postgresql - THIS ONE IS REQUIRED FOR THE NEXT STEP
  os.environ.setdefault("DB_URL", "postgresql:///**Your database name**")
  ```
5. Set up your database
  1. run `psql` from the command line
  2. run the command `CREATE DATABASE **Your database name from the previous step**`
  3. run `\c **Your database name**`
  4. finally, run `db.create_all()` - this will create the follow `user` database schema
    ![Database schema](/docs/readme/deployment/database-schema.png)
6. Run a live server using the following command:
    `python3 run.py`

### Deployment

This page is deployed using [Heroku](). Here I will explain how to deploy a project using Heroku.

1. Create a Heroku account.
2. Under 'new' select 'create new app'
    ![New Heroku project](/docs/readme/deployment/new-heroku-project.png)
3. Choose a name and region
    ![Heroku name and region screen](/docs/readme/deployment/heroku-name-and-region.png)
    - **Note:** the name must be unique, and the it is a good idea to set the region to the one closest to you geographically
4. Next, navigate to the 'settings' tab and add all the necessary environment and configuration variables under 'config vars'
    - Note: These config variables will be the ones you set up for flask and mongodb (which can be seen in 'development' above)
    ![Config Variables](/docs/readme/deployment/heroku-config-vars.png)
5. Then, navigate to the 'deploy' tab, this will give you a list of the deployment methods. For this project I decided to use the Heroku CLI - as there was issues with GitHub integration - to do this:
    ![Heroku deployment methods](/docs/readme/deployment/heroku-deployment-methods.png)
    1. Navigate back to your project and open a terminal
    2. Use the command `heroku login -i` to login via the terminal
    3. Enter your email and password
    4. Once you are logged in, use the following commands:
        1. `git add .`: this will stage your changes.
        2. `git commit -m 'commit message'`: this will commit your code, readying it to be pushed up
        3. `git push heroku main`: this will push your code to Heroku - it is worth noting that the `main` in this command may need to be changed to reflect the name of the branch you are pushing.
6. Sit back and let Heroku do the work!
 
## Credits
- [This article](https://medium.com/mkdir-awesome/how-to-change-the-bootstrap-5-tooltip-background-and-arrow-color-67e6c5aea510#:~:text=You%20can%20add%20different%20Bootstrap,the%20data%2Dbs%2Dpalcement%20.&text=By%20aiming%20.,you%20can%20change%20the%20color.) helped me to figure out how to style the Bootstrap tooltips (used in the nav).
- [This Stack Overflow answer](https://stackoverflow.com/questions/33627646/python-flask-template-return-first-150-characters) showed me how to use Jinja's `truncate` filter, to limit the project cards to 450 characters each.
- [This Stack Overflow answer](https://stackoverflow.com/questions/8676455/flask-current-page-in-request-variable) showed me how to apply CSS classes dependent on the page the user is currently on.
- [This Stack Overflow answer](https://stackoverflow.com/questions/16573095/case-insensitive-flask-sqlalchemy-query) demonstrated how to convert Sqlalchemy queries to lowercase.
- [This Stack Overflow thread](https://stackoverflow.com/questions/41542845/how-to-display-file-name-for-custom-styled-input-file-using-jquery) showed me how to display the name of the file being uploaded when using a custom upload button
- Thanks to [favicon.io](https://www.favicon.io) for providing free to use favicons

### General Thanks
- I would like to thank my mentor [Simen](https://github.com/Eventyret) for all of his feedback and support with this project.