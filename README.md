<h1 align="center">Pizza Heaven - Resturant Booking</h1>

[View the live project here.](https://nikolaycranner.herokuapp.com/)

This is the official page for Nikolay Cranner. It is designed to be responsive and accessible on a range of devices, making it easy to navigate.
The page offers role base authentication, including admin manage privileges for inventory of the store. If a user is not authenticated, it's default user id will be guest. The site have a webstore where customers can purchase music via paypal with the possibility to download the song(s) after successful purchase, and for authenticated users it also offers a profile page where the user can view previous orders and its contents. Login and signup is found in the menu, and for this allauth
is used with email verification as the signup process. Real emails are pushed out to the user tha signs up to the page. NOTE check the spam filter, cause domain priority is not considered in this project ( yet ). The user also have the ability to remove products from shopping bag before purchase. The orders are stored on the postgres server. So that the user can find back to this any time, while logged in. NOTE: if more guest users are trying to shop at the time, the system is not good at handing this at the momen, because the user id will be guest for all users. To be improved in the future.

<h2 align="center">
    <img src="assets/pizza-heaven-responsive.PNG">
</h2>

## User Experience (UX)
-   ### User stories

    -  [Jira User Stories](https://nno24.atlassian.net/jira/software/c/projects/NCO/boards/1?selectedIssue=NCO-10&atlOrigin=eyJpIjoiMWMyZmRlZTdiMjMxNGEyNzhlMmE4NDkyMmRiZmFkNWYiLCJwIjoiaiJ9)

-   ### Design
    -   #### Colour Scheme
        -   The three main colours used are brown, darker brown, black, and white. The css uses the materializecss css library.
    -   #### Typography
        -   Uses the materializecss standard fonts.
    -   #### Imagery
        -   Proprietary Nikolay Cranner images, permission granted for artwork an other

        #### Media
        -  When purchasing a song, it's possible to download a test sample to illustrate functionality.

        #### Social Media
        -  The footer has all social media links with icons making it easy for the user to click
        and follow. There is no added links to these, because this is a fictive site. But the icons are taken 
        from fontawesome cdn. See base.html.
    <h2 id="wireframes"></h2>
-   ### Wireframes/Mockup
-   There are no wireframes for this webpage




## Features

-   Fully interactive booking form, submitting the booking request to the heroku postgresql server. 

-   The booking form has input validation, and has included date and time pickers from the materializecss library.

-   The user will be greeted with a booking confirmation if succesfully added to the database, this page also renders the 
    booking details back to the user.

-   Staff people for the resturant can login to the database to see the bookings, and do changes if necessary. The staff can login
    to django admin by adding "/admin" to the url, and login with user: staff, pass: staff.

-   The about and menu/booking sites is just fictive and illustrative for demonstration purposes only.

-   The navbar is responsive, and uses side-nav functionality from materializecss during resizing to mobile/tablet devices.

<h2 align="center">
    <img src="assets/screenshots/pizza-heaven-booking.PNG">
    <img src="assets/screenshots/pizza-heaven-booking-time.PNG">
</h2>

<h2 align="center">
    <img src="assets/screenshots/pizza-heaven-conf.PNG">
    <img src="assets/screenshots/pizza-heaven-sidenav.PNG">
    <img src="assets/screenshots/booking-admin.PNG">
</h2>


## Features to be added/fixed
-   Set a limit for how many can book in the same time duration at the same date.
    This info must be rendered to the user when before submitting the form.
-   Give the user the possibility to cancel or change their booking from the webpage.
-   Complete the menu/book with some more usable menu content - pizza types etc.
-   Complete the send mail functionality in production environment, this was tested sucecssfully in development.
    This is the functionality that sends the email to the actual client, with the booking confrimation.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/about)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used
1. [django](https://www.djangoproject.com/)
    - Django is a high-level Python fullstack web framework that was used for implementing the MVC.
1. [heroku:](https://dashboard.heroku.com/)
    - Used for production, hosting service for the app with the postgresql
1. [Cloudinary:](https://cloudinary.com/)
    - Cloudinary was used to host the static files, like custom css, javascript and images.
1. [Materializecss:](https://materializecss.com/)
    - Materializecss was used for css and date/time pickers.
1. [Fontawesome:](https://fontawesome.com/)
    - Fontawesome was used for icons in the socials section in the footer
11. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [GitPod:](https://gitpod.io/)
    - GitPod is used as the IDE for the project.
1. [Chrome-DevTools:](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used to test responsiveness on all devices,to inspect html/css, and to debug the application.
1.  [Am I Responsive?](http://ami.responsivedesign.is/)
    - Am I Responsive? was used to create the screenshot of the website for all devices, the first image of the README.



## Testing

No testing was performed in this project. There was a very limited time, but the conceps for implementing a simple fullstack website in django was demonstrated.

## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Signup to heroku
2. Created the appname
3. Added environment variables and heroku postgresql
4. Attached the git repo to heroku, under deploy tab.
5. Deployed from heroku web interface

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/fullstack-toolkit-p4)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/fullstack-toolkit-p4)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/nno24/fullstack-toolkit-p4
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/nno24/fullstack-toolkit-p4
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits
1. Awesome django documentation
2. Stackoverflow at times, and some youtube videos came handy to get django more in the fingers.

### Code

-   The pizza background image came from [Motionarray](https://motionarray.com/) with the right licence to use.


### Content

-   All content was written by the developer.

### Media

- N/A

### Acknowledgements

-   My Mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
