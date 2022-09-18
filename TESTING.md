<h1 align="center"> RND|ROLL Testing Documentation </h1>

<h2 align="center"><img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663424555/media/images/README%20IMAGES/readme-title-pic_a4yhkr.webp" height="500" width="900"></h2>


## MANUAL TESTING
Preliminary Setup:
Created: 
* User: Superuser - admin
* User Profile for admin
* Test Event:
* Test Character:
* Test Note:
* Test categories: 
    <br>This will serve as test content for the page, to be used in the following tests.

1. Test runs - Visitor access:
    * a) Reviewing visitor journey through RND|Roll.<br>Visitor can access and read:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | home | pass | pass |
        | 2 | conduct | pass | pass |
        | 3 | help | pass | pass |
        | 4 | tag - index | pass | pass |
        | 5 | tagged events | pass | pass |
        | 6 | search results | pass | pass |
        | 7 | event details | pass | pass |
        | 8 | character details | pass | pass |
        | 9 | Registration | pass | pass |
        | 10 | Login | pass | pass |

        Conclusion:<br>
        The visitor has view only access to the on RND|Roll as intended.<br>
        Enough to browse through events and event look a character details.<br>
        Depending on the dilligence of the creator, event can hereby caugth the attention of visitors.<br>

        <br>
    * b) Reviewing visitor access by manually posting the URLs in the address bar:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | create event | fail | fail |
        | 2 | event edit | fail | fail |
        | 3 | event remove | fail | fail |
        | 4 | profile| fail | fail |
        | 5 | update profile | fail | fail |
        | 6 | update settings | fail | fail - Server Error (500) |
        | 7 | change password | fail | fail - Page Not found 404 |
        | 8 | create characters | fail | fail |
        | 9 | edit characters | fail | fail |
        | 10 | delete characters | fail | fail |
        | 11 | edit items | fail | fail |
        | 12 | edit equipment | fail | fail |
        | 13 | delete note | fail | fail |
        | 14 | delete tag | fail | fail |
        | 15 | message | fail | fail |
        | 16 | administrator dashbord | fail | fail |

        Conclusion:
        As expected the visitor is prohibited from using any other feature on RND|Roll, even if one would try to bypass the normall webpage.
        The error that was found ans fixed was by events of deleted users, which have not been assigned to a new user.
        These were able to be deleted by a visitor, if he had the link form the deletion of that event.
        This was possible as the IF-Statement on the site checked "if user.id == event.owner.id".
        Since a user deletion would set the event onwer to nothing and a visitor is also nothing, the visitor was allowed to do that on these singular events.
        A correction was made to extent the Statement "if event.owner and user.id == event.owner.id".
        Now it looks if an event owner exsits and if he has the same id, causing an visitor to get the correct error message.

        <br><br>
2. Test runs - User access:
    Setup:
    Created User: rndroll

    * a) Reviewing User journey through RND|Roll.
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | home | pass | :--- |
        | 2 | conduct | pass | :--- |
        | 3 | help | pass | :--- |
        | 4 | tag - index | pass | :--- |
        | 5 | tagged events | pass | :--- |
        | 6 | search results | pass | :--- |
        | 7 | event details | pass | :--- |
        | 8 | character details | pass | :--- |
        | 9 | create event | pass | :--- |
        | 10 | edit own event | pass | :--- |
        | 11 | remove own event | pass | :--- |
        | 12 | profile| pass | :--- |
        | 13 | update own profile | pass | :--- |
        | 14 | update own settings | pass | :--- |
        | 15 | change own password | pass | :--- |
        | 16 | edit own characters | pass | :--- |
        | 17 | delete own characters | pass | :--- |
        | 18 | edit own items | pass | :--- |
        | 19 | edit own equipment | pass | :--- |
        | 20 | delete own note | pass | :--- |
        | 21 | message | pass | :--- |

        Conclusion:


        * Created Profile for Test User:
        * Created Event:
        * Created Character:
        * Created Note:
        * Created Categories:

        <br>
    * b) Reviewing user access by manually posting the URLs in the address bar:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | edit foreign event | fail | :--- |
        | 2 | remove foreign event | fail | :--- |
        | 3 | update foreign profile | fail | :--- |
        | 4 | update foreign settings | fail | :--- |
        | 5 | change foreign password | fail | :--- |
        | 6 | edit foreign characters | fail | :--- |
        | 7 | delete foreign characters | fail | :--- |
        | 8 | edit foreign items | fail | :--- |
        | 9 | edit foreign equipment | fail | :--- |
        | 10 | delete foreign note | fail | :--- |
        | 11 | delete tag | fail | :--- |
        | 12 | administrator dashboard | fail | fail |

        Conclusion:

        <br><br>
