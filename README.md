# indicatorVC

Indicator "version control" for the CI process at MUN.

A Django webservice built to store indicator information and allow it to be easy to update.

To get the project running, a few things have to be done first:
- Install Django (i.e. pip install django in the command line)
- Install any backend dependencies that your database requires (this project uses MySQL by default, but that can be reconfigured)
- In the indicatorVC folder, there is a file called settings.py. The DATABASES section of that file needs to be properly configured to use the webservice
- The .sql and .csv files in the repository are MySQL queries to properly pre-load the database. If/once you have a MySQL database connected to the webservice, run those queries to populate the database

For more information, see the Django tutorial at https://docs.djangoproject.com/en/2.1/intro/tutorial01/
