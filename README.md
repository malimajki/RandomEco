# RandomEco

My learning project for Django, HTMX, AlpineJS, PostgreSQL, and TailwindCSS

Project randomEco contains a few apps:

1.Blog
 - function based views
 - filtering by category and search filed
 - blog posts with comment section (using HTMX) and likes

2.Ecommerce
 - function based views
 - new context_processors for cart
 - filtering by category, search field and price slider (nouisliderJS)
 - rating products
 - QR code payment system (maybe later Paypall or Stripe)

3.Users
 - creating Profile model using signals (when creating User at the same time is created Profile)
 - social authentication with Google (using DjangoAllauth)

4.Messages
 - messages between user (using HTMX)
 - messages encrypted using (cryptography.fernet)

5.API
 - APIs (using DjangoRestFramewrok)
 - APIs for all products, categories of products, posts and categories of posts

6.Dashboard - in progress
 - class based views
 - creating posts and products

TODO:
 - pdf invoice generator 
 - checkout page
 - 7.Booking 
    - apppointment system for users 
    - user can make appointment once per 14 days
    - on every branch there can be up to 3 users per hour
    - every branch has its own working hours
    - add branches to API

In the future maybe implementation of NEXT.js for frontend.

How to run project:
- Get project -- git clone https://github.com/malimajki/RandomEco.git
- Create virtual enviroment -- virtulenv venv
- Activate virtualenv -- venv/scripts/activate (for windows)
- Install dependencies -- pip install -r requirements.txt
- Create and change DATABSE in settings.py
- Migrate database -- python manage.py makemigrations -> python manage.py migrate
- Create admin user (superuser) -- python manage.py createsuperuser
- In admin area create google social auth

- For development you may fill database with dumb data - python manage.py populate_products (from shop app)
                                                         python manage.py populate_posts    (from blog app)
                                                         python manage.py populate_users    (from users app)
                                                         python manage.py add_social_applications