3. Test runs - Game Master access:
    * Setup:
    * Created User: Game Master
    * Created Profile for Game Master

    * a) Testing the promotion to Game Master feature:
        | # | Action | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | User request promotion in profile | pass | :--- |
        | 2 | User repeat request promotion in profile  | fail | :--- |
        | 3 | Promotion request is in the messages section (only visible to Admin)| pass | :--- |
        | 4 | Admin can set a user to game master in Administrator Dashboard | pass | :--- |
        | 5 | User sees GM badge on the navigation bar and in profile | pass | :--- |

        Conclusion:

        <br>
    * b) Test GM access:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | edit forigin event | pass | :--- |
        | 2 | remove forigin event | fail | :--- |
        | 3 | update forigin profile | fail | :--- |
        | 4 | update forigin settings | fail | :--- |
        | 5 | change forigin password | fail | :--- |
        | 6 | edit forigin characters | fail | :--- |
        | 7 | delete forigin characters | fail | :--- |
        | 8 | edit forigin items | fail | :--- |
        | 9 | edit forigin equipment | fail | :--- |
        | 10 | delete forigin note | fail | :--- |
        | 11 | delete tag | fail | :--- |
        | 12 | administrator dashbord | fail | :--- |

        Conclusion:
        * Updated Event:

        <br><br>
4. Test runs - Administrator access:
    * a) Test Administrator access:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | edit forigin event | pass | pass |
        | 2 | remove forigin event | pass | pass |
        | 3 | update forigin profile | fail | :--- |
        | 4 | update forigin settings | fail | :--- |
        | 5 | change forigin password | fail | :--- |
        | 6 | edit forigin characters | pass | :--- |
        | 7 | delete forigin characters | pass | :--- |
        | 8 | edit forigin items | pass | :--- |
        | 9 | edit forigin equipment | pass | :--- |
        | 10 | delete forigin note | pass | :--- |
        | 11 | delete tag | pass | pass |
        | 12 | administrator dashbord | pass | pass |

        Conclusion:
        
        <br><br>
