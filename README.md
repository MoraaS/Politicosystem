[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bbcb75a47fed4509a006645dae946fad)](https://app.codacy.com/app/MoraaS/Politicosystem?utm_source=github.com&utm_medium=referral&utm_content=MoraaS/Politicosystem&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/MoraaS/Politicosystem.svg?branch=develop)](https://travis-ci.org/MoraaS/Politicosystem)[![Coverage Status](https://coveralls.io/repos/github/MoraaS/Politicosystem/badge.svg)](https://coveralls.io/github/MoraaS/Politicosystem)
<a href="https://codeclimate.com/github/MoraaS/Politicosystem/maintainability"><img src="https://api.codeclimate.com/v1/badges/0d1a30ed1d095a439fc7/maintainability" /></a>

# POLITICO

 >Politico is a platform used in elections making the voting procedure smooth and efficient

# Setup and Installation

1 Clone repo from github

> - git clone https://github.com/MoraaS/Politicosystem
> - cd Politicosystem
>- git checkout develop branch'

2 Create a virtual environment

> - python3 -m venv venv`

3 Activate the virtual environment

> - venv/bin/activate

4 Install project dependencies

> - pip install -r requirements.txt`

# Running Application 

While on the terminal of the Politicosystem:

> - set APP_SETTING variable by: EXPORT APP_SETTING=development
> - Set application entry point by: EXPORT FLASK_APP=run

# Running tests

>- For pytest- pytest tests
>- For intergrating coverals in tests- python -m pytest --cov=app

# Framework

> Python Flask

# Endpoints

| HTTP Method   | URL Endpoint  | Description  |
| -------- | ------------------------------------ | ---------------- |
| POST   | /api/v1/offices                   | An Admin Can Create Office |
| GET    | /api/v1/offices                    | A user can get a list of all offices |
| GET  | /api/v1/offices/<int:office_id>    | A User can get office by id |
| POST    | /api/v1/parties                    | An admin can create a party |
| GET  | /api/v1/parties | A user can get a list of all parties |
| GET   | /api/v1/parties/<int:party_id>      | A user can get party by id |
| DELETE  | /api/v1/parties/<int:party_id> | An admin can delete party with id |
| PATCH | /api/v1/parties/<int:party_id>/name | An admin can update party using id to select|

## Author: Salma Moraa 

## Credits: Andela
