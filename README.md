# Butyplast site


## What's included?

* Blueprints
* Flask-SQLAlchemy for databases
* mysql-connector
* Flask-WTF for forms
* Flask-Login
* Flask-Security
* Flask-Admin
* Flask-BabelEx
* Flask-Uploads

## Setting up

* Clone the repo
* $ git clone <https://github.com/Andreyinweb/butyplast.git>
* Create a virtual environment
* $ python3 -m venv venv
* $ source venv/bin/activate
* $ cd butyplast
* $ pip3 install -r requirements.txt
* 

* Сreate file config.env

# Database

* $ mysql -u root -p
* \>>  create database [name database] character set utf8 collate utf8_unicode_ci;
* \>>  exit;

# Running the application                       

* $ cd butyplastsite
* $ python3 main.py

# Fill the database

* Open the catalog z_run_base
* File data: worddict.py
* Folder for image: images 
* $ python3 run.py