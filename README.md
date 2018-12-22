# [Django E-Commerce Mini-Project](https://ddeveloper72-ecommerce.herokuapp.com)
## The Full Stack: bringing it all together in Django...
#### *A part of Full Stack Development*


Welcome to my write up on the Django tutorial, which I followed using both VSCode and Cloud 9

[![Build Status](https://travis-ci.org/ddeveloper72/Django-e-commerce.svg?branch=master)](https://travis-ci.org/ddeveloper72/Django-e-commerce)




The tutorial was taught by the
[Code Institute](https://courses.codeinstitute.net/)

This tutorial focuses on bringing everything together, that we have learned so far, as software developers.  It's about recapping on knowledge and building on our experience.

In this tutorial, we create an actual working ecommerce website. To begin with, we used the accounts app from the Django Authorization tutorial; there is no need to rewrite good code!  Then we build a products app with a model to showcase items we are retailing. Remember our models are for creating our tables in our SQL database.

Once our products app is working, we then crate a shopping cart which works in the current session and a checkout app, which takes the session data and moves it into a table based on a checkout model as soon as the user is logged in.

Things that are new in this tutorial is that we create a Stripe account as well as an Amazon AWS account.

Stripe is fantastic background service that processes all the financial services for our ecommerce application. Stripe handles the money trail and insures the security of the financial transaction from your customers payment to your ecommerce store account.  To find out  more about [Stripe](https://stripe.com/ie), have a look at their support documentation.

[Amazon AWS](https://aws.amazon.com) provide a very powerful tool for helping us realize the ecommerce site.  Amazon AWS let us crate a online bucket, into which we can store all of our media, which would normally be lost on Heroku.  Files such as the product images that are changed frequently will no longer be lost.  But in addition to this, Amazon AWS will also host all of our CSS, JavaScript files and Font-Awesome files (Some developers recommend using the Font-Awesome CDN links instead, so as to maintain access to the most uptodate icons), which for the purpose of this tutorial, demonstrates the service really well.

## 1. First things first. The backend structure of the application uses

   * Django with SQLite3 developer backend.
   * Heroku postgresql for our production deployment.
   * Customer authentication handled by Django auth models.
   * Our app tree structure:

````
├── index
├── accounts
│   ├── templates
│   ├── backends
│   ├── forms
│   ├── urls_reset
│   └── views
├── cart
│   ├── templates
│   ├── contexts
│   ├── urls
│   └── views
├── checkout
│   ├── templates
│   ├── admin
│   ├── forms
│   ├── models
│   ├── urls
│   └── views
├── ecommerce
│   ├── settings
│   ├── urls
│   └── wsgi
├──home
│   ├── templates
│   └── views
├──media
│   └── images
├── products
│   ├── templates
│   ├── models
│   ├── urls
│   └── views
├── search
│   ├── urls
│   └── views
├──static
│   ├── css
│   ├── font-awsome
│   │   ├── css
│   │   └── webfonts
│   └── js
├── templates
├── custom_storages
└── manage
````

## 2. The Cart app

````
└── cart
       ├── templates
       ├── contexts
       ├── urls
       └── views
````

### The Views

   * The carts view is made up of different elements:
  
        1 view_cart,
        2 add_to_cart - where we take the id of the object and added it to the cart
        3 adjust_cart - the quantity of the id can be changed, so that the item can be removed or updated.

## 3. The Checkout app

````
└── checkout
    ├── templates
    ├── admin
    ├── forms
    ├── models
    ├── urls
    └── views
````
### The forms

* Checkout uses a MakePaymentForm and a OrderForm. The MakePaymentForm provides the customer with input fields for their credit card information which will be picked up by Stripe.
* The OrderForm passes the customer's contact details to the order model.

### The models

* Checkout uses two models, for the order and for the orderLineItem. The order model takes the customer's address information from the order form.
* The orderLineItem assigns the product being ordered, the quantity, to the order

### The Views

* Checkout requires that the customer is logged in, to be able to process the order.
* The payment process goes through a process of validation which is tied in with Stripe.  Stripe provides the view with live information on the processing status of the payment.
* On our end, what we re concerned with, is the information that the customer gives us.  Firstly the order form data and the payment form data is is valid, then apply the current date/time and save with the user information. We then do the math on the cart items to generate a financial total for each the the product id.  The financial information is then submitted to Stripe for processing, while we use the customer's email as our own id for the order.
* What happens next, depends on what Stripe's response is to the customer's payment details.
  1. Stripe my return a CardError in which case, payment from card was declined.
  2. If the payment is successful, we return the payment was successful and we then empty the shopping cart.
  3. If there is an error processing the payment, we return an error message.
  4. If there is an error in the payment form data, we return a message saying there is a that we were unable to take payment with the card details that they provided.
  5. Lastly if everything is good and the payment goes through, we pass the payment_form data to the MakePaymentForm model and the order_form to the OrderForm.

## 4. The Products app

````
└── products
    ├── templates
    ├── models
    ├── urls
    └── views
````

### The models

* Checkout uses one model, to show the product name, description, price and of course and image.

### The Views

* Our view returns everything from the products model to the products.html

## 5. The Search app

````
└── search
    ├── urls
    └── views
````

### The Views

   * The view lets us apply a filter to the products using a `name__icontains` and returning the product id found, to products.html.


## 6. Useful development tips and lessons learned

   * From the start of this tutorial, I used Travis automated testing. It's great till one runs in to anything but a green badge and then one starts to wonder who is looking at my build failing.  I'm proud to say, I had loads of failed builds.  Travis is very useful as a debug tool as well because even though I had a perfectly good working product live and online, I still had environmental variable selection issues with my development database selection switch.  

   * I spent at least 40% of my time debugging the applications as they were written.  The majority of my problems came from spelling errors when taking down notes from the tutorial. Other errors came from automation in VSCode where I use closing automatic closing brackets created, for example,
  `<form method="post" action="{% url 'add_to_cart' product.id %}"></form>`  some code here, and then, `<button class="btn btn-success" type="submit">Add</button>`  
  
  * Relocating `</form>` to the end of my form, was all it took to resolve why nothing was being added to my shopping cart.
  I also ran into incorrect syntax errors, where I had used `redirect(request('view_cart'))` instead of `return redirect(reverse('view_cart'))`.

  * Trying to debug payment declined errors when using stripe, was one of the silliest errors I had made.  I found the error in my checkout models, where I had written def `__self__(self):` instead of `__str__(self):`, so I was never returning the string for my orders and so I kept getting a required field was missing error.  The error took me the longest to discover, because I immediately went to debug what was new and different in this project, which was the stipe JavaScript. I never thought to think that in all the models that I had written, one was incorrect.  I found it by doing a like for like comparison with my other models then realized my error.

* Another error that I discovered was when I wanted to add new products to my production database from the live website. I kept getting an authentication error, then realised that I hadn't added my Amazon AWS keys to my config vars.  That problem was the very quickly resolved.


## 7. Setting up the environmental variables for use with VSCode

### From settings.py in Django

#### Setting up the allowed hosts for VSCode and Cloud 9

````python
ALLOWED_HOSTS = [
    'ddeveloper72-ecommerce.herokuapp.com',
    os.environ.get('C9_HOSTNAME'),
    os.environ.get('localhost', '127.0.0.1')
]
````
#### Setting up the os VSCode.

(enable `inport env` for use on Cloud 9)

````python
import os

# import env

import dj_database_url
````

#### Setting up the development & debug mode environments in VSCode and Cloud 9

````python
# Switch Debug between True and False
if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False
````

````python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = development
````

#### Setting up a if else switch to select the production or development SQL database VSCode, which works with Travis testing.

````python
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) } 
else:
    print("Database URL not found. Using SQLite instead")
    DATABASES =  {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
````

#### Setting up the requirements for the email interface

````python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
````

### From .vscode settings.json
The reason why I'm showing this, is because one of the most challenging aspects that I have while learning coding, had been learning to use the development software and configuring environments.  Learning to Understanding ones tools for coding is as essential as the projects themselves.

````javascript
"terminal.integrated.env.windows": {
        "DEVELOPMENT": "True",
        "SECRET_KEY": "secret_key",
        "ADMIN": "admin pass",
        "DJANGO_SETTINGS_MODULE": "ecommerce.settings",
        "DATABASE_URL": "your_database_url_here",
        "STRIPE_PUBLISHABLE": "your_stripe_publishable_key",
        "STRIPE_SECRET": "your_stripe_secret_key",
        "AWS_ACCESS_KEY_ID": "your_AWS_access_key_ID",
        "AWS_SECRET_ACCESS_KEY": "your_AWS_secret_access_key",
        "EMAIL_ADDRESS": "your_email_address",
        "EMAIL_PASSWORD": "your_email_account_login_password",
          }

````

### in your env.py, used on Cloud 9, that you have added to .gitignore

````python
import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "your_stripe_publishable_key")
os.environ.setdefault("STRIPE_SECRET", "your_stripe_secret_key")
os.environ.setdefault("SECRET_KEY", "secret_key")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "your_AWS_access_key_ID")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your_AWS_secret_access_key")
os.environ.setdefault("DATABASE_URL", "your_database_url_here")
os.environ.setdefault("EMAIL_ADDRESS", "your_email_address)
os.environ.setdefault("EMAIL_PASSWORD", "your_email_account_login_password")
````