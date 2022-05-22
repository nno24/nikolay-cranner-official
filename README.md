<h1 align="center">Nikolay Cranner Official</h1>

[View the live project here.](https://nikolaycranner.herokuapp.com/)

This is the official page for Nikolay Cranner. It is designed to be responsive and accessible on a range of devices, making it easy to navigate.
The page offers role base authentication, including admin manage privileges for inventory of the store. If a user is not authenticated, it's default user id will be guest. The site have a webstore where customers can purchase music via paypal with the possibility to download the song(s) after successful purchase, and for authenticated users it also offers a profile page where the user can view previous orders and its contents. Login and signup is found in the menu, and for this allauth
is used with email verification as the signup process. Real emails are pushed out to the user tha signs up to the page. NOTE check the spam filter, cause domain priority is not considered in this project ( yet ). The user also have the ability to remove products from shopping bag before purchase. The orders are stored on the postgres server. So that the user can find back to this any time, while logged in. NOTE: if more guest users are trying to shop at the time, the system is not good at handing this at the moment, because the user id will be guest for all users. To be improved in the future.

It's also possible to signup to the newsletter, and the admin user can push out newsletters to the subscribers from a menu item
only accessible to the admin. Real emails are pushed out. Have not implemented a way to unsubscribe yet.

<h2 align="center">
    <img src="screenshots/iamresp/r-home.png">
    <img src="screenshots/iamresp/r-store.png">
    <img src="screenshots/iamresp/r-store_details.png">
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
        and follow. The icons used are from fontawesome.
    <h2 id="wireframes"></h2>
-   ### Wireframes/Mockup
-   <h2 align="center">
    <img src="screenshots/mockup/home.png">
    <img src="screenshots/mockup/store.png">
    <img src="screenshots/mockup/signup.png">
    <img src="screenshots/mockup/login.png">
    <img src="screenshots/mockup/music.png">
</h2>




## Features

-   Store whre user can purchase music, and get a download oppurtunity after purchase. Checkout with paypal.

-   Role based authentication

-   The admin user can manage the inventory, and crete newsletter when logged in it's accesible from the menu

-   Users can signup of login, and view their order history if logged in

-   Responsive on all devices


## Features to be added/fixed
-   When anonymous user is purchasing products, it's not working good if more anonymous users are shopping at the same time.
    Each anonymous user have the user_id of "guest", and this should be fixed to a unique user id. ( could be done via cookie consent dialouge )
-   The users can not unsubscribe to newsletters
-   Missing cookie consent dialouge
-   Add more products to inventory etc.

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
1. [AWS:](https://aws.amazon.com/)
    - AWS was used to host the static files, like custom css, javascript and media files with S3 buckets.
1. [Materializecss:](https://materializecss.com/)
    - Materializecss was used for css and date/time pickers.
1. [Meta conversion tracking:](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking)
    - Was used for tracking payments, and site activity against meta pixel attached to the facebook business account.  
   <h2 align="center">
        <img src="screenshots/meta/meta-pixel.png">
        <img src="screenshots/meta/meta-pixel-purchase.png">
    </h2>
1. [django-allauth:](https://pypi.org/project/django-allauth/)
    - Was used for login, signup authentication, templates was customised to fit webpage design/style.
1. [PayPal SDK:](https://developer.paypal.com/home)
    - Was used for payments on checkout, see Testing section for details
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

Tested on all devices, and with payment with real paypal/credit cards.
NOTE: For testing purposes with paypal checkout and sandbox, use the following:
user: sb-h8kdy16271303@personal.example.com
pass: Ofkk^(5>


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

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/nikolay-cranner-official)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/nikolay-cranner-official)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/nno24/nikolay-cranner-official
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/nno24/nikolay-cranner-official
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

-   Images and media files are proprietary files from Nikolay Cranner, and have the permission to use.


### Content

-   All content was written by the developer.

### Media

- N/A

### Acknowledgements

-   My Mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
