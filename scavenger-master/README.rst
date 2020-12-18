===============================
Scavenger Hunt
===============================


Requirements
------------

* Django 3.1+
* Python 3.6


Installation
----------------------------

#. Make Virtual environment and activate it.
#. Install all the requirements mentioned in the requirements file using the following command from the same directory of requirements file::

    $ pip install -r requirements.txt


#. Apply migrations::

    $ python manage.py migrate


#. Use the following to run your project::

    $ python manage.py runserver


#. Use the following command to generate qrcodes::

    $ python manage.py make_qrcode

#. Scan the QR codes and data will be filled accordingly on the home page.

#. User will be allowed to proceed further only if all the QR codes are filled properly.

#. After successful completion of the game, all the data will be reset and the user has to scan the QR codes again to play the game.


Production Requirements
________________________

#. Make Debug = False

#. Change the URL in the make_qrcode.py file to your production URL.

#. Change the URL in index.html and question.html file present under the script tag to your production URL.

#. To reset game after successful completion, uncomment "localStorage.clear()" from badge.html.


