# Setup
cd to backend folder where manage.py lived

run following comand <br/>

python -m venv env <br/>
env/Scripts/active <br/>
pip install django <br/>
pip install djangorestframework <br/>
pip install djangorestframework-simplejwt <br/>

# run server
python manage.py runserver<br/>



# registrtation request

endpoint = http://127.0.0.1:8000/api/users/login <br/>

format<br/>
{<br/>
    "username": "<username>", <br/>
    "password": "<password>"<br/>
}<br/>

# login request 

endpoint = http://127.0.0.1:8000/api/users/login <br/>

format<br/>
{<br/>
    "username": "<username>",<br/>
    "password": "<password>"<br/>
}<br/>
