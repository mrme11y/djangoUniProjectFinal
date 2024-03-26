READ ME

WEBSITE URL
-----------------
https://djangouniprojectfinal-61eddaacee54.herokuapp.com/

ADMIN, USER LOGIN AND HELPDESK TICKETS SYSTEM
-----------------

ADMIN PANEL
- For the admin panel, you can login with the following credentials (Admin and Manager):
- https://djangouniprojectfinal-61eddaacee54.herokuapp.com/admin/

HELPDESK TICKETS SYSTEM USER LOGIN PAGE
- For the helpdesk tickets system, you can login with the following credentials (Admin, Manager or Helpdesk Agents):
- https://djangouniprojectfinal-61eddaacee54.herokuapp.com/user_login/

HELPDESK TICKETS SYSTEM DASHBOARD
- and then go to the below for the dashboard
- https://djangouniprojectfinal-61eddaacee54.herokuapp.com/tickets/

USER LOGIN CREDENTIALS
-----------------

ADMIN
-----------------
With the Admin User you are able to create new managers and helpdesk agents and you have full rights to the system. This includes creating, viewing and deleting helpdesk tickets.
Username: admin
Password: admin1234

MANAGER
-----------------
Managers also have access to the Admin Panel but with limited rights. They can only create new helpdesk agents. Managers can also create new helpdesk tickets, view helpdesk tickets and delete helpdesk tickets.
Username: manager1
Password: iamapassword

HELPDESK AGENTS
-----------------
You are not allowed to view or access the admin panel with any helpdesk agent account. These are only used to create new helpdesk tickets and view helpdesk tickets.
Username: helpdeskagent1
Password: hda12345

Username: helpdeskagent2
Password: hda12345

HOW TO ADD A HELPDESK TICKET (signed in as a helpdesk agent)
-----------------
1. Login with the helpdesk agent credentials
2. Go to the helpdesk tickets system dashboard
3. Click on the "Create a new ticket" button
4. Fill in the form and click on the "Create Ticket" button

HOW TO UPDATE A TICKET (signed in as a helpdesk agent)
-----------------
1. Login with the helpdesk agent credentials
2. Go to the helpdesk tickets system dashboard
3. Click on the "View" button (eye symbol) on the right hand side of the ticket you want to update
4. Click on the green "Update ticket" button
5. Fill in the form and click on the orange "Update ticket" button

HOW TO DELETE A TICKET (signed in as a helpdesk agent)
-----------------
1. Login with the manager credentials
2. Go to the helpdesk tickets system dashboard
3. Click on the "View" button (eye symbol) on the right hand side of the ticket you want to delete
4. Click on the red "Delete ticket" button
5. Confirm the deletion by clicking on the "Delete" button

HOW TO ADD A MANAGER (signed in as an admin)
-----------------
TODO

GIT REPOSITORY
-----------------
https://github.com/mrme11y/djangoUniProjectFinal/

HOW TO RUN THE APP LOCALLY
-----------------
1. Clone the repository
2. Install the requirements/dependencies
3. Run the server with the command `python manage.py runserver`
4. Open the browser and go to http://127.0.0.1:8000/user_login/
5. You can now login with the credentials above
6. You can also access the admin panel by going to http://127.0.0.1:8000/admin/
7. You can also access the helpdesk ticket system by going to http://127.0.0.1:8000/tickets/

HOW TO RUN THE APP ON HEROKU
-----------------
You simply need to click on the link (WEBSITE LOGIN URL https://djangouniprojectfinal-61eddaacee54.herokuapp.com/user_login/ ) and you will be taken to the website. You can then login with the credentials above.

HOW TO RUN THE TESTS
-----------------
TODO

DEPENDENCIES
-----------------
- asgiref = "==3.7.2"
- brotli = "==1.1.0"
- certifi = "==2024.2.2"
- charset-normalizer = "==3.3.2"
- crispy-bootstrap4 = "==2024.1"
- distlib = "==0.3.8"
- dj-database-url = "==2.1.0"
- django = "==5.0.2"
- django-crispy-forms = "==2.1"
- filelock = "==3.13.1"
- gunicorn = "==21.2.0"
- idna = "==3.6"
- packaging = "==23.2"
- pipenv = "==2023.12.1"
- platformdirs = "==4.2.0"
- requests = "==2.31.0"
- sqlparse = "==0.4.4"
- typing-extensions = "==4.10.0"
- urllib3 = "==2.2.1"
- virtualenv = "==20.25.1"
- whitenoise = "==6.6.0"

REQUIRED PYTHON VERSION = "3.12"

