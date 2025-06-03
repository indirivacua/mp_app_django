# mp_app_django

```
pip install -r requirements.txt
```

```
django-admin --version
django-admin startproject mp_app .

python manage.py startapp productos

python manage.py makemigrations
python manage.py migrate

python manage.py flush

python manage.py runserver
```

http://127.0.0.1:8000/productos/

```
ngrok config add-authtoken <token>
ngrok http 8000
```