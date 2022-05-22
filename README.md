# DevHub

Welcome to Devhub, the online platform for sharing your web development projects!

The goal of this platform is to make sharing your projects with other devs, or finding inspriation from other devs, as simple as possible.

**User credentials**
To use the website, you may either create your own account, or use the following test user credentials:
- Username: testaccount
- Password: test123

## Table of Contents

## UX/UI

### User Goals

### User Stories

### Site Owner's Goals

### User Requirements and Expectations

#### Requirements

#### Expectations

### Design Choices

#### Colours
For this project, I used the pre-made ['Enviro'](https://colorhub.vercel.app/select-palette/enviro) colour pallete from [Daniel Cranney](https://twitter.com/danielcranney)'s ['ColorHub'](https://colorhub.vercel.app/). I decided that I wanted green to be the focal brand colour of this project to symbolise growth. Also, I wanted the other colours in the pallete to be more mild shades of black, grey, and white, to make the brand green stand out.

![Devhub's Colour Pallete](static/docs/readme/colour-palette.png)

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

### Existing Features

#### Site-wide
**Fixed nav**
On every page on the site, the nav is either fixed to the left-side of the screen (on desktop), or slides in from the left-side of the screen (on mobile and tablet).

![Static nav](/static/docs/readme/features/fixed-nav.png)

**Nav displays different links dependent on if user if logged in/out**
Depending on whether the user is logged in/out, the main nav will show different links - allowing logged in users to access more features of the website. Additionally, when a user is logged in, it shows the first letter of their username as the link to their profile - I achieved this by using using Jinja's `first` and `upper` filters, e.g.:
- `{{ session.user | first | upper }}`

Logged in version:
![Logged in version of nav](/static/docs/readme/features/nav-logged-in.png)

Logged out version:
![Logged out version of nav](/static/docs/readme/features/nav-logged-out.png)

#### Homepage
**Project Cards**
![Example of two project cards](/static/docs/readme/features/homepage-project-cards.png)
There is a card containing the following information for each project:
    - Name
    - Creator
    - Link to live site
    - Link to repository
    - Project description
    - Project image
    - Project tags

#### 

### Features to be Implemented
- Upvoting/Downvoting: In future iterations of this project, I would like to add up and down arrows to the project cards for (logged in) users to upvote/downvote the projects.
- Sorting project by most popular: Once the upvoting/downvoting feature (above) was implemented, I would like the users to be able to filter the projects on the homepage by popularity, seeing which have the most upvotes.
- Homepage pagination: On the homepage, rather than displaying every single project in a list, I think it would be beneficial to performace to only show a certain number of projects per page.

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

### Design
- [Figma](https://www.figma.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

## Testing

### Test Title

#### Test Description
Add in a table for the Plan, Implementation, Test, Result steps
Add screenshot for each test

## Bugs

### Bug Title

#### Project cards different sizes depending on length of description
- **Bug**: If the length of the project description was too long (approximately > 450 characters), it would cause the project card to expand, thus no longer aligning with its neighbouring cards (as seen in the picture below).
![Project card bug](/static/docs/readme/bugs/bug-one.png)
- **Fix**: I had two potential fixes in mind for this bug: either make all cards stretch to the same height using `align-items: stretch`. However, after some research, I found that you can limit the amount of characters via Jinja's `truncate` filter - which I set to 450 characters.
- **Verdict**: If the project's description exceeds 450 characters, it is successfully truncated, stopping the project card from expanding. I have deemed this fix a success.

#### Bug Description
- **Bug**: 
- **Fix**:
- **Verdict**:

## Deployment

### Local Development

### Deployment

## Credits
- [This article](https://medium.com/mkdir-awesome/how-to-change-the-bootstrap-5-tooltip-background-and-arrow-color-67e6c5aea510#:~:text=You%20can%20add%20different%20Bootstrap,the%20data%2Dbs%2Dpalcement%20.&text=By%20aiming%20.,you%20can%20change%20the%20color.) helped me to figure out how to style the Bootstrap tooltips (used in the nav).
- [This Stack Overflow answer](https://stackoverflow.com/questions/33627646/python-flask-template-return-first-150-characters) showed me how to use Jinja's `truncate` filter, to limit the project cards to 450 characters each.

### General Thanks