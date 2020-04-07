
[![Build Status](https://travis-ci.com/Luciano-Lima/ecommerce.svg?branch=master)](https://travis-ci.com/Luciano-Lima/ecommerce)


# OnlineStore

This is a ecommerce web app with intended to make a increase in the sales for a company who is looking to expand the business. 

This website was creating for a company who has been trading from its warehouse for a few years but now the owners have decide that is time to take their business to the next level and for that they need to start trading online.



## UX

• The users can register to create an account.
• The users can edit their account details 
• The users can perform searches for a product in the specific category
• The users can purchase the items and make payments using Stripe
• The users can sign up to receive a newsletter
• The users can follow us in the major social media
    
   
The wireframe for this project can be accessed here https://luciano-online-store.s3.eu-west-2.amazonaws.com/wireframe.jpg
   
  

## Features

Navigation for login, logout, profile and cart.

Navigation directing the user to a specific category

A search bar to perform random searches in the database

Maim content area to display the products in the database

Footer displaying a search bar, newsletter sign in and social media icons



### Existing Features

• In the top right of the page the users will find a navigation allowing then to login or register as a new user and also a     cart button where it displays the products added to the cart.

• The logged in user will also have the ability to see his profile and also to edit his personal information. The user          details will be automatically filled in the  form so he doesn't have to remember the details that were given when he         first signed up. 

• From the top of the page the user will find the main navigation menu where it will direct to the main product categories.

•Bellow the main navigation the user will find a search bar which they can perform search for products like laptop or tv.

•there will be three products displaying in the home page which can be for different categories.

•The users can purchase a item of their choose and fill out the form to process the payment with their credit card.

•Under the products gallery the user will find a paginator future which will allow to navigate to all the products in the database

•In the footer the user will find in the left hand side another search bar where he can perform a search for individual         items. Also in the footer section in the right hand side the user will find the newsletter form where he can fill up with    his email to subscribe to receive notifications.

•The last content also in the footer is reserved for the social navigation links which includes, Twitter, Facebook,             Instagram, and Pinterest.



### Features Left to Implement

• A newsletter form  to be placed in the newsletter/sign_in page after the user subscription where he would be able to choose which kind of content to receive.

• A wish button to be placed next to the add to cart button so the user can have the option to save a product instead of placing it direct to the cart.

• A image gallery to display multiple pictures instead of only one of each item.
  
•  The ability to toggle the item description.

    

    
    

## Technologies Used
    
  
  * <a href="https://dev.w3.org/html5/html-author/">HTML</a>
      * The project uses __HTML__ a mark-up language for the structure and presentation of the contents.

  * <a href="https://getbootstrap.com/">Bootstrap</a>
    * The project uses __Bootstrap__ for responsive grid layout.

  * <a href="https://jquery.com/">JQuery</a>
    * The project uses __JQuery__ to simplify the DOM manipulation.


  * <a href="https://fontawesome.com/">Font Awesone</a>
    * The project uses __Font Awesome__ a toolkit based on CSS and LESS used to display icons.

  * <a href="https://stripe.com/gb">Stripe</a>
    * The project uses Stripe to process credit card payments

* <a href="https://www.python.org/">Phython</a>
    * The app was build in Python

* <a href="https://www.djangoproject.com/">Django</a>
    * Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

* <a href="https://aws.amazon.com/">AWS</a>
    * Amazon S3 a storage service  offered by Amazon Web Services that provides object storage through a web service interface



## Testing

This project was manually tested in all the major browsers including Google Chrome, Safari and Internet Explorer to confirm compatibility. The tests were conducted in virtual mode using the google developer tools and also physical mobile phones such us: Nokia, Samsung Galaxy, HtcM8, Samsung Tablet S4, IPad and IPhone5. I can confirm the project has a mobile friendly design and it does work in all platforms.

I have used <a href="https://validator.w3.org/">HTML Validator</a> to validate the HTML code and corrected all the major error. I have also uploaded the CSS file to <a href="https://jigsaw.w3.org/css-validator/">CSS Validator</a> to check for error and the result was clear, no error or warning was detected.

The navigation links were tested individually to make sure it redirects to the relevant item category.

The two search forms were tested with a diversity of queries to confirm it does return the relevant query.

The forms for login, register and profile update were tested to confirm it displays a message to the user asking to enter the required information and preventing the form submission in case a field were left empty.
The social media links were tested individually to make sure it does redirect the user to the relevant content. 

I have also conducted TDD tests in the cart app views,  testing expecting to get  a status code of 200 and all the testing views passed.
I have also conducted TDD tests in the app checkout forms asserting for (assertingEqual and assertingFalse), with the intention of  checking for a form validation and for required fields which both of the tests returned a OK result meaning that passed the test.
I have also conducted TDD tests in the newsletter app testing for a returning  code of status 200. 
I have also conducted TDD tests in the products  models, to confirm that a product can not be created without a name
And also each product can have its own unique id, which guarantee a consistence in the database.
the product app view were also tested looking for a status code of 200 asserting that it does return the correct template as per the views reverse request.




## Deployment

To see the code follow the link to my GitHub repository. https://github.com/Luciano-Lima/ecommerce. If you like you can also download or clone the repo, just click on the green "Clone or Download button" then save it to a folder in you computer. The website is hosted on Heroku. Here is the live version link: https://luciano-online-store.herokuapp.com/

To deploy the project to heroku I have used the following commands:

 • on GitHub create a new repository.
 
 • Initializing the repository -  'git init'
 
 • Adding files - 'git add' 
 
 • To save it to git - 'Git commit -m'  'first commit'
 
 • To push commits -  git push -u origin master.

You can see your list apps going too: heroku apps
From Heroku go to settings and then  to config vars that will allow you to set up the environments variables allowing to connect the app to heroku. For security reason the environment variables were set in a separate file env.py and referenced by os.environ. During the development phase the debug mode were set to True so that would help to identify and correct any bugs. For deployment the debug were set to back to False that will also enable increasing in the app performance.

## The Database
The database used for this project was Postgressql an open source database. 
The relationship was based in 1 to 1 where a user can have 1 profile and 1 profile will be related with 1 user only with prevents duplicate profiles.

## Credits


#### Content & Media

• The pictures and the products descroptions were obtained from 
<a href="https://www.currys.co.uk/gbuk/index.html">PCworld</a>

• The social media icons and the icons for the contact section are from <a href="https://fontawesome.com/">Font Awesone</a>



### Ackowledgments

• The whole project was unstructured following <a href="https://courses.codeinstitute.net/login">Code Institute</a> good practice in how to build an ecommerce web app where some of the fundamental code logic were implemented in this app with updates to fit the app purpose.  