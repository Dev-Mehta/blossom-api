# API for Blossom Project - Online nursery and plants diary app

## Table of Contents
- [API for Blossom Project - Online nursery and plants diary app](#api-for-blossom-project---online-nursery-and-plants-diary-app)
  * [Installation](#installation)
    + [Step 1 : Clone the repo](#step-1---clone-the-repo)
    + [Step 2 : Create a virtual enviroment for the project and activate it](#step-2---create-a-virtual-enviroment-for-the-project-and-activate-it)
      - [For windows](#for-windows)
      - [For Unix based systems](#for-unix-based-systems)
    + [Step 3 : Install the dependencies/requirements to run this project](#step-3---install-the-dependencies-requirements-to-run-this-project)
    + [Step 4 : Run the Server and start making requests:fire:.](#step-4---run-the-server-and-start-making-requests-fire-)
  * [Usage 🚀👨‍💻](#usage--------)

## Installation
### Step 1 : Clone the repo
```
git clone https://github.com/Dev-Mehta/blossom-api.git
```
### Step 2 : Create a virtual enviroment for the project and activate it
 ```
 pip install virtualenv
 virtualenv env
 ```
 **Activate the virtualenv**
 #### For windows
 ```
 env\Scripts\activate
 ```
 #### For Unix based systems
 ```
 source env/bin/activate
 ```
 ### Step 3 : Install the dependencies/requirements to run this project
 ```
 pip install -r requirements.txt
 ```
 ### Step 4 : Run the Server and start making requests:fire:.
 ```
 python manage.py runserver
 ```
## Usage 🚀👨‍💻
| Endpoint                | Description                                                                  | Request Method |
|-------------------------|------------------------------------------------------------------------------|----------------|
| /api/consumer/register/ | Register a client/consumer for the app                                       | POST           |
| /api/seller/register/   | Register a seller for the app<br>(The nursery which would be selling plants) | POST           |
| /api/consumer/login/    | Login a client/consumer to the app                                           | POST           |
| /api/seller/login/      | Login a seller to the dashboard app                                          | POST           |
| /api/seller/add-plant/  | Add a plant to the catalogue of nursery                                      | PUT            |
