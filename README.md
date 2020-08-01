# blogClone
BLOGClone 
is a django web application which allows user to post their blogs and comments.

Currently it allows only superuser to login, and approve the comments which can therefore be published on the post.

You can download the project, make sure to delete the content of migrations folder inside app and thereafter run,

  -> python manage.py migrate
  -> python manage.py makemigrations app
  -> python manage.py migrate (#again)

then create a superuser using the command python manage.py createsuperuser _enter_your_name_
enter email and password and you're good to go :)

Happy developing!

