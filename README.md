Video Link:
C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\1.Python Django Project - Ecommerce Store (2021) - Part 1 - Building models, views and testing.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\2.Python Django-Build an ecommerce basket with session handling.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\3.Python Django - Build a user, payment and order management system_2.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\4.Python Django - Refactoring the Ecommerce Store Templates.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\5.Python Django Ecommerce Multi-Product Types Database Implementation_2.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\6.Python Django Ecommerce CRUD and UUID - Managing multiple addresses.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\7.Python Django Ecommerce Customer Wish List.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\8.Python Django Ecommerce PayPal Integration.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\9.Python - Django - Ecommerce - Refactor Folder Structure & Pytest Introduction.mp4

C:\Users\admin\Downloads\Video\Python Django Project - Ecommerce Store (2021)\10.Python - Django - Ecommerce - Pytest Testing including Factory Boy.mp4

Video Timeline::

# master

    -Starting Project structure with core app
    -store app created
    -Seperate settings has been set on 'settings'
    -Static folder has been added to project
    -Homepage url setup by urls
    -Created Requirement text by cmd__ 'pip freeze > requirements.txt'

# 01

    -Category and Product Model created
    -For image media file handling installed cmd__ 'pip install Pillow'
    -Databse 'makemigrations' and 'migrate' done
    -Creating Superuser as 'admin' and Password '1234' by cmd__ 'createsuperuser'
    -Configuring Media Folder on settings
    -Added some demo data on database
    -basket app creatd
    -basket context_processors added to settings
    -Basket Summary Page Created
    -Basket Class Created
    -Basket Class Interaction (add, update, delete) on Basket Summary Page

# 02

    -Restructure of Navbar on Header and Basket on Summary
    -User Management
        --Custom Model: 00:35:00
            * django-countries package installed by cmd and added to UserBase model
            * Deleted old datavase and migrations file and newly makemigrations and migrate done
        --Signup Process(email confirmation): 00:53:30
            * six package installed
            * Sending Email confirmation on console: 01:06:00
            * Activating User from Link and Redirect to Dashboard with Login Authentication: 01:39:10
        --Login/Logout Facilities: 01:58:20
        --Dashboard Update User: 02:12:00
        --Dashboard Delete User: 02:21:15
        --User Password Reset: 02:27:35
    -Payment (03:07:45)
        --Template created and Checkout button Implemented: 03:17:45
        --Gathering Order Info for Building Payment Intent: 03:27:30
        --Stripe Element: 03:37:10
    -Order (04:02:24)
        --Order Models Created and Migrated
        --Order updated with Payment Status (04:23:10)
        --Order show in dashboard (04:37:10)

# 03
