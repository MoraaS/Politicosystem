[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bbcb75a47fed4509a006645dae946fad)](https://app.codacy.com/app/MoraaS/Politicosystem?utm_source=github.com&utm_medium=referral&utm_content=MoraaS/Politicosystem&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/MoraaS/Politicosystem.svg?branch=develop)](https://travis-ci.org/MoraaS/Politicosystem)[![Coverage Status](https://coveralls.io/repos/github/MoraaS/Politicosystem/badge.svg)](https://coveralls.io/github/MoraaS/Politicosystem)
<a href="https://codeclimate.com/github/MoraaS/Politicosystem/maintainability"><img src="https://api.codeclimate.com/v1/badges/0d1a30ed1d095a439fc7/maintainability" /></a>

<h1>Politico</h1>
<p> Politico is a platform used in elections making the voting procedure smooth and efficient</p>

<h2>Requirements</h2>


<h3>Set-up and Installation</h3><br>

<ol>
  <li>Set-up virtual environment</li><br>
  
 In the root directory: virtualenv venv
 
  <li> Activate the virtual environment</li><br>
  
 source venv/bin/activate
 
  <li>Install the requirements</li><br>
  
  pip install -r requirements.txt
  
  <li> Set-up the environment variables</li><br>
  
  export FLASK_APP=run.py<br>
  export FLASK_DEBUG=1<br>
  export FLASK_ENV=development<br>
  
</ol>
<h2>Endpoints</h2>

<table>
  <tr>
    <th>HTTP Method</th>
    <th>Route</th>
    <th> Funtionality</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/v1/offices</td>
    <td>An Admin Can Create Office</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/offices</td>
    <td>A user can get a list of all offices</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/offices/<int:office_id></td>
    <td>A User can get office by id</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/v1/parties</td>
    <td>An admin can create a party</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/parties</td>
    <td>A user can get a list of all parties</td>
    
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/parties/<int:party_id></td>
    <td>A user can get party by id</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>/api/v1/parties/<int:party_id></td>
    <td>An admin can delete party with id</td>
  </tr>
  <tr>
    <td>PATCH</td>
    <td>/api/v1/parties/<int:party_id></td>
    <td>An admin can update party using id to select</td>
  </tr>
</table>

# Setup 

1. Clone repo from github

- `$ git clone https://github.com/MoraaS/Politicosystem`
- `$ cd store-api-v1`
- `$ git checkout dev `

2. Create a virtual environment

`$ python3 -m venv venv`

3. Activate the virtual environment

`$ . venv/bin/activate`

4. Install project dependencies

`$ pip install -r requirements.txt`

5.Running app

`$ python3 run.py: flask run`

# Running tests
`$ pytest tests<br>

 $ python -m pytest --cov=app

# Framework 
Python Flask 

<h2>Author: Salma Moraa </h2>
<h2>Credits: Andela</h2>
