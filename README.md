# TrainMan Recruitement Project API

## Project Moto

[![Build Status](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME}.png?branch=master)](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME})

Coverage build

.. image:: https://cdn.rawgit.com/dbrgn/coverage-badge/master/example.svg
    :alt: coverage badge

For a movie rating app, create a django rest api using ```django rest framework```. The app needs to have the capability to 
list movies, 
logged in users can save movies to a watchlist or mark them watched.  
logged in users can view list of movies in their watchlist or watched list.
Build the corresponding rest APIs.

To populate the movies in your database, create a scraper to scrape IMDb’s top list (https://www.imdb.com/chart/top/). The scrapper should follow each movie’s url and extract details from the movie’s page. The details you want to save are up to you. The more the better.
This scraper should ideally be triggered by an endpoint in your django api and accept any similar url e.g. https://www.imdb.com/india/top-rated-indian-movies.
Already existing movies should be only updated. Not replaced/duplicated.

#### Few points to keep in mind

* use django-rest-framework
* use pipenv/virtualenv etc to make the project easy to setup for anyone, add a setup file
* use sqlite as database for portability
* users should be able to sign up and login, use token authentication
* take care of permissions - users cannot delete a movie, view other users’ watched list etc
