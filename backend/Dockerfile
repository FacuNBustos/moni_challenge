FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
RUN python3 manage.py migrate

CMD [ "gunicorn", "-c", "config/gunicorn/config.py", "--bind", ":8000", "--chdir", "config", "wsgi:application" ]