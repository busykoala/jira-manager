# Jira Manager

This is work in progress. The basic idea is to create a better overview of jira
tasks if you work in a big company in different projects.

You will have to login manually (on start up login to your jira and proceed in
the shell). That process will make sure the cookies are stored to do the
following requests. This is necessary for the case that your company has setup
some two factor authentication processes or has similar mechanisms.

## Install & Run

```
# copy .env.example to .env and add your details

# install dependencies
poetry install

# run app
poetry run python app/main.py
```
