# Jira Manager

:construction: WORK GOING ON HERE :construction:

The basic idea is to create an easier overview of your tasks if you work in a
big company in different projects as a developer.

To allow super enterprisy setups with two factor auth or similar the login is
still done manual in a Selenium browser to retrieve the cookies for the
api requests.

## Next steps

### List, Filter & Sort

- Filter by Project (Tag?)
- Filter by My Issues
- Filter by State

### Actions

- Change Issue State

### Improvements

- Store cookies until invalid
- Think of a better idea than Selenium for the login

## Install & Run

```
# copy .env.example to .env and add your details

# install dependencies
poetry install

# run app
poetry run python app/main.py
```
