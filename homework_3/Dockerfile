FROM python:3-slim-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

COPY hw_3.py hw_3.py

CMD python hw_3.py
