Alerta Hogar
===================================


Vamos a registrar agresiones en el hogar: insultos, discriminación, ofensas


Postgres DB
-----------
Using [Postgres Docker stack](https://gist.github.com/adagio/e1a7b6edbc0f2c21e32e0cec30a07baa)


Basic Commands
--------------

with venv activated:

```
pip install -r requirements.txt
cd alertas
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```
