# Porject

flask-interview-template is a minimum implementation of python flask web framework with peewee orm and sqlite integration.

It's currently used as an interview template for candidates to work on, often onsite.

# Installation

You must have python and pip installed.

To install the dependencies of this project, please `cd` to the root folder of this project and type the following command in the terminal:

```
pip install requirements.txt
```
# Running

Please use the following command in the terminal to run the web application:

```
python app.py
```

You should expect to see a json response like the following in your browser if everything checks out at http://localhost:3000

```
{
  "developer": {
    "creation": "Wed, 14 Dec 2016 19:20:58 GMT",
    "last_login": null,
    "username": "develop",
    "uuid": "71819d38-c232-11e6-ae51-b8e85632d8d8"
  },
  "message": "Hello, World!"
}
```

# Dependencies

## Flask

Please find the Flask tutorials here at http://flask.pocoo.org/docs/0.11/ if you are not previously familiar with it.

## Peewee

Please find the Peewee tutorials here at http://docs.peewee-orm.com/en/latest/peewee/example.html if you are not previously familiar with it.

# Peeking into database

You will be able to access the database directly if you open the sqlite database `coding-exercise.db` with sqlite browser like this one: http://sqlitebrowser.org/

# What's going to happen during the interview

We are going to ask you to implement a few new web endpoints with Flask with a few new database tables.
