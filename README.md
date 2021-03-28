This is a REST API server using flask from a video course from mr. teclado.
It uses flask, sqlalchemy and marshmallow.
The passwords were hashed with bcrypt for security reasons ;)

**Install all packages**

```
pip3 install -r requirements.txt
```

**Config database**

Rename the file /instance/config.py.example to /instance/config.py
Edit the file /instance/config.py

**Make migration**

Make sure to activate the virtual environment (must be on powershell)

```
flask db init
flask db migrate
flask db update
```

**Run the application in development mode**

Make sure to activate the virtual environment (must be on powershell)

```
$env:FLASK_APP="run.py"; $env:FLASK_CONFIG="development"; flask run
```

**Run the tests suit from flask-testing**

Make sure to activate the virtual environment (must be on powershell)

```
python tests.py
```

**Run the application in production mode**

Make sure to activate the virtual environment (must be on powershell)

```
$env:FLASK_APP="run.py"; $env:FLASK_CONFIG="production"; flask run
```
