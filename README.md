# Python-based Linked Data Notifications libraries

[![Build Status](https://travis-ci.org/trellis-ldp/py-ldn.png?branch=master)](https://travis-ci.org/trellis-ldp/py-ldn)

This is an implementation of a python-based [Linked Data Notification](https://www.w3.org/TR/ldn/) sender.

## Writing a LDN sender

```
from ldn.sender import Sender

sender = Sender()

inbox = sender.discover(target_resource)

if inbox is not None:
    sender.send(inbox, data)
```

The `data` value may be a string, a dictionary, a list or an `rdflib`-based Graph.

## Maintainer

[Aaron Coburn](https://github.com/acoburn)

