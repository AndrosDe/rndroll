<h1 align="center"> RND|ROLL </h1>
<h2> Welcome </h2>

<h4> 
  This is the free "TV Guide" for Online RollPlay(RP or RPG) / TableTopRollPlayGames (TTRPG): "RND|Roll".
  <br><br>
  The main purpose is to list upcoming events from content creators of these games and offer some information on the event and even the character in the event.
  <br>
  This way, like with a TV Guide, one can browse through the listed events and can  decide which event to watch.
  <br><br>
  "RND|Roll" offers a number of features to vistiors, authenticated users and game masters.
  <br>
  You will have different ways to search for an event and be able to open every event for more details.
  <br> 
  Once you registered, you can create Events to be displayed. If want more than just watch, you can create a character to join an event. You can also create a profile to tell interesed people a little bit about you.
  <br>
  All your created events and characters will be attached to your profile. So when someone enjoys your events or your characters, they can see in what other events you played.
  <br><br>
  The "RND|Roll"-Team wishes all of you teh best and hope that you will have fun on our blog /  "TTRPG -TV Guide".
<h4>

<h2 align="center"><img src="#" height="500" width="900"></h2>

[View the live project here](https://rndroll.herokuapp.com/)
<br>
<small>This link might change in the future due to changes by heroku, we will keep you updated on this</small>

<hr>

<h2> Table of content </h2>

- ### [User Experience (UX)](#user-experience-ux-1)
  - [Customer Focus](#customer-focus)
  - [Design](#design)
  - [Flowchard](#flowchard)
- ### [Features](#features-1)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- ### [Technologies Used](#technologies-used-1)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- ### [Testing](#testing-1)
  - [Testing the User Experience (UX)](#user-experience-ux)
  - [Further Testing](#further-testing)
  - [Known Bugs](#known-bugs)
  - [Fixed Bugs](#fixed-bugs)
- ### [Deployment](#deployment-1)
  - [Heroku](#heroku)
- ### [Credits](#credits-1)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

<hr>

## User Experience (UX) 

## Strategy
- ### Project Goals
* The website should offer an overview of upcoming shows with a small discription (similar to a TV-Guide)
* Every show can be opened for more details
* The side is responsive and can be displayed on mobile and desktop devices
* Guest users will be able to view, find and open shows for more detail, even without having their own account
* Present the available information in a user friendly way
* Provide users the option to register and create an account
* Registered users will be able to create and join shows
* Registered users will be able to create a profile to review and manage their created shows and characters
* Provide registered users (player) access to full CRUD functionality
* Provide registered users (Game Master) access to a full CRUD functionality and Upade functionality for other events
* Provide registered users (Administrator / User designated as "staff") access to a complete CRUD functionality over everything
* Provide staff access to a admin dashboard with full access for any user designated as a staff member
* Include defensive programming to enable users to make an informed decision when deleting shows
* Handle any errors to help the users understand the issue

- ### User Demographic
* Anyone who is able to coduct themselves in a honest, respectful and mature manner
* Visitors who are interesed in D&D, Pen and Paper, TTRPG and similar games
* Visitors who are looking entertainment
* Registered users who want to share their shows/ game sessions to attract more viewers
* Registered users who want to join in an open show


- ### User Stories
- #### Visitor Goals - As a user who has not created an account, I want to be able to:
* Quickly understand the main purpose and use of the application, RND|Roll, and how to use it
* Search for specific shows or view details on any show, by title, owner or catergory
* Register/ create a user account

- #### Registered User Goals - As a user who has an account, I want to be able to:
* Learn more about what I can do on RND|Roll 
* Create, Update and Review my own shows / events
* Categorise my shows
* Upload Images for my shows
* Create a new Category
* Have player able to join my show
* Have like and comment my shows / events
* Have access to tools I may need in order to add, update or delete shows / events
* Be able to add additional information about my show
* Remove any player joined in my own event
* Create, Update, Review and Delete my own characters
* The Deleteion of shows (but be only be possible in emergencies)
* Be forewarned of the consequences of what I am about to do on the App, when approriate and final, such as deleting characters
* Have my own user profile to update my settings and profile information and have all my shows and characters displayed
* Request a promotion to Game Master
* Send a message to Game Masters and staff, if extraordnary actions have to be taken

- #### Registered User Goals - As a user who has an upgraded account (Game Master), I want to be able to:
* Add, edit and delete my own shows / events
* Create, Update, Review and Delete my own characters
* Upade all shows / events, in case some quick updates are needed and the owner is not availble
* Change the Owner of shows / events, in case the owner is no longer able to do the shows / events<br>As an alternative to deleteing shows / events
* remove any player joined in any event

- #### Site Admin Goals - As a staff member / administrator, I want to be able to:
* Have the ability to maintain RND|Roll, in particular the shows / events, categories, character
* Add, edit and delete my own shows / events
* Create, Update, Review and Delete my own characters
* Create, Update, Review and Delete any user created content on RND|Roll
* Promote Users to Game Master
* Promote Users to staff member

<hr>

## Scope
- ### Feature Ideas Planning
When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | View, Create, Edit and Delete shows / events | 5 | 5 |
| 2 | Display upcoming shows / events | 5 | 5 |
| 3 | Create, Edit and Delete Account | 5 | 5 |
| 4 | Login and Logout to Account | 5 | 5 |
| 5 | Game Master Accounts and being able to be promoted to one | 5 | 5 |
| 6 | Create, Edit and Delete Profile | 5 | 5 |
| 7 | Add Categories | 5 | 5 |
| 8 | Search shows / events by Category | 5 | 4 |
| 9 | View, Create, Edit and Delete Characters | 5 | 4 |
| 10 | View, Create, Edit and Delete shows / events with minimal information | 4 | 3 |
| 11 | View, Create, Edit and Delete Characters with minimal information | 3 | 3 |
| 12 | Create, Edit and Delete Profile with minimal information | 3 | 2 |
| 13 | Join shows / events with a character | 5 | 4 |
| 14 | Add / Delete further Categories | 2 | 2 |
| 15 | Search for Categories by title and owner | 4 | 4 |
| 16 | Have the Profile display all owned and narraed shows / events  | 5 | 4 |
| 17 | Have the Profile display all created characters  | 5 | 4 |
| 18 | Have characters detail pages | 3 | 2 |
| 19 | Be able to add notes, information on items and equipment on characters detail pages | 1 | 2 |
| 20 | Picture galary for characters | 1 | 1 |
| 21 | Calendar with the show being displayed | 4 | 2 |
| 22 | Game Master Promtion | 5 | 4 |
| 23 | Group Chat on shows / events | 5 | 4 |
| 24 | Automatic removal of expired shows / events from the main view | 5 | 4 |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement most Features, with the exception of 20, 21, 23, 24 as their implemtation proved more challeging as expected. By reviewing the importance of these features in light of the already implemented ones, I decided to park them for the time being and may add them in the future.

- ### Functionality Requirements
* Clean and themed presentation of shows / events details
* Clean and themed presentation of character details
* Clean and themed presentation of profile details
* Intuitive App navigation
* Use of placeholder images in case the user did not upload their own
* creation of shows / events, character and profile with minimal requirements
* Full CRUD functionality
* Use of Defensive Programming to Safeguard Logged In Users (Members and Superadmin) about any unintended result of their actions, if these actions are final
* Robust error handling provide information

<hr>

## Structure
- ### Topology Diagrams
  The green elements in these diagrams illustrate the pages that are accessible to the user.<br>
  The grey elements in these diagrams are the pages not accessible to a particular user.<br>
  The difference of acces between game master and normal user, is that a normal user can update their own created shows / events game master can update all shows / events.<br>
  The add, edit and delete elements are only available to logged in users. The delete functions will return to:
  - A REGISTERED USER DELETING A HIS OR HER OWN CHARACTER WILL RETURN TO THE INDEX PAGE
  - A STAFF MEMEBER CAN DELETE, UPDATE EVENTS FROM THE INDEX PAGE,<br> ANY DELETION HAPPENING OUTSIDE THE ADMINISTRATION PANEL WILL REDIRECT TO THE INDEX PAGE

  - #### Guest User
  ![GUEST USER JOURNEY ACROSS RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_noaccount_mclbcv.png)

  - #### Registered User
  ![REGISTERED USER'S JOURNEY ACROSS RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_account_k0wcrx.png)

  - #### Administrator / Staff Memeber
  ![STAFF MEMBER'S PERMISSION AND ACCESS ACROSS RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_admin_vldyav.png)

### Database Schema and Structure
RND|Roll uses PostgreSQL and was created with Django+sqlparse.

During the development of the Application, and prior to project submission, the Entity Relationship Diagram (ERD) below went through several iterations to adapt to the challenges encountered during development to better adabt to the features that were implemented or discarded. [The first version can be found here, back when it was callen "en-roll".](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247025/media/images/README%20IMAGES/enroll_database_qzu0ym.png)
The current version can be seen below:

![POSTGRES DATABASES SCHEMA](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663323848/media/images/README%20IMAGES/rndroll_database_j2ekw4.png)

<hr>

## Skeleton
- ### Wireframes
The wireframes created for this project:
- [Base Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_base_tastjb.png)
- [Index Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_index_jhw0x9.png)
- [Event Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_event_ew3a4r.png)
- [Event Create Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_event_create_lwazwo.png)
- [Event Edit Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_event_edit_gonhij.png)
- [Conduct Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_conduct_icybm8.png)
- [Login Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_login_u4npc8.png)
- [Register Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_signup_en937r.png)
- [Profile Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326117/media/images/README%20IMAGES/rndroll_webpages_profile_xql1iz.png)
- [Character Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_character_hwengy.png)
- [Character Create Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_character_create_otehld.png)
- [Equipment Edit Page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663326116/media/images/README%20IMAGES/rndroll_webpages_character_edit_ycci2e.png)

For all other pages did not have any wireframes and are either direct copies of exsiting pages, like "Index Page" is for the "Search Results" and "Tagged Events Search Results".
All other pages are coies of the "Login Page".

### Design
[Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used and customised for the front-end development.


#### Typography
I used Google Fonts to import the fonts I used across the application.

#### Imagery & UI
The colour scheme and typography used for RND|Roll was inspired by the [Django3blog](https://github.com/Code-Institute-Solutions/Django3blog) from Matt Rudge / Code Institute.

<hr>

## Features
Breakdown of the features and elements implemented for the App.
The CRUD is depiced in the feature with teh following color code:
* <span style="color: green">Green = Create</span>
* White = Read
* <span style="color: orange">Oragne = Update</span>
* <span style="color: red">Red = Delete</span>

  ## Multi Page Elements
  - ## Header
    ![Header of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/header_nkgay4.png)
    - ### General Features of the Navbar
        - Logo
        - Slogan
  <br><br>
    - ### Features of the Navbar for authenticated users 
      - Greeting to the logged in user
  <br>
  - ## Navbar
    - ### <strong>General Features of the Navbar</strong>
      ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_visitor_xftaic.png)
      - Home
      - Conduct
      - Tag
      - Help
      - Register
      - Login
  <br>
    - ### <strong>Features of the Navbar for authenticated users</strong>
      ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_user_oot1dw.png)
      - <span style="color: green">Create Event</span>
      - Profile & Repository / Create Profile (if no profile exsits)
      - Message
  <br><br>
    - ### <strong>Features of the Navbar for game masters</strong>
      ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_gm_wobccu.png)
      - GM-Icon
  <br><br>
    - ### <strong>Features of the Navbar for staff members</strong>
      ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_admin_mqll2r.png)
      - Admin-Icon (With link to the Adminstrator - Django Dashboard)
  <br>
  - ## Footer
    ![Footer of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/footer_c8quce.png)
    - Links to different pages

  ## Home/ Index Page
  - ### <strong>General Features of the Index Page</strong>
    ![Index of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339734/media/images/README%20IMAGES/index_visitor_xn0nu3.png)
    - Lists of all upcoming events (shows only public events)
    - Every list item has a link to the related event
    - Search funktion to search events by Title or Owner
  <br><br>
  - ### <strong>Features of the Index Page for authenticated users</strong>
    ![Index of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339734/media/images/README%20IMAGES/index_user_xqg9sr.png)
    - <span style="color: orange">Update Event option on self created event</span>
  <br><br>
  - ### <strong>Features of the Index Page for game masters</strong>
    ![Index of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_gm_akj8gn.png)
    - <span style="color: orange">Update Event option on all event</span>
  <br><br>
  - ### <strong>Features of the Index Page for staff members</strong>
    ![Index of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_admin_bzqhhs.png)
    - <span style="color: orange">Update Event option on all event</span>
    - <span style="color: red">Delete Event option on all event</span>

  ## Events
  - ### <strong>General Feature of the Event</strong>
    ![Event of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_visitor_oyfdj1.png)
    - Section 1 - All Provided information and media form the event creation:
      - Title
      - Picture ( If no picture was uploaded yet a default picture is displayed)
      - Story
      - "Watch Us Here" Button -> uses the provided main link to the event in a new tab
      - Shoutouts
      - Other links
      - Start Date
      - Max. Players
      - Game Master
      - Event Owner
    - Section 2 - Characters:
      - Shows all the characters that have joined the Event
      - The character image has a link to the character page
    - Section 3 - Comments:
      - If comments are made they are shown here
  <br><br>
  - ### <strong>Features of the Event for authenticated users (not event owner)</strong>
    ![Event of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_visitor_oyfdj1.png)
    - Section 1:
      - Event Owner is a link to the Profile (if the owner has a profile)
      - <span style="color: orange">Like Button to Like or Unlike the event</span>
      - Join Button to open a list of Users own created characters
      - <span style="color: orange">Add Character to event</span>
    - Section 2:
      - <span style="color: orange">Remove own character</span>
    - Section 3 - Comments:
      - <span style="color: green">Add a comment</span>
  <br><br>
  - ### <strong>Features of the Event for authenticated users (event owner)</strong>
    ![Event of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_owner_roxk6z.png)
    - Section 1:
      - <span style="color: orange">Update Event</span>
      - <span style="color: red">Delete Event</span>
    - Section 2:
      - <span style="color: orange">Remove any character</span>
  <br><br>
  - ### <strong>Features of the Event for game masters</strong>
    ![Event of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_gm_geak0j.png)
    - Section 2:
      - <span style="color: orange">Remove any character</span>
  <br><br>
  - ### <strong>Features of the Event for staff members</strong>
    ![Event of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_admin_l9zdre.png)
    - Section 1:
      - <span style="color: orange">Update Event</span>
      - <span style="color: red">Delete Event</span>
    - Section 2:
      - <span style="color: orange">Remove any character</span>

  ## Conduct
  - ### <strong>General Features of Conduct</strong>
    - Links to the different page section at the top
    - Links to different pages
    - Information and Disclaimer on/for RND|Roll

  ## Tag Index
  - ### <strong>General Features of Tag Index</strong>
    ![Tag of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tag_user_bfupls.png)
    - Option to add a new tag
    - List of all tags
    - tags link to a search result for events with the tag (opens in a new tab)
  <br><br>
  - ### <strong>Features of the Index Page for staff members</strong>
    ![Tag of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352077/media/images/README%20IMAGES/tag_admin_owaxye.png)
    - <span style="color: red">Delete Tag option (Opens a new page)</span>
  <br><br>
  ## Tagged Events
  - ### <strong>General Features of the Tagged Events</strong>
    ![Events of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_user_gsjngh.png)
    - shows all public and expired events that have a certain tag
  <br><br>
  - ### <strong>Features of the Tagged Events for authenticated users</strong>
    ![Events of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_user_gsjngh.png)
    - <span style="color: orange">Update Event option on self created event</span>
  <br><br>
  - ### <strong>Features of the Tagged Events for game masters</strong>
    ![Events of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_gm_ltjblb.png)
    - <span style="color: orange">Update Event option on all event</span>
  <br><br>
  - ### <strong>Features of the Tagged Events for staff members</strong>
    ![Events of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_admin_gcyvv3.png)
    - <span style="color: orange">Update Event option on all event</span>
    - <span style="color: red">Delete Event option on all event</span>
  <br><br>
  ## Delete Tag
  - ### <strong>Features of the Tagged Events for staff members</strong>
    - Option to delete a Tag (will open Admin Dashboard)
  <br><br>
  ## Help
  - ### <strong>General Features of Help</strong>
    - Information on different topics like:
      - creating and managing an event
      - creating and managing a character
      - creating and managing a profile
  <br><br>
  ## Register
  - ### <strong>General Features of Register</strong>
    - <span style="color: green">creates a new account</span>
    - offers advise of password
    - error messages are in a different color
    - offers link to login page 
  <br><br>
  ## Login
  - ### <strong>General Features of Login</strong>
    - offers link to registration page
  <br><br>
  - ### <strong>Features of Login for authenticated users</strong>
    - log into user account
  <br><br>
  ## Messages
  - ### <strong>Features of Messages for authenticated users</strong>
    ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663340653/media/images/README%20IMAGES/navbar_user2_rvhc5d.png)
    - <span style="color: green">Create message for the Game Masters and Administrators</span>
  <br><br>
  ## GM-Badge
  - ### <strong>Features of GM-Badge for game masters</strong>
    ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_gm_wobccu.png)
    - shows that you are a Game Master
  <br><br>
  ## Administrator-Badge
  - ### <strong>Features of Administrator-Badge for staff members</strong>
    ![Navbar of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_admin_mqll2r.png)
    - shows that you are an Administrator
    - links to administrator dashboard (opens in a new tab)
  <br><br>
  ## Create Profile
  - ### <strong>Features of Create Profile for authenticated users</strong>
    - <span style="color: green">creating user profile (minimum requirement: Click "Create Profile")</span>
  <br><br>
  ## Profile & Repository
  - ### <strong>Features of Profile & Repository for authenticated users (not profile owner)</strong>
    ![Profile of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663341279/media/images/README%20IMAGES/profile_visitor_gdxcpl.png)
    - Section 1 - view all provided information and media from the profile creation:
      - username
      - Game Master badge, if profile user is game master
      - profile picture / default picture
      - bio
      - links to profile user websites and social media
    - Section 2 *(hidden)*
    - Section 3 - Owned Events
      - Lists all created events of the profile user
      - Lists *Private Events*
      - Every list item has a link to the related event
    - Section 4 - Narrated Events
      - Lists all narrated / game mastered events of the profile user
      - Lists *Private Events*
      - Every list item has a link to the related event
    - Section 5 - Characters
      - Lists all created characters of the profile user
      - Every list item has a link to the related characters
  <br><br>
  - ### <strong>Features of Profile & Repository for authenticated users (profile owner)</strong>
    ![Profile of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663346670/media/images/README%20IMAGES/profile_gm_owner_oj87hl.png)
    - Section 1 - view all provided information and media from the profile creation:
      - email
      - <span style="color: orange">Request Game Master Promotion / Note the Game Master Promotion Request is pending</span>
      - <span style="color: orange">Edit Profile (update bio, picture, links)</span>
      - <span style="color: orange">Edit Settings (update username, email)</span>
      - <span style="color: orange">Change Password (update password)</span>
    - Section 2 *(hidden)*
    - Section 3 - Owned Events
      - <span style="color: orange">Update Event option on self created event</span>
    - Section 4 - Narrated Events
      - <span style="color: orange">Update Event option on self created event</span>
    - Section 5 - Characters
      - <span style="color: green">Create a new Character</span>
  <br><br>
  - ### <strong>Features of the Profile & Repository for game masters</strong>
    ![Profile of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663341279/media/images/README%20IMAGES/profile_gm_ztbbgy.png)
    - Section 1 - view all provided information and media from the profile creation:
      - no email
    - Section 2 - Messages
      - User messages
    - Section 3 - Owned Events
      - <span style="color: orange">Update Event option</span>
    - Section 4 - Narrated Events
      - <span style="color: orange">Update Event option</span>
  <br><br>
    
    <summary><h4><strong>Features of Profile & Repository for staff members</strong></h4></summary>
    <details>
      <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663346726/media/images/README%20IMAGES/profile_adminr_gkujwu.png" name="image-name">
    </details>
      <ul>
      <li>
      Section 1 - view all provided information and media from the profile creation:
        <ul>
        <li>
        email
        </li>
        </ul>
      </li>
      <li>
      Section 2 - Messages
        <ul>
        <li>
        User messages
        </li>
        <li>
        GM Promotion Requests
        </li>
        </ul>
      </li>
      <li>
      Section 3 - Owned Events
        <ul>
        <li>
        <span style="color: orange">Update Event option</span>
        </li>
        <li>
        <span style="color: red">Delete Event option</span>
        </li>
        </ul>
      </li>
      <li>
      Section 4 - Narrated Events
        <ul>
        <li>
        <span style="color: orange">Update Event option</span>
        </li>
        <li>
        <span style="color: red">Delete Event option</span>
        </li>
        </ul>
      </li>
      </ul>

  <br><br>
  ## Character
  - ### <strong>General Features of Character</strong>
    ![Character of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_user_zgdd37.png)
    - Section 1 - view all provided information and media from the character creation:
      - name
      - class
      - image
      - background
      - character creator
      - show equipment
    - Section 2 - Items
      - items
    - Section 3 - Notes
      - notes
    - Section 4 - Joined Events
      - Lists all events the character has joined
      - Lists *Private Events*
      - Every list item has a link to the related event
  <br><br>
  - ### <strong>Features of Character for authenticated users (not character creator)</strong>
    - Section 4 - Joined Events
      - <span style="color: orange">Update Event option on self created event</span>
  <br><br>
  - ### <strong>Features of Character for authenticated users (character creator)</strong>
    ![Character of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_owner_x7n9gg.png)
    - Section 1 - view all provided information and media from the character creation:
      - <span style="color: orange">Update Character</span>
      - <span style="color: red"> Delete Character</span>
      - <span style="color: orange">update equipmment</span>
    - Section 2 - Items
      - update items
    - Section 3 - Notes
      - <span style="color: red"> Delete Note</span>
      - <span style="color: green">Create New Note</span>
  <br><br>
  - ### <strong>Features of Character for game masters</strong>
    ![Character of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_gm_eqnml8.png)
    - Section 1 - view all provided information and media from the character creation:
      - <span style="color: orange">Update character</span>
    - Section 4 - Joined Events
      - <span style="color: orange">Update Event option</span>
  <br><br>
  - ### <strong>Features of Character for staff members</strong>
    ![Character of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_admin_c9mm2s.png)
    - Section 1 - view all provided information and media from the character creation:
      - <span style="color: orange">Update character</span>
      - <span style="color: red">Delete character</span>
    - Section 4 - Joined Events
      - <span style="color: orange">Update Event option</span>
      - <span style="color: red">Delete Event option </span>


<br>

## Defensive Programming
To keep the application secure and protected any feature that is not read only requires the user to be logged in.
Further is any deletion feature restriced to the creator user or administrator.
<br>
The update function is avalible to creator or administrator and a special group of users.
To be promoted to this group requires an administrator to manually set a flag in the user profile.
<br>
Event entering the webside manualy to circumvent the restricons placed on the links on the page, will end in a custom error note, explaining why the content is not displayed.
<br>

<hr>

## Technologies Used
* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back end programming of the site.

<br>

* [Cloudinary API](https://cloudinary.com/) 
    * was used to enable users to upload images for their recipes whilst keeping the App safe and secure

* [Django](https://www.djangoproject.com/)
    * Django was used to create the models for the database, forms to post data into the database, the templates and the view connecting them all together.

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used to store user registration, login and authentication. Postgres was also used to store the Categories.

* [Django Summernote](https://www.mongodb.com/)
    * MongoDB was the nonrelational database used to store less structured data such as the recipes. MongoDB is where we host our NoSQL database.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [gunicorn](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project.

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open source toolkit and was used for ease of styling the Earthlings app.

* [Brave](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Lunapic](https://www9.lunapic.com/editor/)
    * Lunapic was used to work with images: Background removal, scale, etc.

* [Grammarly:](https://app.grammarly.com/)
    * Grammarly was used for spell checking.

* [Notepad++:](https://notepad-plus-plus.org/)
    * Notepad++ for keeping notes for the project.

* [WEBP Converter:](https://www.onlineconverter.com/webp)
    * WEBP Converter was used to change *.jpg files to *.webp to reduce the size.

* [tinypng:](https://tinypng.com/)
    * Tinypng was used to reduce the file size of pictures.

### Future Implementation
* Reset Password Function
* Group Chat on Events for Event owner and joined players
* Item Model with pictures, etc. and changing equipment fields on character to ForeignKeys
* Delete comments
* Delete own user account
* login with social media
* bad name list

<hr>

## Testing
### All testing undertaken for this project can be found in the [Testing Document](/TESTING.md)
<br>
<hr>

## Bugs, Issues and Solutions
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | CSS not loading in heroku deployment | Set "Debug = False" in settings.py before commiting you lated version to github
| 2 | CSS or Summernote issues when running the server in gitpod with "python3 manage.py runserver" | Set "Debug = True" in settings.py
| 3 | Linking to profile causes error if user is not logged in or has no profile | Use {% if user.profile.id  %} to only offer the link to a profile if a profile exsits.
| 4 | Image does not upload in form | Make sure to add 'enctype="multipart/form-data"' form attributes"
| 5 | Image, Videos and links can not be added to Text Rich-Field of Summernote | You may need to add "SUMMERNOTE_THEME = 'bs4'" into settings.py, as it sometmes does not accept bootstrap 5 or other settings.
<br>
<hr>

## Deployment & Local Development

### Deployment to Heroku

The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:
  
1. **Log in to Heroku** or create an account if required.
1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I used the same name as the GitHub repository (empty-the-array) for this project.
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Germany.
1.  When you are happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.

1. This will bring you to the project "Deploy" tab. From here, go to **resources** and select **Heroku Postgres** on the **Add-ons** section.

1. Then navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** add the following keys and values:

    | Key | Value |
    | :---: | :---: |
    | DATABASE_URL | postgresql |
    | SECRET_KEY | mysecretkey |
    | CLOUD_NAME | mycloudinaryname  |

1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by following one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.


### Local Development
* How to Fork To fork the repository, use the following steps:
Login or signup to Github and locate the repository.
Click the Fork button in the top right corner

### Making Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/AndrosDe/rndroll
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/AndrosDe/rndroll
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

<hr>

## Credits
### Code
* This project was havely inflancend by "I Think Therefore I Blog"-Project from Code Institute / Matt Rudge and even some the HTML and CSS code were as basis for my own project
* Additionally I found a lot of help with some feature (like the connecting the profile ) from John Elder's Youtube series on Django [Create A Simple Blog With Python and Django](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
### Media
All used picture a free use, changed / modified or allow non profit usage and mostly only used for testing purposes.

### Resources
README was strongly influanced by Joy Zadan and her awesome project [PALEO RECIPES](https://github.com/JoyZadan/paleo-recipes)

<hr>

## Acknowledgements
* Big Thank you to Matt Rudge, as the "I Think Therefore I Blog"-Project helped me to get the project rolling.
* Thank you to John Elder for offering the basic walk through of Django.
* Special mention and thanks to my mentor, Dario Carrasquel, for his support and insights, as it made obvious to me that all the stuff I think are obvious and self-explanatory, are not obvious and self-explanatory at all.

<hr>

## Copyrights
&copy; 2022 RND|Roll by Andreas Beier