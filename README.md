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

3.Dashboard
 - class based views
 - creating posts and products

4.Users
 - creating Profile model using signals (when creating User at the same time is created Profile)
 - social authentication with Google, Facebook or Github (using DjangoAllauth)

5.Messages
 - messages between user (using HTMX)
 - messages encrypted using (cryptography.fernet)

6.API
 - APIs (using DjangoRestFramewrok)
 - APIs for all products, categories of products, posts and categories of posts

TODO:
 - pdf invoice generator 
 - checkout page

In the future maybe implementation of NEXT.js for frontend.

How to run project:
- Get project -- git clone https://github.com/malimajki/RandomEco.git
- Create virtual enviroment -- virtulenv venv
- Activate virtualenv -- venv/scripts/activate (for windows)
- Install dependencies -- pip install -r requirements.txt
- Migrate database -- python manage.py makemigrations -> python manage.py migrate
- Create admin user (superuser) -- python manage.py createsuperuser

- For development you may fill database with dumb data - python manage.py populate_products (from shop app)
                                                         python manage.py populate_posts    (from blog app)
                                                         python manage.py populate_users    (from users app)
