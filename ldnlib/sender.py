from rdflib import Graph, URIRef
import requests

import ipaddress
import json
import socket
from urllib.parse import urlparse

LDP_INBOX = "http://www.w3.org/ns/ldp#inbox"
JSON_LD = "application/ld+json"
ACCEPT_HEADERS = ("application/ld+json; q=1.0,"
                  "text/turtle; q=0.9,"
                  "application/xml+rdf; q=0.5")


class Sender(object):

    def __init__(self, **kwargs):
        self.allow_localhost = kwargs.get('allow_localhost', False)
        self.accept_headers = kwargs.get('accept_headers', ACCEPT_HEADERS)

    def __discover_head(self, target, **kwargs):
        r = requests.head(target, allow_redirects=True,
                          auth=kwargs.get('auth'))
        r.raise_for_status()
        if LDP_INBOX in r.links:
            return r.links[LDP_INBOX].get('url')

    def __discover_get(self, target, **kwargs):
        headers = {'accept': self.accept_headers}
        r = requests.get(target, auth=kwargs.get('auth'), headers=headers)
        r.raise_for_status()
        # TODO -- check for HTML
        g = Graph().parse(data=r.text, format=self.__content_type_to_mime_type(
            r.headers['content-type']))

        for (subject, inbox) in g[:URIRef(LDP_INBOX)]:
            print("Inbox: " + str(inbox))
            return str(inbox)

    def __content_type_to_mime_type(self, content_type):
        return content_type.split(";")[0].strip()

    def __accept_post_options(self, inbox, **kwargs):
        r = requests.options(inbox, auth=kwargs.get('auth'))
        if r.status_code == requests.codes.ok and 'accept-post' in r.headers:
            if JSON_LD in r.headers['accept-post']:
                return JSON_LD

            for content_type in r.headers['accept-post'].split(','):
                return self.__content_type_to_mime_type(content_type)

    def __is_localhost(self, inbox):
        return ipaddress.ip_address(socket.gethostbyname(
            urlparse(inbox).hostname)).is_loopback

    def __post_message(self, inbox, data, content_type, **kwargs):
        if self.allow_localhost or not self.__is_localhost(inbox):
            headers = {"content-type": content_type}
            r = requests.post(inbox, data=data, headers=headers,
                              auth=kwargs.get('auth'))
            r.raise_for_status()
        else:
            raise ValueError("Invalid local inbox.")

    def discover(self, target, **kwargs):
        """Discover the inbox for a resource."""
        return self.__discover_head(target, **kwargs) or self.__discover_get(
                target, **kwargs)

    def send(self, inbox, data, **kwargs):
        """Send the provided data to an inbox."""
        if isinstance(data, dict) or isinstance(data, list):
            self.__post_message(inbox, json.dumps(data), JSON_LD, **kwargs)
        elif isinstance(data, str):
            self.__post_message(inbox, data, JSON_LD, **kwargs)
        elif isinstance(data, Graph):
            ct = self.__accept_post_options(inbox, **kwargs) or JSON_LD
            self.__post_message(inbox, data.serialize(format=ct),
                                ct, **kwargs)
        else:
            raise TypeError(
                    "You cannot send data of type {}.".format(type(data)))
