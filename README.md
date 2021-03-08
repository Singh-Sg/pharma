# E-Precscription-Service

The E-Precscription-Service is responsible to generate the precscription for the patient and place the order. 

# Steps to install and run E-Precscription-Service on your local machine:-

* Run `$ pip install virtualenv` command to install virtual environment
* Run `$ virtualenv env -p python3.7` command to Create Virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment
* Run `$ git clone ##` command for cloning the project
* Run `$ cd pharma` command for jump into the project directory
* Run `$ pip install -r requirements.txt` command to Install project requirement file
* Run `$ python manage.py migrate` command to apply migrations on your local machine
* Run `$ python manage.py runserver` command to run project on your local machine


# Work Structure:-

* Create superuser through terminal, Run command:-
    ```
    $ python manage.py createsuperuser
    username:-admin
    email:-admin@gmail.com
    password:-1234!@#$
    ```
* Run `$ python manage.py runserver` command to run project on your local machine.

* Can see `API-DOCS` & `model structure` & `request api` by calling this:-
    - `http://127.0.0.1:8000/api-doc/`
    - `http://127.0.0.1:8000/swagger/`

* Go to admin panel `http://127.0.0.1:8000/admin` and login with superuser.

* Create `users` and then create `Doctor` and `Patient` through admin panel.

* Can create `Drugs`and `Precscription` through admin panel(optional).

* Can use `POSTMAN` for calling API's.

* Now Generate auth token for authentication:-
    - run `python manage.py drf_create_token your_user_name` on terminal.
    OR
    -run this `http://127.0.0.1:8000/api-token-auth/` with crediantial(username & password).

* Now can generate a Precscription by calling this API using `POST` request with token which you have      genrated:-
    - `http://127.0.0.1:8000/api/precscription/` with data example:-
    doctor:doctor_id
    patient:patient_id
    drugs:["drug_name1", "drug_name2"]

* Can fetch all Precscription by callig API using `GET` request with auth token:-
    - `http://127.0.0.1:8000/api/precscription/`

* Can fetch single Precscription by callig API using `GET` request with auth token:-
    - `http://127.0.0.1:8000/api/precscription/{id}`

* Can see order which automatically created after Precscription saved on admin section.


# Running the Tests
* Run `$ cd pharma` command for jump into the project directory
* Run `$ python3 manage.py test` command for run all test cases


# Running Tests Coverage
* Run `$ cd pharma` command for jump into the project directory
* Run `$ coverage run --source='.' manage.py test` for run test cases with coverage
* Run `$ coverage html`  to see the result


# Third party libraries:
1. `rest_framework.authtoken` :- Used to generate token for a user.

2. `django-service-objects`:- To write a logic.

3. `drf_yasg`:- A Swagger generation tool and library available for Django. Using drf-yasg, you can create APIs in a more organized and user-friendly way than is possible with the default structures provided by Django. 