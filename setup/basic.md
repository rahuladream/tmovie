
# Basic Installation & setup


```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev nginx
```


# Create a virtual environment

```
virtualenv -p python3 venv
```


# Install packages

```
pip install -r requirements.txt
```


# Run Migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Run Tests

```
python3 manage.py tests app.authentication.tests

python3 manage.py tests app.movies.tests

```

# Run server & use api

```
python3 manage.py runserver
```

## API Information can be found here: 

```
https://docs.google.com/document/d/1m1G9PMt2kI-cGnISAQsapfX-o-LGgMjknpwn6eZyxVE/edit?usp=sharing
```