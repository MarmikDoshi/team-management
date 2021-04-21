# Django Team Management App
Team management application written in Django 

**Pre-requisites:**
- python3


## Create a virtualenv for python 3
```
virtualenv -p python3 virtualenvname
```

##Activate the virtualenv
```
source virtualenvname/bin/activate
```

## Change directory to team-management-app
```
cd team-management-app/
```

## Install dependencies
```
pip install -r requirements.txt
```

## Update database settings
Create database in mysql as 'team_management' and update User and Password field in the settings.py file as per local system mysql settings
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'team_management',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## In the main project directory which is teammanager folder run the following command to run migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Run the application
```
python manage.py runserver
```

## Test the APIs:
```
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/users/ -d '{"first_name": "Joe", "last_name": "Burns", "email": "joe.burns@gmail.com", "phone_number": "+911234567890", "role": "RE"}'
```