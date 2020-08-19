FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user/app


# Installing required system depencies

RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    python3 -m pip install --no-cache-dir pip-tools


# Install python dependencies

RUN pip install -r requirements/base_requirements.txt && \
    pip install -r requirements/addition_requirements.txt


# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm /var/lib/apt/lists/* rm -rf /var/cache/apt/*

USER user
CMD gunicorn tmovie.wsgi --log-file - -b 0.0.0.0:8000 --reload