5. Feature Test:<br>*Some of these features have already been confirmed working in the previous test runs*<br><br>
    * a) Normal Features:
        | # | Site | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | create event | pass | :--- |
        | 2 | edit event | pass | :--- |
        | 3 | remove event | pass | pass |
        | 3 | create profile | pass | :--- |
        | 3 | update profile | pass | :--- |
        | 4 | update settings | pass | :--- |
        | 5 | change password | pass | :--- |
        | 6 | create characters | pass | :--- |
        | 6 | edit characters | pass | :--- |
        | 7 | delete characters | pass | :--- |
        | 8 | edit items | pass | :--- |
        | 9 | edit  equipment | pass | :--- |
        | 9 | add note | pass | :--- |
        | 10 | delete note | pass | :--- |
        | 11 | add tag | pass | pass |
        | 12 | delete tag | pass | pass |

        Conclusion:

        <br>
    * b) Event Feature "Join":
        | # | Action | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | Visitor can press join | fail | fail |
        | 2 | Join button active for private events | fail | :--- |
        | 3 | Join button active for players that already joined | fail | :--- |
        | 4 | Join button active for events that reached the maximal amount of players | fail | :--- |
        | 5 | Join button opens a drop-down to display only user-created characters | pass | :--- |
        | 6 | Add will add character to the events character section | pass | :--- |

        Conclusion:

        <br>
    * c) Event Feature "Character Remove":
        | # | Action | Expected Outome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | Visitor can remove a character from the event | fail | fail |
        | 2 | Random User can remove a character from the event | fail | :--- |
        | 3 | Character Creator can remove his/her character from the event | pass | :--- |
        | 4 | Event owner can remove any character from the event | pass | :--- |
        | 5 | Game Master can remove any character from the event | pass | :--- |
        | 6 | Administrator can remove any character from the event | pass | pass |

        Conclusion:

        <br>
    * d) Event Edit:
        | # | Action | Expected Outome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | User can add characters to the event | fail | :--- |
        | 2 | Game Master add characters to the event  | pass | :--- |
        | 3 | Administrator add characters to the event  | pass | pass |

        Conclusion:

        <br>
    * e) Set automatically by creation:
        | # | Action | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
        | 1 | Event owner is set automatically | pass | pass |
        | 2 | Character creator is set automatically | pass | pass |
        | 3 | Note is set automatically assigned to character | pass | pass |
        | 4 | Message creator is set automatically | pass | pass |
        | 5 | Comment creator is set automatically | pass | pass |
        | 6 | GM request user is set automatically | pass | pass |

        Conclusion:
        The feature works as intended and will add the user as the creator and adds the note to the appropriate character.
        
        <br><br>
6. Deletion of content and cascade effect:
    | # | Action | Expected Outcome | Result |
    | :--- | :--- | :--- | :--- |
    | 1 | Delete Note | no cascade | pass |
    | 2 | Delete Character | cascade: deletes notes, items, and equipment and will be removed from any joined event | pass |
    | 3 | Delete Event | no cascade, characters that were joined will still be around | pass |
    | 4 | Delete Tag | no cascade, events with the Tag will still be around  | pass |
    | 5 | Delete Profile | no cascade, events, and character should still be there | Deleting the profile will delete any request for Game Master promotion |
    | 6 | Delete User | mix: the profile, characters should be deleted / the event loses the owner | Profile, Characters, notes, and requests are deleted.<br> Events and comments are still there, event update on the site requires, a new one has to be set in over the administrator dashboard |

    Conclusion:
    The delete of objects is behaving as expected. It is intended to have an event remain after, the user who owned it is deleted, as it might be handed to another user.
    Otherwise, the event can always be deleted separately
    
    <br><br>

