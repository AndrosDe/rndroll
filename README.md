<h1 align="center"> RND|ROLL </h1>
<h2> Welcome </h2>

<h4> 
  This is the free "TV Guide" for Online RollPlay(RP or RPG) / TableTopRollPlayGames (TTRPG): "RND|Roll".
  <br><br>
  The main purpose is to list upcoming events from content creators of these games and offer some information on the event and even the character in the event.
  <br>
  This way, like with a TV Guide, one can browse through the listed events and can decide which event to watch.
  <br><br>
  "RND|Roll" offers several features to visitors, authenticated users, and game masters.
  <br>
  You will have different ways to search for an event and be able to open every event for more details.
  <br> 
  Once you registered, you can create Events to be displayed. If want more than just to watch, you can create a character to join an event. You can also create a profile to tell interested people a little bit about you.
  <br>
  All your created events and characters will be attached to your profile. So when someone enjoys your events or your characters, they can see what other events you played.
  <br><br>
  The "RND|Roll"-Team wishes all of you the best and hopes that you will have fun on our blog /  "TTRPG -TV Guide".
<h4>

<h2 align="center"><img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663424555/media/images/README%20IMAGES/readme-title-pic_a4yhkr.webp" height="500" width="900"></h2>

[View the live project here](https://rndroll.herokuapp.com/)
<br>
<small>This link might change in the future due to changes by Heroku, we will keep you updated on this</small>

<hr>

<h2> Table of content </h2>

- ### [Strategy)](#strategy-1)
  - [Project Goals](#project-goals)
  - [User Demographic](#user-demographic)
- ### [User Stories](#user-stories-1)
- ### [Scope](#scope-1)
  - [Feature Ideas Planning](#feature-ideas-planning)
  - [Functionality Requirements](#functionality-requirements)
- ### [Structure](#structure-1)
  - [Topology Diagrams](#topology-diagrams)
  - [Database Schema and Structure](#database-schema-and-structure)
- ### [Skeleton](#skeleton-1)
  - [Wireframes](#wireframes)
  - [Design](#design)
- ### [Features](#features-1)
  - [Multi Page Elements](#multi-page-elements)
  - [Home/Index Page](#home-index-page)
  - [Events](#events)
  - [Conduct](#conduct)
  - [Tag Index](#tag-index)
  - [Tagged Events](#tagged-events)
  - [Delete Tag](#delete-tag)
  - [Help](#help)
  - [Register](#register)
  - [Login](#login)
  - [Messages](#messages)
  - [GM-Badge](#gm-badge)
  - [Administrator-Badge](#administrator-badge)
  - [Create Profile](#create-profile)
  - [Profile & Repository](#profile--repository)
  - [Character](#character)
  - [Defensive Programming](#defensive-programming)
  - [Future Implementation](#future-implementation)
- ### [Technologies Used](#technologies-used-1)
- ### [Testing](#testing-1)
- ### [Bugs, Issues, and Solutions](#bugs-issues-and-solutions-1)
- ### [Deployment & Local Development](#deployment--local-development-1)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Local Development](#local-development)
  - [Making Local Clone](#making-local-clone)
- ### [Credits](#credits-1)
  - [Code](#code)
  - [Media](#media)
  - [Resources](#resources)
- ### [Acknowledgements](#acknowledgements-1)
- ### [Copyrights](#copyrights-1)

<hr>

## Strategy
  - ### Project Goals
    * The website should offer an overview of upcoming shows with a small description (similar to a TV Guide)
    * Every show can be opened for more details
    * The side is responsive and can be displayed on mobile and desktop devices
    * Guest users will be able to view, find and open shows for more detail, even without having their account
    * Present the available information in a user-friendly way
    * Provide users the option to register and create an account
    * Registered users will be able to create and join shows
    * Registered users will be able to create a profile to review and manage their created shows and characters
    * Provide registered users (player) access to full CRUD functionality
    * Provide registered users (Game Master) access to a full CRUD functionality and Update functionality for other events
    * Provide registered users (Administrator / User designated as "staff") access to a complete CRUD functionality over everything
    * Provide staff access to an admin dashboard with full access for any user designated as a staff member
    * Include defensive programming to enable users to make an informed decision when deleting shows
    * Handle any errors to help the users understand the issue
    <br><br>
  - ### User Demographic
    * Anyone who can conduct themselves in an honest, respectful, and mature manner
    * Visitors who are interested in D&D, Pen and Paper, TTRPG, and similar games
    * Visitors who are looking for entertainment
    * Registered users who want to share their shows/ game sessions to attract more viewers
    * Registered users who want to join in an open show
    <br><br>

## User Stories
  - ### Visitor Goals - As a user who has not created an account, I want to be able to:
    * Quickly understand the main purpose and use of the application, RND|Roll, and how to use it
    * Search for specific shows or view details on any show, by title, owner, or category
    * Register/ create a user account
    <br><br>
  - ### Registered User Goals - As a user who has an account, I want to be able to:
    * Learn more about what I can do on RND|Roll 
    * Create, Update and Review my own shows/events
    * Categorise my shows
    * Upload Images for my shows
    * Create a new Category
    * Have players able to join my show
    * Have like and comment on my shows/events
    * Have access to tools I may need to add, update or delete shows/events
    * Be able to add additional information about my show
    * Remove any player joined in my event
    * Create, Update, Review and Delete my characters
    * The Deletion of shows (but be only possible in emergencies)
    * Be forewarned of the consequences of what I am about to do on the App when appropriate and final, such as deleting characters
    * Have my user profile to update my settings and profile information and have all my shows and characters displayed
    * Request a promotion to Game Master
    * Send a message to Game Masters and staff, if extraordinary actions have to be taken
    <br><br>
  - ### Registered User Goals - As a user who has an upgraded account (Game Master), I want to be able to:
    * Add, edit and delete my own shows/events
    * Create, Update, Review and Delete my characters
    * Update all shows/events, in case some quick updates are needed and the owner is not available
    * Change the Owner of shows/events, in case the owner is no longer able to do the shows/events <br>As an alternative to deleting shows/events
    * remove any player joined in any event
    <br><br>
  - ### Site Admin Goals - As a staff member/administrator, I want to be able to:
    * Have the ability to maintain RND|Roll, in particular the shows/events, categories, character
    * Add, edit and delete my own shows/events
    * Create, Update, Review and Delete my characters
    * Create, Update, Review and Delete any user-created content on RND|Roll
    * Promote Users to Game Master
    * Promote Users to a staff member
    <br><br>
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
  | 6 | Create, Edit, and Delete Profile | 5 | 5 |
  | 7 | Add Categories | 5 | 5 |
  | 8 | Search shows / events by Category | 5 | 4 |
  | 9 | View, Create, Edit, and Delete Characters | 5 | 4 |
  | 10 | View, Create, Edit, and Delete shows/events with minimal information | 4 | 3 |
  | 11 | View, Create, Edit, and Delete Characters with minimal information | 3 | 3 |
  | 12 | Create, Edit, and Delete Profile with minimal information | 3 | 2 |
  | 13 | Join shows / events with a character | 5 | 4 |
  | 14 | Add / Delete further Categories | 2 | 2 |
  | 15 | Search for Categories by title and owner | 4 | 4 |
  | 16 | Have the Profile display all owned and narrated shows/events | 5 | 4 |
  | 17 | Have the Profile display all created characters  | 5 | 4 |
  | 18 | Have characters detail pages | 3 | 2 |
  | 19 | Be able to add notes, information on items and equipment on characters detail pages | 1 | 2 |
  | 20 | Picture gallery for characters | 1 | 1 |
  | 21 | Calendar with the show being displayed | 4 | 2 |
  | 22 | Game Master Promtion | 5 | 4 |
  | 23 | Group Chat on shows / events | 5 | 4 |
  | 24 | Automatic removal of expired shows/events from the main view | 5 | 4 |

  <br>
  Based on the results of the Feature Ideas Planning, I have decided to attempt to implement most Features, except for 20, 21, 23, and 24 as their implementation proved more challenging than expected. By reviewing the importance of these features in light of the already implemented ones, I decided to park them for the time being and may add them in the future.
  <br><br>

- ### Functionality Requirements
  * Clean and themed presentation of shows/events details
  * Clean and themed presentation of character details
  * Clean and themed presentation of profile details
  * Intuitive App navigation
  * Use of placeholder images in case the user did not upload their own
  * creation of shows/events, characters, and profiles with minimal requirements
  * Full CRUD functionality
  * Use of Defensive Programming to Safeguard Logged In Users (Members and Superadmin) about any unintended result of their actions, if these actions are final
  * Robust error handling provides information
  <br><br>
<hr>

## Structure
- ### Topology Diagrams
  The green elements in these diagrams illustrate the pages that are accessible to the user.<br>
  The grey elements in these diagrams are the pages not accessible to a particular user.<br>
  The difference in access between a game master and a normal user is that a normal user can update their own created shows/events game master can update all shows/events.<br>
  The add, edit and delete elements are only available to logged-in users. The delete functions will return to:
  - A REGISTERED USER DELETING A HIS OR HER CHARACTER WILL RETURN TO THE INDEX PAGE
  - A STAFF MEMBER CAN DELETE, UPDATE EVENTS FROM THE INDEX PAGE,<br> ANY DELETION HAPPENING OUTSIDE THE ADMINISTRATION PANEL WILL REDIRECT TO THE INDEX PAGE
  <br><br>

  <summary><h3><strong>Guest User</strong></h3></summary>
  <details>
    <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_noaccount_mclbcv.png" name="GUEST USER JOURNEY ACROSS RND|ROLL">
  </details>
  <br>

  <summary><h3><strong>Registered User</strong></h3></summary>
  <details>
    <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_account_k0wcrx.png" name="REGISTERED USER'S JOURNEY ACROSS RND|ROLL">
  </details>
  <br>

  <summary><h3><strong>Administrator / Staff Memeber</strong></h3></summary>
  <details>
    <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247333/media/images/README%20IMAGES/enroll_authorisation_admin_vldyav.png" name="STAFF MEMBER'S PERMISSION AND ACCESS ACROSS RND|ROLL">
  </details>
  <br>

- ### Database Schema and Structure
  RND|Roll uses PostgreSQL and was created with Django+sqlparse.

  During the development of the Application, and before project submission, the Entity Relationship Diagram (ERD) below went through several iterations to adapt to the challenges encountered during development to better adapt to the features that were implemented or discarded. [The first version can be found here, back when it was called "en-roll".](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663247025/media/images/README%20IMAGES/enroll_database_qzu0ym.png)
  <br>
  
  <summary><h3><strong>The current version can be seen below in the details.</strong></h3></summary>
  <details>
    <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663323848/media/images/README%20IMAGES/rndroll_database_j2ekw4.png" name="POSTGRES DATABASES SCHEMA of RND|ROLL">
  </details>
  <br>

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

    All other pages did not have any wireframes and are either direct copies of existing pages, like "Index Page" is for the "Search Results" and "Tagged Events Search Results".
    All other pages are copies of the "Login Page".

  - ### Design
    [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used and customized for the front-end development.

    - #### Typography
      I used Google Fonts to import the fonts I used across the application.

    - #### Imagery & UI
      The color scheme and typography used for RND|Roll were inspired by the [Django3blog](https://github.com/Code-Institute-Solutions/Django3blog) from Matt Rudge / Code Institute.
      <br><br>

<hr>

## Features
Breakdown of the features and elements implemented for the App.
The CRUD is depicted in the feature with the following color code:
  <ul>
  <span style="color: green">
  <li>
  Green = Create
  </li>
  </span>
  <li>
  White = Read
  </li>
  <span style="color: orange">
  <li>
  Orange = Update
  </li>
  </span>
  <span style="color: red">
  <li>
  Red = Delete
  </li>
  </span>
  </ul>
  <br>

  - ## Multi Page Elements
    - ### Header
      ![Header of RND|ROLL](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/header_nkgay4.png)
      
      <h4><strong>General Features of the Header</strong></h4>
        <ul>
        <li>
        Logo
        </li>
        <li>
        Slogan
        </li>
        </ul>
      <br>

      <h4><strong>Features of the Header for authenticated users </strong></h4>
        <ul>
        <li>
        Greeting to the logged-in user
        </li>
        </ul>
      <br>

    - ### Navbar
      - <summary><h4><strong>General Features of the Navbar</strong></h4></summary>
        <details>
        <ul>
          <li>
          Home
          </li>
          <li>
          Conduct
          </li>
          <li>
          Tag
          </li>
          <li>
          Help
          </li>
          <li>
          Register
          </li>
          <li>
          Login
          </li>
        </ul>
        Image:
        <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_visitor_xftaic.png" name="Navbar of RND|ROLL">
        </details>
        <br>

      - <summary><h4><strong>Features of the Navbar for authenticated users</strong></h4></summary>
        <details>
        <ul>
          <span style="color: green">
          <li>
          Create Event
          </li>
          </span>
          <li>
          Profile & Repository / Create Profile (if no profile exists)
          </li>
          <li>
          Message
          </li>
        </ul>
        Image:
        <details>
          <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_user_oot1dw.png" name="Navbar of RND|ROLL">
        </details>
        <br>

      - <summary><h4><strong>Features of the Navbar for game masters</strong></h4></summary>
        <details>
        <ul>
          <li>
          GM-Icon
          </li>
        </ul>
        Image:
        <details>
          <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_gm_wobccu.png" name="Navbar of RND|ROLL">
        </details>
        <br>

      - <summary><h4><strong>Features of the Navbar for staff members</strong></h4></summary>
        <details>
        <ul>
          <li>
          Admin-Icon (With a link to the Administrator - Django Dashboard)
          </li>
        </ul>
        Image:
        <details>
          <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_admin_mqll2r.png" name="Navbar of RND|ROLL">
        </details>
        <br>

    - ### Footer
      <details>  
      <ul>
        <li>
        Links to different pages
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/footer_c8quce.png" name="Footer of RND|ROLL">
      </details>
      <br>

  - ## Home/Index Page
    - <summary><h4><strong>General Features of the Index Page</strong></h4></summary>
      <details>
      <ul>
        <li>
        Lists of all upcoming events (shows only public events)
        </li>
        <li>
        Every list item has a link to the related event
        </li>
        <li>
        Search function to search events by Title or Owner
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339734/media/images/README%20IMAGES/index_visitor_xn0nu3.png" name="Index of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Index Page for authenticated users</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update the Event option on the self-created event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339734/media/images/README%20IMAGES/index_user_xqg9sr.png" name="Index of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Index Page for game masters</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update Event option on all event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_gm_akj8gn.png" name="Index of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Index Page for staff members</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update Event option on all event
        </li>
        </span>
        <span style="color: red">
        <li>
        Delete Event option on all event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_admin_bzqhhs.png" name="Index of RND|ROLLL">
      </details>
      <br>

  - ## Events
    - <summary><h4><strong>General Feature of the Event</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - All Provided information and media from the event creation:
        <ul>
          <li>
          Title
          </li>
          <li>
          Picture ( If no picture was uploaded yet a default picture is displayed )
          </li>
          <li>
          Story
          </li>
          <li>
          "Watch Us Here" Button -> uses the provided main link to the event in a new tab
          </li>
          <li>
          Shoutouts
          </li>
          <li>
          Other links
          </li>
          <li>
          Start Date
          </li>
          <li>
          Max. Players
          </li>
          <li>
          Game Master
          </li>
          <li>
          Event Owner
          </li>
        </ul>
        <li>
        Section 2 - Characters:
        <ul>
          <li>
          Shows all the characters that have joined the Event
          </li>
          <li>
          The character image has a link to the character page
          </li>
        </ul>
        </li>
        <li>
        Section 3 - Comments:
        <ul>
          <li>
          If comments are made they are shown here
          </li>
        </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_visitor_oyfdj1.png" name="Event of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Event for authenticated users (not event owner)</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1  - All Provided information and media from the event creation:
        <ul>
          <li>
          Event Owner is a link to the Profile (if the owner has a profile)
          </li>
          <span style="color: orange">
          <li>
          Like Button to Like or Unlike the event
          </li>
          </span>
          <li>
          Join Button to open a list of Users' own created characters
          </li>
          <span style="color: orange">
          <li>
          Add Character to the event
          </li>
          </span>
        </ul>
        </li>
        <li>
        Section 2 - Characters:
        <ul>
          <span style="color: orange">
          <li>
          Remove own character
          </li>
          </span>
        </ul>
        </li>
        <li>
        Section 3 - Comments:
        <ul>
          <span style="color: green">
          <li>
          Add a comment
          </li>
          </span>
        </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_visitor_oyfdj1.png" name="Event of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Event for authenticated users (event owner)</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1  - All Provided information and media from the event creation:
        <ul>
          <span style="color: orange">
          <li>
          Update Event
          </li>
          </span>
          <span style="color: red">
          <li>
          Delete Event
          </li>
          </span>
        </ul>
        </li>
        <li>
        Section 2 - Characters:
        <ul>
          <span style="color: orange">
          <li>
          Remove any character
          </li>
          </span>
        </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_owner_roxk6z.png" name="Event of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Event for game masters</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 2 - Characters:
        <ul>
          <span style="color: orange">
          <li>
          Remove any character
          </li>
          </span>
        </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="(https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_gm_geak0j.png" name="Event of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Event for staff members</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1  - All Provided information and media from the event creation:
        <ul>
          <span style="color: orange">
          <li>
          Update Event
          </li>
          </span>
          <span style="color: red">
          <li>
          Delete Event
          </li>
          </span>
        </ul>
        </li>
        <li>
        Section 2 - Characters:
        <ul>
          <span style="color: orange">
          <li>
          Remove any character
          </li>
          </span>
        </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/event_admin_l9zdre.png" name="Event of RND|ROLL">
      </details>
      <br>

  - ## Conduct
    - <h4><strong>General Features of Conduct</strong></h4>
      <ul>
      <li>
      Links to the different page sections at the top
      </li>
      <li>
      Links to different pages
      </li>
      <li>
      Information and Disclaimer on/for RND|Roll
      </li>
      </ul>

  - ## Tag Index
    - <summary><h4><strong>General Features of Tag Index</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Option to add a new tag
        </li>
        </span>
        <li>
        List of all tags
        </li>
        <li>
        Tags link to a search result for events with the tag (opens in a new tab)
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tag_user_bfupls.png" name="Tag of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of Tag Index for staff members</strong></h4></summary>
      <details>
      <ul>
        <span style="color: red">
        <li>
        Delete Tag option (Opens a new page)
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352077/media/images/README%20IMAGES/tag_admin_owaxye.png" name="Tag of RND|ROLL">
      </details>
      <br>

  - ## Tagged Events
    - <summary><h4><strong>General Features of the Tagged Events</strong></h4></summary>
      <details>
      <ul>
        <li>
        Shows all public and expired events that have a certain tag
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_user_gsjngh.png" name="Events of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Tagged Events for authenticated users</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update the Event option on the self-created event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_user_gsjngh.png" name="Events of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Tagged Events for game masters</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update Event option on all event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_gm_ltjblb.png" name="Events of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Tagged Events for staff members</strong></h4></summary>
      <details>
      <ul>
        <span style="color: orange">
        <li>
        Update Event option on all event
        </li>
        </span>
        <span style="color: red">
        <li>
        Delete Event option on all event
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/tagged_admin_gcyvv3.png" name="Events of RND|ROLL">
      </details>
      <br>

  - ## Delete Tag
    - <h4><strong>Features of the Tagged Events for staff members</strong></h4>
      <ul>
        <li>
        Option to delete a Tag (will open Admin Dashboard)
        </li>
      </ul>

  - ## Help
    - <h4><strong>General Features of Help</strong></h4>
      <p>Information on different topics:</p>
      <ul>
        <li>
        creating and managing an event
        </li>
        <li>
        creating and managing a character
        </li>
        <li>
        creating and managing a profile
        </li>
      </ul>

  - ## Register
    - <h4><strong>General Features of Register</strong></h4>
      <ul>
        <span style="color: green">
        <li>
        creates a new account
        </li>
        </span>
        <li>
        offers advice on password
        </li>
        <li>
        error messages are in a different color
        </li>
        <li>
        offers a link to the login page 
        </li>
      </ul>

  - ## Login
    - <h4><strong>General Features of Login</strong></h4>
      <ul>
        <li>
        offers a link to the registration page
        </li>
      </ul>

    - <h4><strong>Features of Login for authenticated users</strong></h4>
      <ul>
        <li>
        log into the user account
        </li>
      </ul>

  - ## Messages
    - <summary><h4><strong>Features of Messages for authenticated users</strong></h4></summary>
      <details>
      <ul>
        <span style="color: green">
        <li>
        Create a message for the Game Masters and Administrators
        </li>
        </span>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663340653/media/images/README%20IMAGES/navbar_user2_rvhc5d.png" name="Navbar of RND|ROLL">
      </details>
      <br>

  - ## GM-Badge
    - <summary><h4><strong>Features of GM-Badge for game masters</strong></h4></summary>
      <details>
      <ul>
        <li>
        shows that you are a Game Master
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_gm_wobccu.png" name="Navbar of RND|ROLL">
      </details>
      <br>

  - ## Administrator-Badge
    - <summary><h4><strong>Features of Administrator-Badge for staff members</strong></h4></summary>
      <details>
      <ul>
        <li>
        shows that you are an Administrator
        </li>
        <li>
        links to administrator dashboard (opens in a new tab)
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663329977/media/images/README%20IMAGES/navbar_admin_mqll2r.png" name="Navbar of RND|ROLL">
      </details>
      <br>

  - ## Create Profile
    - <h4><strong>Features of Create Profile for authenticated users</strong></h4>
      <ul>
        <span style="color: green">
        <li>
        creating a user profile (minimum requirement: Click "Create Profile")
        </li>
        </span>
      </ul>

  - ## Profile & Repository
    - <summary><h4><strong>"General" Features of Profile & Repository for authenticated users (not profile owner)</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the profile creation:
          <ul>
          <li>
          username
          </li>
          <li>
          Game Master badge, if profile user is game master
          </li>
          <li>
          profile picture/default picture
          </li>
          <li>
          bio
          </li>
          <li>
          links to profile user websites and social media
          </li>
          </ul>
        </li>
        <li>
        Section 2 (hidden)
        </li>
        <li>
        Section 3 - Owned Events
          <ul>
          <li>
          Lists all created events of the profile user
          </li>
          <li>
          Lists Private Events
          </li>
          <li>
          Every list item has a link to the related event
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Narrated Events
          <ul>
          <li>
          Lists all narrated / game mastered events of the profile user
          </li>
          <li>
          Lists Private Events
          </li>
          <li>
          Every list item has a link to the related event
          </li>
          </ul>
        </li>
        <li>
        Section 5 - Characters
          <ul>
          <li>
          Lists all created characters of the profile user
          </li>
          <li>
          Every list item has a link to the related characters
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663341279/media/images/README%20IMAGES/profile_visitor_gdxcpl.png" name="Profile of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of Profile & Repository for authenticated users (profile owner)</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the profile creation:
          <ul>
          <li>
          email
          </li>
          <span style="color: orange">
          <li>
          Request Game Master Promotion / Note the Game Master Promotion Request is pending
          </li>
          </span>
          <span style="color: orange">
          <li>
          Edit Profile (update bio, picture, links)
          </li>
          </span>
          <span style="color: orange">
          <li>
          Edit Settings (update username, email)
          </li>
          </span>
          <span style="color: orange">
          <li>
          Change Password (update password)
          </li>
          </span>
          </ul>
        </li>
        <li>
        Section 2 (hidden)
        </li>
        <li>
        Section 3 - Owned Events
          <ul>
          <span style="color: orange">
          <li>
          Update the Event option on the self-created event
          </li>
          </span>
          </ul>
        </li>
        <li>
        Section 4 - Narrated Events
          <ul>
          <span style="color: orange">
          <li>
          Update the Event option on the self-created event
          </li>
          </span>
          </ul>
        </li>
        <li>
        Section 5 - Characters
          <ul>
          <span style="color: green">
          <li>
          Create a new Character
          </li>
          </span>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663346670/media/images/README%20IMAGES/profile_gm_owner_oj87hl.png" name="Profile of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of the Profile & Repository for game masters</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the profile creation:
          <ul>
          <li>
          no email
          </li>
          </ul>
        </li>
        <li>
        Section 2 - Messages
          <ul>
          <li>
          User messages
          </li>
          </ul>
        </li>
        <li>
        Section 3 - Owned Events
          <ul>
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Narrated Events
          <ul>
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663341279/media/images/README%20IMAGES/profile_gm_ztbbgy.png" name="Profile of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of Profile & Repository for staff members</strong></h4></summary>
      <details>
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
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          <span style="color: red">
          <li>
          Delete Event option</span>
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Narrated Events
          <ul>
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          <span style="color: red">
          <li>
          Delete Event option</span>
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663346726/media/images/README%20IMAGES/profile_adminr_gkujwu.png" name="Profile of RND|ROLL">
      </details>
      <br>

  - ## Character
    - <summary><h4><strong>General Features of Character</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the character creation:
          <ul>
          <li>
          name
          </li>
          <li>
          class
          </li>
          <li>
          image
          </li>
          <li>
          background
          </li>
          <li>
          character creator
          </li>
          <li>
          show equipment
          </li>
          </ul>
        </li>
        <li>
        Section 2 - Items
          <ul>
          <li>
          Items
          </li>
          </ul>
        </li>
        <li>
        Section 3 - Notes
          <ul>
          <li>
          Notes
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Joined Events
          <ul>
          <li>
          Lists all events the character has joined
          </li>
          <li>
          Lists Private Events
          </li>
          <li>
          Every list item has a link to the related event
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_user_zgdd37.png" name="Character of RND|ROLL">
      </details>
      <br>

    - <h4><strong>Features of Character for authenticated users (not character creator)</strong></h4>
      <ul>
        <li>
        Section 4 - Joined Events
          <ul>
          <span style="color: orange">
          <li>
          Update the Event option on the self-created event
          </li>
          </span>
          </ul>
        </li>
      </ul>

    - <summary><h4><strong>Features of Character for authenticated users (character creator)</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the character creation:
          <ul>
          <span style="color: orange">
          <li>
          Update Character</span>
          </li>
          <span style="color: red">
          <li>
          Delete Character</span>
          </li>
          <span style="color: orange">
          <li>
          Update Equipmment</span>
          </li>
          </ul>
        </li>
        <li>
        Section 2 - Items
          <ul>
          <span style="color: orange">
          <li>
          Update Item</span>
          </li>
          </ul>
        </li>
        <li>
        Section 3 - Notes
          <ul>
          <span style="color: red">
          <li>
          Delete Note</span>
          </li>
          <span style="color: green">
          <li>
          Create New Note</span>
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_owner_x7n9gg.png" name="Character of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of Character for game masters</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the character creation:
          <ul>
          <span style="color: orange">
          <li>
          Update character</span>
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Joined Events
          <ul>
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_gm_eqnml8.png" name="Character of RND|ROLL">
      </details>
      <br>

    - <summary><h4><strong>Features of Character for staff members</strong></h4></summary>
      <details>
      <ul>
        <li>
        Section 1 - view all provided information and media from the character creation:
          <ul>
          <span style="color: orange">
          <li>
          Update character</span>
          </li>
          <span style="color: red">
          <li>
          Delete character</span>
          </li>
          </ul>
        </li>
        <li>
        Section 4 - Joined Events
          <ul>
          <span style="color: orange">
          <li>
          Update Event option</span>
          </li>
          <span style="color: red">
          <li>
          Delete Event option </span>
          </li>
          </ul>
        </li>
      </ul>
      Image:
      <details>
        <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663352078/media/images/README%20IMAGES/character_admin_c9mm2s.png" name="Character of RND|ROLL">
      </details>
      <br>

  ## Defensive Programming
  To keep the application secure and protected any feature that is not read-only requires the user to be logged in.
  Further is any deletion feature restricted to the creator user or administrator
  <br>
  The update function is available to the creator or administrator and a special group of users.
  To be promoted to this group requires an administrator to manually set a flag in the user profile.
  <br>
  Event entering the websites manually to circumvent the restrictions placed on the links on the page will end in a custom error note, explaining why the content is not displayed.
  <br>
  Only in very die-hard cases, the following errors can appear:
  - AttributeError at /members/edit_profile/ - 'AnonymousUser' object has no attribute '_meta'
    This happens is a visitor enters the URL to edit user settings in the address bar.
    Since a visitor is not logged in, a related user object cannot be found, so an error is intended.
    No fix and working kind of intended.<br> Not logged-in Users should not be able to edit a profile, because they don't have one.
  - 404 - Page not found at /members/password/ 
    This happens is a visitor enters the URL to edit a user password change in the address bar.
    No fix and working kind of intended.<br> Not logged-in User can't change a password, if you forgot your password you need to make a "password reset"
  <br>

  ## Future Implementation
  * Reset Password Function
  * Group Chat on Events for Event owners and joined players
  * Item Model with pictures, etc. and changing equipment fields on the character to ForeignKeys
  * Delete comments
  * Delete own user account
  * Login with social media
  * bad name list

<hr>

## Technologies Used
* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back-end programming of the site.
<br>

* [Cloudinary API](https://cloudinary.com/) 
    * was used to enable users to upload images for their recipes whilst keeping the App safe and secure

* [Django](https://www.djangoproject.com/)
    * Django was used to create the models for the database, forms to post data into the database, the templates, and the view connecting them all.

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used to store user registration, login, and authentication. Postgres was also used to store the Categories.

* [Django Summernote](https://www.mongodb.com/)
    * MongoDB was the nonrelational database used to store less structured data such as recipes. MongoDB is where we host our NoSQL database.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [gunicorn](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project.

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open source toolkits and was used for ease of styling the Earthlings app.

* [Brave](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Lunapic](https://www9.lunapic.com/editor/)
    * Lunapic was used to work with images: Background removal, scale, etc.

* [Grammarly:](https://app.grammarly.com/)
    * Grammarly was used for spell-checking.

* [Notepad++:](https://notepad-plus-plus.org/)
    * Notepad++ for keeping notes for the project.

* [WEBP Converter:](https://www.onlineconverter.com/webp)
    * WEBP Converter was used to change *.jpg files to *.webp to reduce the size.

* [tinypng:](https://tinypng.com/)
    * Tinypng was used to reduce the file size of pictures.
<br><br>


<hr>

## Testing
### All testing undertaken for this project can be found in the [Testing Document](/TESTING.md)
<br>
<hr>

## Bugs, Issues, and Solutions
| # | Bugs, Errors, and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | CSS not loading in Heroku deployment | Set "Debug = False" in settings.py before committing your late version to GitHub
| 2 | CSS or Summernote issues when running the server in gitpod with "python3 manage.py runserver" | Set "Debug = True" in settings.py
| 3 | Linking to profile causes an error if the user is not logged in or has no profile | Use {% if user.profile.id  %} to only offer the link to a profile if a profile exists.
| 4 | Image does not upload in form | Make sure to add 'enctype="multipart/form-data"' form attributes"
| 5 | Image, Videos, and links can not be added to Text Rich-Field of Summernote | You may need to add "SUMMERNOTE_THEME = 'bs4'" into settings.py, as it sometimes does not accept bootstrap 5 or other settings.
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
1. **Click** the button labeled **"Reveal Config Vars"** and **enter** add the following keys and values:

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
* This project was heavily influenced by the "I Think Therefore I Blog"-Project from Code Institute / Matt Rudge and even some of the HTML and CSS code were the basis for my project
* Additionally I found a lot of help with some features (like connecting the profile ) from John Elder's Youtube series on Django [Create A Simple Blog With Python and Django](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
### Media
All used pictures a free use, changed/modified, or allow nonprofit usage and are mostly only used for testing purposes.

### Resources
README was strongly influenced by Joy Zadan and her awesome project [PALEO RECIPES](https://github.com/JoyZadan/paleo-recipes)

<hr>

## Acknowledgements
* Big Thank you to Matt Rudge, as the "I Think Therefore I Blog"-Project helped me to get the project rolling.
* Thank you to John Elder for offering the basic walk-through of Django.
* Special mention and thanks to my mentor, Dario Carrasquel, for his support and insights, as it made obvious to me that all the stuff I think is obvious and self-explanatory, is not obvious and self-explanatory at all.

<hr>

## Copyrights
&copy; 2022 RND|Roll by Andreas Beier