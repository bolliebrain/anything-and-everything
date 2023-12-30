# Anything and Everything

The live link can be found here - [Anything and Everything](https://anything-and-everything-be0c15127928.herokuapp.com/)

Anything and Everything is a advertising app for users who wish to post about items they are selling, wish to buy, need help or guidance with or simply to reach out to the community.

The site acts as a area where users can communicate with other users.

![Mockup]

![Colour Palette] ()insert colour Palette here

## **Index - Table of Contents**


- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Deployment](#deployment)

- [Design]
        -[Colour Scheme]
        -[Imagery]
        -[Fonts]
        -[Wireframes]
    *[Agile Methodology]
    *[Data Model]
    *[Testing]
    *[Security Features and Defensive Design]
        -[User Authentication]
        -[Form Validation]
        -[Database Security]
        -[Custom Error Pages]
 
deployment
    *[Forking this repository]
    *[Cloning this repository]
    *[Languages]
    *[Frameworks - Libraries - Programes Used]
    *[Credits]
    *[Acknowledgements]

## **User Experience (UX)**

A Visitor to Anything and Everything would be someone who is likely to want to buy or sell items, might be looking for services such as a plumber or cleaner. Other Visitors would be people wanting to browse to see what is available.

### User Stories

#### EPIC - User Profile
- As a Site User I can register my account so that I can add, edit, delete posts and comment on other peoples posts.
- As a Site User, I can log in or log out of my account so that I can keep my account secure.
- As a Site User I can see my login status so that I know if I'm logged in or out.

#### EPIC - User Navigation
- As a Site User, I can clearly understand the purpose of the site so that I can decide if it meets my needs.
- As a Site User, I can navigate around the site so that I can find content and understand where I am on the site.
- As a Site User, I can view the latest posts.
- As a Site User, I can click on the posts so that I can read the full detail and view other comments left by users.

#### EPIC - Post Management
- As a Site User, I can post anything and everything onto the app through an easy to use interface so that I can share with other users.
- As a Site User, I can edit and delete posts that I have created so that I can easily make changes without having to start over.
- As a Site User, I can view only my posts so that I can quickly see and respond to comments in one location.

#### EPIC - Post Interation
- As a Site User, I can comment on other users posts so that I can interact with them.
- As a Site User, I can edit and delete comments that I have created so that I can easily make changes if I have made a mistake.

#### EPIC - Site Administration
- As a Site Administrator, I can create, read, update and delete posts and comments so that I can manage the app content.

## **Existing Features**

### Header

![header](docs/images/features/navloggedout.png)

**Navigation Bar**

- The navigation bar is present at the top of every page and includes links to sign up or login.
- When the user has logged in, their username appears in which they are able to interact with this.

![header](docs/images/features/navloggedin.png)

- The options to Sign-up or Log in will change to the option to log out once the user has logged in.

### Footer

![header](docs/images/features/footer.png)

- The footer section includes icons for Facebook, Instagram, Email and Twitter.
- There is also a contact detail for the company.
- These links do not work and are fictitious for the purpose of this project.

### Home Page

![header](docs/images/features/homesignedout.png)

- The home page includes a sign-up section which encourages the user to register.
- The sign-up button takes the user to the sign-up page.
- If a user is already signed in the message changes to "Add a Post" and the user is encouraged to create a new post.
- The sign-up button changes to a "Add a Post" button which takes the user to the Add a Post page.

![header](docs/images/features/homesignedin.png)


   *[Features]
        - User Account Pages
        - Post Detail Page
        - Add Post Form
        - Add Comment Form
        - Update Post Form
        - Update Comment Form
        - Delete Post
        - Delete Comment
        - Future Features



## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.
