<h1>SecondHandBooks</h1>
<p>Love Reading Books?<br>
SecondHandBooks is an online store that sells used books in great condition and at an excellent value. A B2C company with a vision of reaching its target audience (people interested in books) through the internet. With the mission of delivering quality products through a reliable, fast and intuitive online sales platform.
</P>

[View website in Heroku Pages](https://secondhandbookk.herokuapp.com/)

![]()


<h2>Contents</h2>

<h2>UX/UI Design</h2>

<p>During the elaboration of the project, the aspects for the final result to respect a good UX (User experience) and UI (User interface) behavior were taken into consideration, thus delivering a quality project where the user can follow the steps of a purchase without difficulties or complications.</p>

<h3>Strategy</h3>

<h3>Site goals</h3>

<p>As mentioned, the project is an eCommerce project. I chose books as the main product to be sold in the online store. The business model is B2C where our target audience is direct consumers.

The idea of marketing and promotion would be the presence on social networks aiming at the themes of the books and their importance in our culture and education. With a well-designed SEO for the site that conveys trust and transparency to users, I believe it would be a project with the potential for success.</p>

*  The Second Hand Books e-commerce store aims to be responsive across devices to reach and be available to as many people as possible.
*  That the online store has a practical and simple checkout, requesting only the most important information to finish the order safely.
*  That the website provides feedback on important user actions, such as messages informing when logged in, logged out, when the order was completed, or at other relevant times.
*  The website should prioritize the display of the posts and present the content in a good way.
*  That users can view offers and discounted prices.
*  Be practical to register and access the account/profile for users who wish to do so.
*  So that users can easily add products to their bag and also modify it with convenience.


<h3>Agile</h3>

<p>For the development of this project, the Agile methodology was applied. As a support tool, I used the GitHub projects.</p>

[Go to this link for the project](https://github.com/users/cacpaes/projects/7)

<p>As you can see, we used a simple Kanban board with the fields (To do, Doing, Done). To do the next ones that will be executed, Doing the ones that are currently being developed and Done the ones that were finished.</p>


<h3>User stories</h3>

*  As an user, I want to know what kind of products I will find in the store, so I can decide if it is the product of my interest.
*  As an user, I want to see which products are on sale, so I can add them to my bag if the price attracts me.
*  As an user, I want to easily add or remove products from my bag, so I can adapt my product selection according to my needs.
*  As an user, I want to easily proceed to the checkout when I finalize my choice, so I can complete the purchase without complications.
*  As an user, I want to see that my order has been successfully completed, so I can be sure that the payment proceeded correctly.
*  As an user, I want to register or connect with the company, so I can be informed with the news and promotions.
*  As a site owner, I want to easily add, edit or remove products, so I can provide new products or correct some information.
*  As a site owner, I want to send a communication to the subscribers of the site, so I can send promotions and communications.
*  As a site owner, I I want to update stock and order status, so I can keep accurate information.


<h3>Scope</h3>

<p>For the scope of this project the following key points were determined.</p>

*  Allow the site owner to update stock and order status direct from the website.
*  Allow the site owner add, update or remove produtos direct from the website.
*  Allow the user to add and manipulate the products in the bag before checkout.
*  Allow logged in users to interact with comments and rating.
*  Allow users to manipulate their delivery details informations.
*  Allow the user to create an account to keep the information saved.
*  The website should be functional and intuitive, easy to navigate and proceed to checkout.
*  Use bootstrap to make the site responsive, and custom CSS and Java Script to complement.
*  Create a checkout using Stripe as payment method tool.
*  Create a webpage application using the Django framework.
*  Create a webpage application using the Django framework.


<h3>Structure</h3>

<p>The page structure for SecondHandBooks Store was determined as follows:</p>

  *  Home, profile, products (filter pages for: Categories / Offers), shopbag, checkout (checkout page / checkout success), management (Product Manag. / Stock Manag. / Order Status Manag. / New Letter Manag.).

<p>For users not logged in, will be displayed:</p>

*  Home, products (filter pages for: Categories / Offers), sign in, sign up, shopbag, checkout (checkout page / checkout success).

<p>For superuser (site owner) logged in, will be displayed:</P>

*  Home, products (filter pages for: Categories / Offers), management (Product Manag. / Stock Manag. / Order Status Manag. / New Letter Manag.), My account (My profile / Logout), shopbag, checkout (checkout page / checkout success).
*  My profile will be the same as users.


<h3>Skeleton</h3>

<p>The wireframe was created using the Pencil. During the elaboration of the wireframes, I added what the front end should look like. At the end of the development some changes were made.</p>

*  Wireframes

![wireframes](https://user-images.githubusercontent.com/93129370/203789166-b2dd8af2-ed05-48cf-9847-b24152416dcd.png)

![wireframes1](https://user-images.githubusercontent.com/93129370/203789212-5a665e98-e8fd-4ffa-bf5b-bb247bc7fc95.png)

![wireframes2](https://user-images.githubusercontent.com/93129370/203789257-1b95334a-6d2d-4c9e-a47f-0f3ef35743c6.png)


<h3>Database diagram</h3>
<p>The SecondHandBooks database is designed to determine all models present in the project and their relationships.

Regarding the purchase and checkout process, the user must be logged in. It is not possible to checkout without an account. The selected products are added to the shopping bag and when accessing the checkout, the information is transferred automatically.</p>



![img-diagram](https://user-images.githubusercontent.com/93129370/204109520-79438816-67d9-4c44-9295-0ea378dd3a49.jpeg)


<h3>Surface</h3>

*  Colours
<p>For the Street Craft project I used predominantly standard Bootstrap colors.<br>
For the texts, the colors white or black were applied according to the background color to have the proper contrast.</p>


<h3>Typography</h3>

<p>The site's font was chosen from google fonts.</p>


<h2>Imagery</h2>

* For the SecondHandBooks project, I selected images that can enhance the user's visual response and convey the idea of the website. 



<h1>Features</h1>

<h2>Existing Features</h2>


<h3>Favicon</h3>

* Favicon is loaded on every page.

<h3>Navbar</h3>

* Navbar that is present on all pages for user navigation through the online store.
* Is present for everyone the logo/banner that redirects to the home page, the search bar, a link to Home, a link to Shop(Dropdown) - All Products / Select Category(Skateboards / Caps & Hats / Backpacks & Bags) / Special Offers(New Arrivals / Special Sale / Las Chance), a shopbag where display Bag icon, total of products and value.
* The other links are displayed depending on whether the user is logged off or not, and what type of account.
* For not logged users, the links are displayed: : Sign in and Sign up.
* For logged users, the links are displayed: : My Account(Dropdown) - My Profile / Logout
* For logged superusers, the links are displayed: : My Account(Dropdown) - My Profile / Logout and Management(Dropdown) - Product Manag. / Stock Manag. / Order Status Manag. / News Letter Manag.
* Navbar is responsive, for mobiles it automatically groups to drowdown menu.




<h3>Footer</h3>

* The footer is shown only when reaching the end of the page, it counts with a few navegation links, News Letter - Subscribe button and Social links.

* The News Letter - Subscribe button, open a modal form when clicked. Where the user can subscribe using e-mail and a name.
* The Social links are four in total, they open a new page of the corresponding social network when clicked.

<h3>Hero image</h3>

<p>At the beginning of the home page, the first section has a carousel of images.</p>

* Present on the index page, and one of the first images that the user sees when he logs into the website, it has a background image of an  coffee.
 
 


<h3>About section</h3>

* This section has a short introductory text about what is being made available on the website.

<h3>Sign out</h3>

* Registration page, with a simple form with the field for username, e-mail (optional) and for password twice, a button to register. A short text that calls who already has a registration to the login page.




<h3>Sign in</h3>

* Access page, with two fields to be filled in (username and password). a button to log in. A short text with a callout for those who don't have an account.



<h3>Logout</h3>

* Page for logged in users who have selected the logout option.


<h3>My Profile</h3>

* Returns the username from which account you are logged in.
* It shows some account options like: a button for My Orders, a field to show active coupons, a button to change the password and another button to delete the profile.
* The delivery data is available as a form that can be changed. By clicking the update info button the information entered into the fields is saved and a success message is displayed


<h3>My Orders</h3>

* Returns the total orders of the logged in user.
* A list with the following information: Order Number / Date / Items / Order Total
* The Order Number ia a link to redirect to that order details page.


<h3>Order Details</h3>

* It shows the details of the order. It is possible to see the order number, date, products and quantity, billing info, delivering info, contact info and order status.
* The Order Status returns what step the order is currently at, and the next and completed steps
* It also has two buttons, one to go back to My Profile page and the other to My Orders.


<h3>All Products</h3>

* The main page for displaying the store's products.
* At the top, it shows how many products there are for a given search / filter. A selection box is present to sort among all products, sorted by price or name.
* The user can add the product to the shopbag via the product card container and select the quantity.
* By clicking on the product image, the user is redirected to the product detail page.
* By selecting the category or offer in the navigation bar the user will only see the products in that specific filter.


<h3>Product Details</h3>

* It shows a picture of the product and just below the average reviews. If the user is logged in, a button is displayed that redirects to the reviews page.
* It is possible to see all information, name, SKU, offer if any, price (discounted price if any), description.
Quantity field (Less / More buttons).
* Buttons for KEEP SHOPPING (back to products page) and ADD TO BAG.
* If logged as superuser the buttons to edit and delete product are visible at the end.
* Delete product button, redirect to a new page to confirm action.


<h3>Shopbag</h3>

* If the shopbag is empty, only a text is displayed and the button to KEEP SHOPPING
* It shows a list with the added products.
* A product image with the name, sku and unit price.
* A field to modify the quantity with the button to update. And the button to remove the product.
* The order and delivery totals are displayed.
* If the user is logged in, a field to add the discount coupon is displayed and the button to apply it. If it is valid the discount is applied and the discount field is displayed.
* At the end are the buttons for KEEP SHOPPING (back to products page) and SECURE CHECKOUT (redirect to checkout page).


<h3>Checkout</h3>

* It shows a Order Summary with a resume of the order.
* A form with contact and delivery information to be filled in. If the user is logged in and has the information saved, these fields are automatically filled in.
* If user not logged display option links to create an account ou to login. If user are logged in, display a check bos to auto save the form information to profile.
* Field for credit card data, using the Stripe tool.
* At the end are the buttons for Adjust Bag (back to shopbag page) and Complete Order (submit the form if valid, and redirect to success checkout page).


<h3>Checkout Success</h3>

* As soon as the order is processed and payment has been confirmed successful, an e-mail is sent to the user with the order information and the order number.
* It shows the details of the order. It is possible to see the order number, date, products and quantity, billing info, delivering info, contact info.
* At the end have one button Check out the latest promotions (redirect to products page)


<h3>Management - Add Product, edit and delete</h3>

* Accessible only to superuser.
* It has a form for the site owner to easily add new products to the store.
* One button for cancel(redirect to My Prodile page) and one button for add product (If valid, submit form and add new product).
* It has a form for the site owner to easily  edit products to the store.
* One button for Update Book
* To delete a book just click the DELETE button
* When add, edit and delete a book a success message appears.


<h3>Management - Custom Facebook Page</h3>

*  A customized page for the store was created on Facebook. In order to increase the presence of the store on social networks.


<h2>Features Left to Implement</h2>

* For the future implement the User Stories #13 Filter products that have not been completed at this time. As a user, I want be able to see any special offers quickly.
* For the future implement the User Stories #15 Filter products that have not been completed at this time. As an user, I want to receive an email to confirm my order, so that I can feel more secure
* For the future implement the User Stories #24 Filter products that have not been completed at this time. As a user I want to see books related to the topic I'm researching so I can have more purchase options


<h2>Deployment</h2>

* To create this project I used GitHub and GitPod.
* I used the Code Institute Gitpod Full Template, clicking on the "Use this template" button. From there I created the repository on Github with my username.
* These commands were used for version control during project:
    * git status - to check the status of the files to be commited.
    * git add filename - to add files before committing.
    * git commit -m "message" - to commit changes to the local repository.
    * git push - to push all committed changes to the GitHub repository.

<h3>Deployment</h3>

<p> 1. Create Django project and app </p>

* I installed django using the command pip3 install Django==3.2;
* I installed supporting  libraries  / models to this project presents in requirements.txt file;
* I created the requirements.txt file using the command pip3 freeze --local > requirements.txt;
* I created my Django project with the command django-admin startproject project_name .;
* I created my Django app with the command python3 manage.py startapp app_name;
* I used the comands python3 manage.py makemigrations and python3 manage.py migrate;
* To test and run the project I used python3 manage.py runserver.


<p> 2. Create Heroku app </p>

* I opened the heroku website and logged into my account
* I created a new app with the project name, chose the region Europe
* I opened the Resources section and searched for Heroku Postgres and selected it
* I opened the Settings section and then Config VARS, after I initially added the keys needed to start development DATABASE_URL/SECRET_KEY/CLOUDINARY_URL;
* Still in Config VARS I added the following keys: PORT with a value of 8000 and DISABLE_COLLECTSTATIC with a value of 1;

<p> 3. Set up Django settings.py and necessary folders/files </p>

* Set up to connect the environment variables
         from pathlib import Path
         import os
         import dj_database_url
         from django.contrib.messages import constants as messages
         if os.path.isfile('env.py'):
         import env
         
* Inside INSTALLED_APPS I added the necessary apps

* For the database I replaced it with the following code

        DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        
* For the static files and media I replaced it with the following code to conect to Amazon (AWS)

      STATIC_URL = '/static/'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
      
      MEDIA_URL = '/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
      
      if 'USE_AWS' in os.environ:
      # Cache Control
      AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
      }
      # Bucket Config
      AWS_STORAGE_BUCKET_NAME = 'streetcraft'
      AWS_S3_REGION_NAME = 'eu-west-1'
      AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
      AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

      # Static and media files
      STATICFILES_STORAGE = 'custom_storages.StaticStorage'
      STATICFILES_LOCATION = 'static'
      DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
      MEDIAFILES_LOCATION = 'media'

      # Override static and media URLs in production
      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
      
      
* Set Google social account provider config.

      SOCIALACCOUNT_PROVIDERS = {
          'google': {
              'SCOPE': [
                  'profile',
                  'email',
               ],
               'AUTH_PARAMS': {
                   'access_type': 'online',
                }

           }
      }


* Set up Stripe config.

      # Stripe setup
      STRIPE_CURRENCY = 'usd'
      STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
      STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
      STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

* Set up e-mail config.

      # E-mail setup
      if 'DEVELOPMENT' in os.environ:
          EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
          DEFAULT_FROM_EMAIL = 'streetcraft@example.com'
      else:
          EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
          EMAIL_USE_TLS = True
          EMAIL_PORT = 587
          EMAIL_HOST = 'smtp.gmail.com'
          EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
          EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
          DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
         
* Create a Procfile and add the following text

      web: gunicorn streetcraft.wsgi:application
      
 
<h3> 4. Final deployment. </h3>

* In settings.py inside the Django project I changed DEBUG to:
  
      if 'USE_AWS' in os.environ:
         DEBUG = False
      else:
         DEBUG = True
         
* I migrate database to ElephantSQL instance using DATABASE_URL settings, coping and pasting the URL without commit. Changing the DATABASES to: 

      DATABASES = {
      'default': dj_database_url.parse('elephantsql-database-url-here')
      }
      
* In Heroku I went back to Settings > Config VARS and removed the DISABLE_COLLECTSTATIC var;
* In Heroku I navigated to the Deploy section;
* I clicked to connect to GitHub and searched for my repository for this project;
* I clicked on manual deploy to build the App;
* When finished, I clicked the View button, which redirected me to the live site.


<h2>Fork</h2>

* Forks let you make changes to a project without affecting the original repository. Follow this steps:
1. Go to the repository page, can be accessed [here](https://github.com/cacpaes/e-commerce).
2. On top right, you select the Fork option and proceed.
3. A duplicate will be created inside your repository.


<h2>Clone</h2>

* Clone let you create an identical repository to the original. Follow this steps:
1. Go to the repository page, can be accessed [here](https://github.com/cacpaes/e-commerce).
2. Click on code drop down menu.
3. Choose if you want to clone using HTTPS, SSH or GitHub CLI. Then select de copy button.
4. Open your Git Bash in your IDE.
5. Type git clone and then paste the URL you copied before.
6. Press Enter to create your clone.


<h2>Technologies and tools</h2>

<p> Programming languages used: Python 3.8, Java Script, HTML5 and CSS3. </p>

* Gitpod - Used to create/edit the code of the project.

* Github - Used to create repository, for version control and Agile project.

* Heroku - Used to deploy the project.

* Django - Used in the development of this project. Main python Framework.

      *The following python modules were used on this project:
      asgiref==3.5.2
           django-model2puml==0.2.1
           asgiref==3.2.3
           boto3==1.12.42
           botocore==1.15.42
           chardet==3.0.4
           dj-database-url==0.5.0
           Django==3.0.1
           django-allauth==0.41.0
           django-countries==6.0
           django-crispy-forms==1.8.1
           django-storages==1.9.1
           docutils==0.15.2
           gunicorn==20.0.4
           idna==2.8
           jmespath==0.9.5
           oauthlib==3.1.0
           Pillow==7.0.0
           psycopg2-binary==2.8.5
           python3-openid==3.1.0
           pytz==2019.3
           requests==2.22.0
           requests-oauthlib==1.3.0
           s3transfer==0.3.3
           sqlparse==0.3.0
           stripe==2.42.0
           urllib3==1.25.7

* Bootstrap - Used to . CSS/JS Framework for developing responsiveness and styling.

* ElephantSQL - Used as database for this project.

* Amazon AWS - Used to upload images and cloud hosting service.

* Jquery Ajax - Used to load more content at garage and events pages.

* Ludichart - Used to create the database diagram and agile images.

* Pencil - Used to creat the wireframes.

* Font Awesome - Used for the favourite icon.

* Bootstrap Icons - Used for all others icons.

* Favicon.io - Used to implement the favicon on the website.

* DevTools - Chrome - to assist in the development of the project.

* Lighthouse (Chrome Devtools) - Used to performance test.

* WAVE - Used to acecessibility test.

* PEP8 - Used to test/validate Python code.

* JShint - Used to test Java Script code.

* Jigsaw - Used to test CSS code.

* Validator - Used to test HTML code.


