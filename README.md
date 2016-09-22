scrap-groceries is a command line tool that scrap the supplied URL (that must
to be a Sainsbury's grocery product list page) and return a JSON with
significant information for each product.

~~~ sh
$ scrap-groceries http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html
~~~

There is the `--pretty/-p` attribute to show the output indented.


Installation
============

Dependencies:

* **Python 2.7+**
* requests
* lxml
* cssselect
* simplejson

~~~ sh
$ git clone https://github.com/gbarba/sainsbury_technical_test.git
$ cd sainsbury_technical_test
$ pip install -r requirements.txt
$ python setup.py install
~~~


Run tests
=========

From the root of repository, you can run tests using setuptools:

~~~ sh
$ python setup.py test
~~~

or executing the tests script:

~~~ sh
$ python tests/test_scrap_groceries.py
~~~
