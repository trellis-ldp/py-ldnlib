
Python-based Linked Data Notifications libraries
================================================


.. image:: https://badge.fury.io/py/py-ldnlib.svg
   :target: https://badge.fury.io/py/py-ldnlib
   :alt: Version


.. image:: https://img.shields.io/pypi/pyversions/py-ldnlib.svg
   :target: https://pypi.python.org/pypi/py-ldnlib
   :alt: Python Versions


.. image:: https://travis-ci.com/trellis-ldp/py-ldnlib.svg?branch=master
   :target: https://travis-ci.com/trellis-ldp/py-ldnlib
   :alt: Build Status


.. image:: https://ci.appveyor.com/api/projects/status/m7tl8ak46ihteouo?svg=true
   :target: https://ci.appveyor.com/project/acoburn/py-ldnlib
   :alt: Build status


.. image:: https://coveralls.io/repos/github/trellis-ldp/py-ldnlib/badge.svg?branch=master
   :target: https://coveralls.io/github/trellis-ldp/py-ldnlib?branch=master
   :alt: Coverage Status


This is an implementation of a python3-based `Linked Data Notification <https://www.w3.org/TR/ldn/>`_ sender and consumer.

Installing
----------

``pip install py-ldplib``

Adding an LDN sender to your code
---------------------------------

A simple LDN Sender could be written as:

.. code-block::

   import ldnlib

   sender = ldnlib.Sender()

   inbox = sender.discover(target_resource)

   if inbox is not None:
       sender.send(inbox, data)

The ``data`` value may be a string, a dictionary, a list or an ``rdflib``\ -based Graph.

Adding an LDN consumer to your code
-----------------------------------

A simple LDN Consumer could be written as:

.. code-block::

   import ldnlib

   consumer = ldnlib.Consumer()

   inbox = consumer.discover(target_resource)

   if inbox is not None:
       for iri in consumer.notifications(inbox):
           // fetch the notification as a Python dictionary
           notification = consumer.notification(iri)

Authentication
--------------

If the target-resource or inbox-resource requires authentication, an ``auth`` tuple may be supplied:

.. code-block::

   import ldnlib

   sender = ldnlib.Sender()

   inbox = sender.discover(target_resource, auth=(username, password))

   if inbox is not None:
       sender.send(inbox, data, auth=(username, password))

Maintainer
----------

`Aaron Coburn <https://github.com/acoburn>`_
