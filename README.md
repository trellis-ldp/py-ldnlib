# Python-based Linked Data Notifications libraries

[![Build Status](https://travis-ci.org/trellis-ldp/py-ldn.png?branch=master)](https://travis-ci.org/trellis-ldp/py-ldn)

This is an implementation of a python3-based [Linked Data Notification](https://www.w3.org/TR/ldn/) sender library.

## Adding an LDN sender to your code

An LDN Sender can be implemented with code such as the following:

```
from ldn.sender import Sender

sender = Sender()

inbox = sender.discover(target_resource)

if inbox is not None:
    sender.send(inbox, data)
```

The `data` value may be a string, a dictionary, a list or an `rdflib`-based Graph.


## Authentication

If the target-resource of inbox-resource require authentication, an `auth` tuple may be supplied:

```
from ldn.sender import Sender

sender = Sender()

inbox = sender.discover(target_resource, auth=(username, password))

if inbox is not None:
    sender.send(inbox, data, auth=(username, password))
```


## Maintainer

[Aaron Coburn](https://github.com/acoburn)

