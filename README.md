# Commerce
Designed an eBay-like e-commerce auction site that allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”



## Video review: https://www.youtube.com/watch?v=hOKHp8L1yP8 


## Getting started
<pre>
$ pip install -r requirements.txt
$ python manage.py runserver
<kbd>Ctrl</kbd>+<kbd>C</kbd> - to shut down the server. 
</pre> 

## Content
1. [Models](#Models)
    1. [User](#User)
    2. [Category](#Category)
    3. [Watchlist](#Watchlist)
    4. [Comment](#Comment)
    5. [Biding](#Biding)
    6. [Listing](#Listing)
2. [Create listing](#Create-listing)
3. [Active listings page](#Active-listings-page)
4. [Listing page](#Listing-page)
5. [Watchlist](#Watchlist)
6. [Categories](#Categories) 
7. [Django Admin Interface](#Django-Admin-Interface)

## **Models**

Here you will find a description of the models that are used.

## User

This model contains the **username**, his **email** and **hashed password**.
Used for registering, logging in, creating listings and working with a wishlist.

## Category

This model contains the **name** of the category.
Used to categorize listings.

## Watchlist

This model contains the **user**, who owns the watchlist, as well as the **listing id**.
Used to add listings to the watchlist.

## Comment

This model contains the **listing** that the comment matches, **content** of the comment, **name** of the commentator and **date** of the comment.
Used to add comments to the listing.

## Biding

This model contains the **listing**, **activity** of the bidding, currrent **buyer** and current **money** price of the listing.
Used to bidding.

## Listing

This model contains the **name**, **description**, **photo**, **category** and the **owner** of the listing.
Used to create new listings and then show them to the people.

## **Create listing**

Users able to visit a page to create a new listing. They able to specify a title for the listing, a text-based description, and what the starting bid should be. Users also can provide a URL for an image for the listing and/or a category.

## **Active listings page**

The default route of web application let users view all of the currently active auction listings. For each active listing, this page display the title, description, current price, and photo.

## **Listing page**

Clicking on a listing take users to a page specific to that listing. On that page, users can view all details about the listing, including the current price for the listing.

1. If the user is signed in he can add the item to their “Watchlist.” If the item is already on the watchlist, the user able to remove it.
2. If the user is signed in, he able to bid on the item.
3. If the user is signed in and is the one who created the listing, he have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
4. Users who are signed in able to add comments to the listing page.

## **Watchlist**

Users who are signed in able to visit a Watchlist page, which display all of the listings that a user has added to their watchlist. Clicking on any of those listings take the user to that listing’s page.

## **Categories**

Users able to visit a page that displays a list of all listing categories. Clicking on the name of any category take the user to a page that displays all listings in that category.

## **Django Admin Interface**

To create a superuser account that can access Django’s admin interface:
<pre>$ python manage.py createsuperuser </pre>
Site superuser able to view, add, edit, and delete any listings, comments, and bids made on the site.
To open superuser's console:
<pre>http://127.0.0.1:8000/admin/</pre>