## Validation Results
- ### HTML: W3C Markup Validator Test Results
    * [/home](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2F)<br>The show error are from the text-input of the character form, and cannot be fixed.
    * [/conduct](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fconduct%2F)
    * [/tag/index](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Ftag%2Findex%2F)
    * [/tag/add](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Ftag%2Fadd%2F)
    * [/tag/Adventure](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Ftag%2FAdventure)<br>The show error are from the text-input of the character form, and cannot be fixed.
    * [/create_event](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcreate_event%2F)
    * [/event/edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fevent%2Fedit%2F2)
    * [/event/remove](https://rndroll.herokuapp.com/event/2/remove)
    * [/event](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fevent%2F2)<br>The show error are from the text-input of the character form, and cannot be fixed.
    * [/members/profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fmembers%2F1%2Fprofile)
    * [/members/update_profile_page](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fmembers%2F1%2Fupdate_profile_page)
    * [/members/edit_profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fmembers%2Fedit_profile%2F)
    * [/members/password](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fmembers%2Fpassword%2F)
    * [/character/create_character](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2Fcreate_character%2F)
    * [/character/character](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2F1%2Fcharacter)<br>The show error are from the text-input of the character form, and cannot be fixed.
    * [/character/character/remove](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2Fcharacter%2F3%2Fremove)
    * [/character/character/edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2Fcharacter%2Fedit%2F3)
    * [/character/item/edit](https://rndroll.herokuapp.com/character/item/edit/3)
    * [/character/equipment/edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2Fequipment%2Fedit%2F3)
    * [/character/note/remove](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fcharacter%2Fnote%2F9%2Fremove)
    * [/help](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fhelp%2F)
    * [/members/message/](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fmembers%2Fmessage%2F)
    * [/search/](https://validator.w3.org/nu/?doc=https%3A%2F%2Frndroll.herokuapp.com%2Fsearch%2F%3Fq%3DTrek)<br>The show error are from the text-input of the character form, and cannot be fixed.
    <br><br>

- ### CSS: W3C CSS Validator Test Results
    * [css validation](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435933/media/images/README%20IMAGES/w3c_css_validated_xtxyjk.png)<br>
    <br><br>

- ### Python: PEP8 Online Test Results
    | # | File | Error Count | Error Detail |
    | :--- | :--- | :--- | :--- |
    | 1 | character models.py | 0 | all right |
    | 2 | character forms.py | 19| line too long|
    | 3 | character admin.py | 0| all right |
    | 4 | character urls.py | 1 | line too long  |
    | 5 | character views.py | 1 | line too long |
    | 6 | members forms.py | 23 | line too long  |
    | 7 | members urls.py | 1 | line too long |
    | 8 | members views.py | 2 | line too long |
    | 9 | event models.py | 0 | all right |
    | 10 | event forms.py | 13 | line too long |
    | 11 | event admin.py | 4 | line too long |
    | 12 | event urls.py | 1 | line too long |
    | 13 | event views.py | 5 | line too long |
    | 14 | rndroll urls.py | 0 | all right |
    | 15 | rndroll settings.py | 5 | line too long |
    | 16 | manage.py | 0 | all right |

    All "line too long" either can't be fixed or would make the code unreadable.
    <br><br>

- ### Lighthouse Test Results
    The results of all pages are within 4% variation, therefore these two representatives were chosen:
    * Desktop:
        ![desktop](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663432099/media/images/README%20IMAGES/lighthouse_rndroll_desktop_gual6r.png)
    * Mobile:
        ![mobile](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663432099/media/images/README%20IMAGES/lighthouse_rndroll_mobile_kp5bqq.png)
    <br><br>

## Responsive Design Testing
As no online tool was able to connect to Heroku to perform a test, all tests were done manually with the "Brave-Browser Development Tools":

- iPhone SE: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-iphone-se_v93ibo.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-iphone-se2_sx2gnk.webp)

- iPhone XR: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-iphone-xr_su3x2k.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-iphone-xr2_klwkzd.webp)

- iPhone12 Pro: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-iphone12pro_ahc45e.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-iphone12pro2_ju5nee.webp)

- IPad Mini: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-ipad-mini_ggqxz7.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-ipad-mini-2_zav89o.webp)

- IPad Air: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-ipad-air_lvfqac.webp), [Image2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-ipad-mini-2_zav89o.webp)

- Surface Pro 7: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-surface-pro-7_tgghgq.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-surface-pro-7-2_xgmzz8.webp)

- Surface Duo: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-surface-duo_wafonf.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-surface-duo-2_ffjjbs.webp)

- Samsung Galaxy S8: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-samsung-galaxy-s8_rtud1j.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435933/media/images/README%20IMAGES/responsive-samsung-galaxy-s8-2_hjqdey.webp)

- Samsung Galaxy A51/71: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-galaxy-a51-71_ewyew9.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-galaxy-a51-71-2_tpaigk.webp)

- Samsung Galaxy S20: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435933/media/images/README%20IMAGES/responsive-samsung-galaxy-s20-ul_rsvavy.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435933/media/images/README%20IMAGES/responsive-samsung-galaxy-s20-ul_2_iotbah.webp)

