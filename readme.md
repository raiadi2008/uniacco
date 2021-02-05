# Setup
cd to backend folder where manage.py lived

run following comand

python -m venv env
env/Scripts/active
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt

# run server
python manage.py runserver



# registrtation request

endpoint = http://127.0.0.1:8000/api/users/login

format
{
    "username": "<username>"
    "password": "<password>"
}

# login request 

endpoint = http://127.0.0.1:8000/api/users/login

format
{
    "username": "<username>"
    "password": "<password>"
}