# 2Bean-or-not-2Bean

![Welcome](./media/readme-screenshots/ss-main.png)

[2Bean-or-not-2Bean](https://beans2beans.herokuapp.com/) is a full stack e-commerce site aimed at the coffee enthusiast, concerned with their own health, fairtrade and the environment. This is an online only store which offers a variety of carefully selected beans(both organic and fairtrade) and quality coffee makers, cups and mugs. 
Organic is the better choice. These organic certified beans have not been treated with chemicals or toxins and as a result the coffee brew may be higher in antioxidants, vitamins, and minerals. All the beans are also fair trade certified, which means farmers who grow these beans receive a fair price, and their communities and the environment will also benefit as a result. What makes this coffee bean seller unique is that the purchaser can choose how dark they want their beans roasted, with the available options being, light, medium and dark. The purchaser can also choose to have their beans grinded with two options available, espresso and filter. As a another treat there are once-off beans which are less known or rare coffee beans, sourced from countries not well known for their coffee bean growers.  These once-off varieties will continuously change.

## User Experience (UX)

### User stories

- As a User, I want:
    - the home page to clearly indicate its intention, selling organic fairtrade coffee beans and coffee related products, such as coffee makers.
    - the home page to clearly indicate the navigation possibilities of the site (search function, order now, all products, beans, coffee makers, cups and mugs and special offers).
    - each page to clearly indicate the navigation possibilities of the site.
    - to find the website easy to navigate and move between the pages of the site.
    - to be able to access the site from different devices, thus the site must be responsive.
    - to find it easy to see what products are available for purchase, such a clicking on all products, and navigating the page by scrolling up and down or make use of the back to top of page button conveniently placed at the right hand side bottom of the page (on all the varying product pages).
    - to find it easy to see all available products under a certain category.
    - to be able to sort the products by price, ascending and descending.
    - to be able to sort the products by rating, ascending and descending.
    - to be able to sort the products by name, sorting from a to z or from z to a.
    - to be able to sort the products by category, sorting from a to z or from z to a.
    - to be able to search for products by any word that may appear in their name and / or description, such a colour, by making use of the search function.
    - to get more information on the products, such as tasting notes about the beans, the material and capacity of the coffee makers and / or cups and mugs by clicking on a specific product image.
    - to find it easy to shop for products by clicking the add to bag option.
    - to find it easy to increase or decrease the amount of products in the shopping bag.
    - to find it easy to remove products from the shopping bag by clicking the remove from bag option.
    - to find it easy to update the contents of the shopping bag, when products are being increased, decreased, added or removed.
    - to find it easy to select the type of roast for beans being bought.
    - to find it easy to select the type of grind (if any) for beans being bought.
    - to find it easy to selct not to have the beans grinded.
    - to see how many products in total are available.
    - to see how many products are available per category in the store.
    - to see how many products have been added to the shopping bag.
    - to see how much more should be spent to qualify for the free delivery.
    - to find it easy to check out and pay for my shopping bag contents, which process should be secure and have no risk of leaking personal information and / or banking details.
    - to find it easy to register a new account.
    - to find it easy to log into an existing account.
    - to find it easy to log out of an existing account.

- As the Site Owner / seller I want to:
    - provide a site that is clear in its intention, selling organic fairtrade beans and other coffee related products.
    - provide an easily navigatable site that provides quality products.
    - be able to store as much data as needed to be able to have a properly functioning online store reflecting all available products.
    - provide a site where users can easily and securely register accounts and provide personal information without having their information / security compromised.
    - provide a site where users can easily and securely purchase products online and provide sensitive information without having their security compromised.
    - ensure that the site is accessible from all device sizes.


### Strategy

The main aim and focus of 2Bean-or-not-2Bean is to provide an online store where users can purchase quality fairtrade organic beans and related coffee products from the comfort of their homes / offices / devices, which transactions can take place securely.
-   by selling organic beans, which have not been subjected to poisons and toxins and is a healthier option than non-organic beans;
-   by providing fairtrade beans, which means that the bean growers get fair prices for their products, which in turn makes their bean growing farms and communities more sustainable;
-   by taking part in the fairtrade model, by which the beans purchased can be traced back to the specific growers;
-   by providing the option to users to rate products, ensuring the highest quality products are being sold and getting the feedback from users ensuring the quality stays impeccable;
-   new / prospective purchasers will feel more comfortable when considering a purchase when they can see the product ratings from other users;
-   if a product is not rated well by users, it can be sold under the specials at a reduced price.


### Scope

A minimum viable product was created which covers the immediate and current goal of the site owner and should satisfy the prospective users:
- a website that clearly sells organic fairtrade beans and related quality coffee products, such as brand name coffee makers, cups and mugs;
- the search function which makes it easy for users to search and find products;
- the navigation bar that makes it easy for users to locate products in the indicated categories;
- user registration;
- user login and authentication;
- shopping bag which is able to add, remove, increase, decrease and update products;
- a secure payment system (stripe);

Possible future feature/s:
- provided that the relevant bean growers give their relevant consent, a section may be created to feature introductory stories about the bean growers, which may also help the bean growers with their own marketing and create awareness of the challenges organic and fairtrade growers face in the very competitive coffee bean market.


### Structure

The purpose of the website is to sell fairtrade organic beans and good quality related products. 
The website has been made very easy to navigate with the navigation bar present on all pages.
The website consists of :
- Home page - reflecting a search bar, navigation bar(all products, beans, coffee makers, coffee mugs and cups, special offers), order now link, my account and shopping bag
- Logo - made clickable to return to the home page
- Once an option has been selected from the drop down menu in the navigation bar, the relevant page will open reflecting all the products within the elected section:
-       All products (By Price, By Rating, By Category, All products)
-       Beans (Arabica Beans, Liberica Beans, Robusta Beans, Once Off available beans, All beans)
-       Coffee Makers (french press, drip coffee, moka pot, siphon pot, coffee maker and cup sets, all coffee makers)
-       Coffee mugs and cups (cappuccino cups, espresso cups, cups, mugs, messages mugs, cups on the move, disposable cups, all coffee mugs and cups)
-       Special offers (end of range, clearance, all specials)
- After a choice has been selected from the drop down menu in the navigation bar, the relevant products will be reflected (their images, price, category and rating)
- Once a product has been selected by clicking on the image, the page will open with a larger image, price, category, rating, description, option to choose the quantity, add to the shopping bag or keep shopping (the beans have additional options available, being roast(light, medium, dark) and grind(none, espresso or filter))
- My Account (Register and Log In options)
- Shopping bag, which has the following options:
-       Increase / decrease products
-       Remove products from bag
-       Update bag
-       Keep shopping
-       Secure checkout


The data schema below was prepared by using [Lucid.app](https://lucid.app/)

 ![Database schema](./readme/schema-db.png)

The sitemap was prepared using [Gloomaps](https://www.gloomaps.com/nMkFjnEiHn)

![Sitemap](./readme/sitemap.png)


### Skeleton

- Considering the strategy, scope and structure the following wireframes were created:

-   The main page of the site (desktop view)

![Main](./media/readme_wireframes/wf-main-page1.png)

![All Products](./media/readme_wireframes/wf-main-page2-ap.png)

![Beans](./media/readme_wireframes/wf-main-page3-bns.png)

![Coffee Makers](./media/readme_wireframes/wf-main-page4-cm.png)

![Coffee Mugs and Cups](./media/readme_wireframes/wf-main-page5-cmc.png)

![Special Offers](./media/readme_wireframes/wf-main-page6-so.png)

![Order](./media/readme_wireframes/wf-main-page7-order.png)

![Search](./media/readme_wireframes/wf-main-page8-search.png)

![My Account](./media/readme_wireframes/wf-main-page9-myacc.png)

![Shopping Bag](./media/readme_wireframes/wf-main-page10-sbag.png)

-   The main page of the site (mobile view)

![MainMobile](./media/readme_wireframes/wf-main-mobile-page1.png)

-   The following page of the site once clicked on one of the following options from the navigation bar : all products, beans, coffee makers, coffee mugs and cups or special offers. (desktop view)

![Next](./media/readme_wireframes/wf-next-page1-ap.png)

-   After clicking on one of the product images, the page opens the specific product selected, with beans having more options available (being the roast and grind options). (desktop view)

![Beans](./media/readme_wireframes/wf-next-page2-beans-clicked.png)

-   If a product has been added to the shopping bag and the shopping bag opened.

![Shopping Bag](./media/readme_wireframes/wf-shoppingbag.png)

-   When checking out (payment) for products in shopping bag.

![Ckeck Out](./media/readme_wireframes/wf-checkout.png)

-   After a successful order has been placed.

![Order confirmation](./media/readme_wireframes/wf-orderconfirmation.png)

-   Signin up view.

![Sign Up](./media/readme_wireframes/wf-signup.png)

-   Profile view.

![My Profile](./media/readme_wireframes/wf-myprofile.png)

-   Sign in view

![Sign In](./media/readme_wireframes/wf-signin.png)


![SKU codes](./media/readme-screenshots/sku-codes.png)




### Surface

- The clickable logo and navigation bar is consistently located on each page, allowing an intuitive user experience
- The images shown on the site, reflects the Katwijk community, which images in itself will draw the community members in as they would be curious about the happenings in their  
  direct environment
- The layout has been kept very clean and simple as the site is aimed at absolutely all persons within the Katwijk community, young and old, from all backgrounds
- The colours taken from the Materialize Color Palette was also kept very simple and more shades of the same colors were used in stead of a greater variety of colours, also to keep
    the site looking calm and relaxing.  The colours were also chosen reflect the blue skye, green of the trees and the colours of the incredible blue and green building.

        "Cool colors include green, blue, and purple, are often more subdued than warm colors. They are the colors of night, of water, of nature, and are usually calming, relaxing, and somewhat reserved.

        Blue is the only primary color within the cool spectrum, which means the other colors are created by combining blue with a warm color (yellow for green and red for purple).

        Because of this, green takes on some of the attributes of yellow, and purple takes on some of the attributes of red. Use cool colors in your designs to give a sense of calm or professionalism." Taken from (https://www.smashingmagazine.com/2010/01/color-theory-for-designers-part-1-the-meaning-of-color/)


- Screenshots reflecting the following pages:

    - For desktop, laptop, tablet and mobile:

  

   

## Features

### Existing Features

#### Common Page features

- Logo
    - The logo is clickable and provides an easy way to navigate back to the welcome page.
  
- Navigation Bar
    - Consistently located on each page allowing an intuitive user experience.
    - Provides links to All Products, Beans, Coffee Makers, Coffee Mugs and Cups, Special Offers.

- My Bean Account Shopping Bag
    - The logo is clickable and provides an easy way to navigate back to the welcome page.
    
#### Page specific features

-   Welcome page - available to the public and giving basic information about the website and providing a photograph of the neighbourhood
-   Login page - for completion of the username and password and clicking on the login link to enable registered members to log into the website 
-   Register page - for new/unregistered members to enable registration by completing their username, providing their firstname, surname and postal code, creating their own password 
    and confirming that they agree to abide by the rules as set out on the bottom of the registration page by clicking the checkbox provided (a requirement before registration can take place). When hovering over the Password space, a tip appears to indicate that a password length must be between 5 and 100 and alphanumerical.
-   Contact Admin page - provides both registered members and unregistered users access to obtain contact details of the site administrator, such as a contact number, email 
    address, office address and available hours and providing another photograph of the neighbourhood
-   Profile page - reflects the registered user's username, firstname, surname and postal code. The registered user can change their password on this page, should they
    want / need to at any stage after their initial registration. When hovering over the Password space, a tip appears to indicate that a password length must be between 5 and 100 and alphanumerical
-   All Offers page -  this page has the option for the registered and logged in user to see all the available offers, to filter the offers by category, to filter the page to 
    only see the offers of the registered user, to clear the filters and to edit or delete their own offers.  Registered members do not have the option to delete or edit offers of other members. No edit or delete buttons appear on the offers of other members. When hovering over the ApplyFilter button, a tip appears to assist the user when making use of this page
-   New Offers page - once a registered member is logged in, they can add their own offer which will appear on the All Offers page.  To add an offer, a member must first elect a 
    category from the drop down list, thereafter provide an offer name, then a description of the offer, provide a collection address, collection date and there is an option to reflect the collection start time and expiry time. A member can also indicate whether the offering is a hot or a cold product, which may be relevant for any persons considering collection of said offering
-   Logout in the nav bar - by clicking on the LogOut tab in the navigation bar a registered user is easily logged out of their profile and the registered section of the site


## Testing

The testing section is in a seperate file: [Testing](testing.md)


## Deployment

### GitHub Pages

- The site is deployed to GitHub pages. The steps to deploy were as follows:
    - Log into GitHub and locate the My-dutch-life GitHub repository, navigate to the Settings tab and select the Pages 
    - From the source section drop-down menu, select the Master Branch
- The live link can be found here - [2Bean-or-not-2Bean](https://beans2beans.herokuapp.com/)

### Making a Clone

- Log into GitHub and locate the My-dutch-life GitHub repository
- Click on the My-dutch-life repository
- Click on the Code button
- Choose the HTTPS option, then click on the clipboard right of the URL
- Then choose your IDE or editor of choice
- Open a respository or create a new repository 
- Open the terminal and type "git clone" and paste the URL copied above 
    git clone https://github.com/Morpheus-23/my-dutch-life.git 
- press enter and the clone will be created

### Forking the repository for own use

- Log into GitHub and locate the My-dutch-life GitHub repository
- Click on the My-dutch-life repository
- Click on the Fork button 

#### Create Mongodb database 

- Create a new database 
- Create the collection for:
    - categories
    - offers
    - members

### Heroku

#### Create a Heroku application 

- Create a Heroku account
- Select 'Create New App' from the dashboard and choose an App name
- Select the region based on your location
- Click 'Create App'

#### Deployment 

- Go to deploy tab and select github
- Enter repo name in the Connect to github search box and select the relevant repo.
- Go to setting and config vars and click reveal Config Vars
- Add environment variables from the env.py file
- Find Manual Deploy, choose master branch
- Click deploy master branch
- Click to Open App


## Technologies Used

Languages
- HTML5
- CSS3
- Javascript
- Python

Frameworks, libraries and others

-   Flask - micro framework for building applications
-   FlaskPyMongo - provides MongoDB support for Flask applications
-   Werkzeug - a library framework (https://werkzeug.palletsprojects.com/)
-   MongoDB - hosting the database in a cloud environment (https://www.mongodb.com/)
-   Gitpod - developing the site (https://www.gitpod.io/)
-   Github - version control and hosting the repository (https://github.com/)
-   Heroku - deploy the live site (https://dashboard.heroku.com/apps)
-   Pip - package installer for Python
-   dnspython - a toolkit for Python
-   jQuery (https://releases.jquery.com/)
-   Jinja (https://jinja.palletsprojects.com/en/3.0.x/templates/#)
-   RandomKeyGen (https://randomkeygen.com/)


## Unimplemented assessment criteria

* Styling can be more compact and less inline.
* Better defensive programming can be applied.
* Features for the site administrator can be developed so that new categories can be created by the administrator on the website and not just from MongoDB.
* Better wireframes could be done by making use of Balsamic, to replace the hand drawn wireframes.
* A more complete description of technologies used with their relevant links


## Content

- All icons were taken from [Font Awesome](https://fontawesome.com/)

- All images were taken from [Pexels](https://pexels.com/)
    -   Welcome page (Photo by Chait Goli: https://www.pexels.com/photo/photo-of-boats-parked-on-river-2031706/)
    -   Contact admin page (Photo by Teodor Savin: https://www.pexels.com/photo/green-and-blue-painted-house-600622/)

- The sitemap was prepared using [GlooMaps](https://gloomaps.com/)

- The database schema was prepared using [Lucid.app](https://lucid.app/)

- Fonts were utilised from [GoogleFonts](https://fonts.google.com/)

- Font and background colours and some functionalities were taken from [Materialize](https://materializecss.com/)

- Responsiveness was tested and screenshots were taken from [AmIResponsive](https://ui.dev/amiresponsive)

- Some design ideas were taken from the Code Institute Backend Development Mini Project.

- Some technical implementation information was taken from [StackOverflow](https://stackoverflow.com/)
    -   https://stackoverflow.com/questions/30207047/how-to-get-multi-select-dropdown-in-materialize-css
    -   https://stackoverflow.com/questions/69950552/mongodb-update-i-cant-update-my-documents-in-mongodb-with-flask-api
    -   https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes
    -   https://stackoverflow.com/questions/23577172/mongodb-pymongo-querying-multiple-criteria-unexpected-results

- Some technical information was taken from [Freecodecamp](https://freecodecamp.org/)
    -   https://www.freecodecamp.org/news/python-list-length-how-to-get-the-size-of-a-list-in-python/

- Some technical information was taken from [Digitalocean](https://digitalocean.com/)
    -   https://www.digitalocean.com/community/tutorials/css-prevent-line-break

- Some technical information was taken from [Youtube](https://www.youtube.com/c/CodersPage)
    -   https://www.youtube.com/watch?v=dQ2niRl2Lek

- I made use of[W3Schools](https://www.w3schools.com/) for help with html and css.
