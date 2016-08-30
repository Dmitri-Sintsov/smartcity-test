==============
smartcity test
==============

Installation
------------

.. highlight:: shell

In Ubuntu 14.04 LTS::

    python3 -m venv smartcity_test
    cd smartcity_test
    source bin/activate
    git clone https://github.com/Dmitri-Sintsov/smartcity-test.git
    cd smartcity-test
    python3 -m pip install -U -r requirements.txt
    python manage.py makemigrations smartcity_product
    python manage.py migrate

