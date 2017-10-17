# Python-based Linked Data Notifications libraries

[![Version](https://img.shields.io/pypi/v/py-ldnlib.svg)](https://pypi.python.org/pypi/py-ldnlib)
[![Python Versions](https://img.shields.io/pypi/pyversions/py-ldnlib.svg)](https://pypi.python.org/pypi/py-ldnlib)
[![Build Status](https://travis-ci.org/trellis-ldp/py-ldnlib.png?branch=master)](https://travis-ci.org/trellis-ldp/py-ldnlib)
[![Build status](https://ci.appveyor.com/api/projects/status/m7tl8ak46ihteouo?svg=true)](https://ci.appveyor.com/project/acoburn/py-ldnlib)
[![Coverage Status](https://coveralls.io/repos/github/trellis-ldp/py-ldnlib/badge.svg?branch=master)](https://coveralls.io/github/trellis-ldp/py-ldnlib?branch=master)

This is an implementation of a python3-based [Linked Data Notification](https://www.w3.org/TR/ldn/) sender and consumer.


## Adding an LDN sender to your code

A simple LDN Sender could be written as:

```
import ldnlib

sender = ldnlib.Sender()

inbox = sender.discover(target_resource)

if inbox is not None:
    sender.send(inbox, data)
```

The `data` value may be a string, a dictionary, a list or an `rdflib`-based Graph.


## Adding an LDN consumer to your code

A simple LDN Consumer could be written as:

```
import ldnlib

consumer = ldnlib.Consumer()

inbox = consumer.discover(target_resource)

if inbox is not None:
    for iri in consumer.notifications(inbox):
        // fetch the notification as a Python dictionary
        notification = consumer.notification(iri)
```


## Authentication

If the target-resource or inbox-resource requires authentication, an `auth` tuple may be supplied:

```
import ldnlib

sender = ldnlib.Sender()

inbox = sender.discover(target_resource, auth=(username, password))

if inbox is not None:
    sender.send(inbox, data, auth=(username, password))
```


## Maintainer

[Aaron Coburn](https://github.com/acoburn)

