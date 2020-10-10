# API-Based-
API-Implementation
1. Go to terminal and create virtual env
        virtualenv .env
        then active env.
2. source .env/bin/activate
	Go into project and install pip requirement txt
3. pip install -r requirement.txt
      - Hit the commands
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py runserver
4. Use MySql Local DB to store Shop Data - 
      Database Details -
        ENGINE 	 : 	'django.db.backends.mysql', 
        NAME     : 	'DB_Name'
        USER     : 	'User_Name'	
        PASSWORD : 	'Password'
        HOST     : 	'localhost'
        PORT     : 	'3306'

