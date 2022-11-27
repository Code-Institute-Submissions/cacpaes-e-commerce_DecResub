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