- Galaxy Fold: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-galaxy-fold_kkrhpr.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-galaxy-fold-2_qonpih.webp), [Image 3](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-galaxy-fold-3_pesuss.webp), [Image 4](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435934/media/images/README%20IMAGES/responsive-galaxy-fold-4_cnyyea.webp)

- Pixel 5: [Image 1](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-pixel5_su3mgk.webp), [Image 2](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435936/media/images/README%20IMAGES/responsive-pixel5-2_pbcyak.webp)

- Nest Hub: [Image](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-nest-hub_y5cqak.webp)

- Nest Hub Max: [Image](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663435935/media/images/README%20IMAGES/responsive-nest-hub-max_kofpzr.webp)

<br><br>
## Testing User Stories
- ### Visitor Goals - As a user who has not created an account, I want to be able to:
    * <strong>Quickly understand the main purpose and use of the application, RND|Roll, and how to use it</strong><br>
        * <strong>Meta description: "TV Guide for TTRPG / RPG Games, Events, Characters"</strong><br>
        * <strong>Slogan "Check out, join in, create, narrate and have fun." sets the appropriate expectation</strong><br>
        * <strong>If events have been created, all public events are shown on the index page</strong><br>
            ![Index page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663439589/media/images/README%20IMAGES/index-vistitor_si4onu.webp)<br><br>
        * <strong>The "Conduct" page and "Help" page offer further information</strong><br>
            ![Conduct](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663439957/media/images/README%20IMAGES/navbar_visitor_2_w0uiul.png)<br><br>

    * <strong>Search for specific shows or view details on any show, by title, owner, or category</strong><br>
        * <strong>Public events are already on the index page</strong><br>
        * <strong>Search funktion is on the index page</strong><br>
        * <strong>Tag Index is accesable ofer the navbar</strong><br>
            ![Index page](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663440289/media/images/README%20IMAGES/index-vistitor-2_innlma.webp)<br><br>

    * <strong>Register/ create a user account</strong><br>
        * <strong>Link to the register page is on the navbar</strong><br>
        * <strong>On the register page, the visitor is able to register and create an account</strong><br>
            ![Navbar](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663440422/media/images/README%20IMAGES/navbar_visitor_3_jgg2li.png)<br><br>
