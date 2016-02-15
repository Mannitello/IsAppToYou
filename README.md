How to deploy
==============

Commit changes
----------------

* git add -A .

* git commit -m "message here"

Push to Git
--------------

* git push  ------> Username: Mannitello, pwd: Mannitello88

In a PythonAnywhere Bash console:
----------------------------------

* cd isapptoyou

* source env/bin/activate

* git pull

* python manage.py collectstatic

* hop on over to the Web tab and hit Reload.