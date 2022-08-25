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




![SKU codes](./media/readme-screenshots/sku-codes.png)