- ### Registered User Goals - As a user who has an account, I want to be able to:
    * <strong>Learn more about what I can do on RND|Roll</strong>
        * <strong>Information on the site and for the features can be fon in "conduct" and "help", both sites are liked on the navigation bar</strong><br>
        <h4><img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493077/media/images/README%20IMAGES/conduct_pfpasr.webp" height="300" width="390">  <img src="https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493077/media/images/README%20IMAGES/help_dbom1o.webp" height="300" width="390"></h4><br><br>
    * <strong>Create, Update and Review my own shows/events</strong><br>
    * <strong>The Deletion of shows (but be only possible in emergencies)</strong><br>
    * <strong>Categorise my shows</strong><br>
        * <strong>the creating an event feature is on the navigation bar, updating is available on any event listing and in the event details</strong><br>
        * <strong>the delete feature is available in the event details</strong><br>
        * <strong>multiple predefined Tags have been added to help Categorise your event</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493077/media/images/README%20IMAGES/event_p473fr.webp)<br><br>
    * <strong>Have players able to join my show</strong><br>
    * <strong>Have like and comment on my shows/events</strong>
        * <strong>Events have the option to like and join them</strong><br>
        * <strong>Comments can be added and read in the last section of an event</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663495472/media/images/README%20IMAGES/join_c4yv5a.png)<br><br>
    * <strong>Remove any player joined in my event</strong><br>
        * <strong>while normal players can only remove their character, event owners and game masters can remove all.</strong><br>
            ![User]()<br><br>
    * <strong>Upload Images for my shows</strong><br>
    * <strong>Be able to add additional information about my show</strong><br>
        * <strong>Options to upload images are in the creation and update forms</strong><br>
        * <strong>The update function  offers to add and edit information</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493076/media/images/README%20IMAGES/update-event_kgedt9.webp)<br><br>
    * <strong>Create, Update, Review and Delete my characters</strong><br>
        * <strong>In the Profile Page is a list of all created characters, clicking the Image of that character opens the character page</strong><br>
        * <strong>In the character page all information on the character can be viewed and edited</strong><br>
        * <strong>Character can be deleted</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663495923/media/images/README%20IMAGES/character_kehnmn.webp)<br><br>
    * <strong>Create a new category</strong><br>
        * <strong>In the Tag Index is the option to add a new category</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493077/media/images/README%20IMAGES/add_tag_kw6td9.png)<br><br>
    * <strong>Be forewarned of the consequences of what I am about to do on the App when appropriate and final, such as deleting characters</strong><br>
        * <strong>Deleteing characters, events and notes will offer information on the consequences</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663495923/media/images/README%20IMAGES/are-you-sure_zmloxe.webp)<br><br>
    * <strong>Have my user profile to update my settings and profile information and have all my shows and characters displayed</strong><br>
        * <strong>The Profile Page offers multiple feature and lists all created and narrated events</strong><br>
        * <strong>A list of all your character is availble</strong><br>
        * <strong>The option to create a new character is near the character list</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493076/media/images/README%20IMAGES/profile_domniy.webp)<br><br>
    * <strong>Request a promotion to Game Master</strong><br>
        * <strong>Requesting a promotion is possible in the Profile</strong><br>
        * <strong>Once the request has been filed, the button will bedisable</strong><br>
        * <strong>The button will be replaced with a Game Master badge if the request is approved</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663493076/media/images/README%20IMAGES/gm_request_vsdb2x.png)<br><br>
    * <strong>Send a message to Game Masters and staff, if extraordinary actions have to be taken</strong><br>
        * <strong>The message function in on the navbar</strong><br>
            ![User](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663340653/media/images/README%20IMAGES/navbar_user2_rvhc5d.png)<br><br>
    <br><br>
- ### Registered User Goals - As a user who has an upgraded account (Game Master), I want to be able to:
    * <strong>Update all shows/events, in case some quick updates are needed and the owner is not available</strong><br>
        * <strong>Game Masters can update all events</strong><br>
            ![GM](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_gm_akj8gn.png)<br><br>
    * <strong>remove any player joined in any event</strong><br>
        * <strong>A Game Master can remove all players from an event</strong><br>
            ![GM](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663442006/media/images/README%20IMAGES/event_characters_yry1oo.png)<br><br>
    <br><br>
- ### Site Admin Goals - As a staff member/administrator, I want to be able to:
    * <strong>Create, Update, Review and Delete any user-created content on RND|Roll</strong><br>
        * <strong>The administrator have that option</strong><br>
            ![Admin](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663339733/media/images/README%20IMAGES/index_admin_bzqhhs.png)<br><br>
    * <strong>Have the ability to maintain RND|Roll, in particular the shows/events, categories, character</strong><br>
        * <strong>The Administrator dashboard allows creation, update, read and deleted function for any content of RND|Roll</strong><br>
            ![Admin](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663440981/media/images/README%20IMAGES/admin_dashboard_qyynii.png)<br><br>
    * <strong>Promote Users to Game Master</strong><br>
        * <strong>Players can be promoted to Game Master in the Profile section of the Administrator dashboard</strong><br>
            ![Admin](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663440981/media/images/README%20IMAGES/admin_gm_promotion_m3gtts.png)<br><br>
    * <strong>Promote Users to a staff member</strong><br>
        * <strong>Users can be promoted to staff members in the User section of the Administrator dashboard</strong><br>
            ![Admin](https://res.cloudinary.com/dbscsb8w1/image/upload/v1663440981/media/images/README%20IMAGES/admin_promotion_w2ldqe.png)<br><br>
    <br><br>