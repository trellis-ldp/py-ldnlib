from rdflib import Graph, URIRef
import requests


class BaseLDN(object):

    ACCEPT_HEADERS = ("application/ld+json; q=1.0,"
                      "text/turtle; q=0.9,"
                      "application/xml+rdf; q=0.5")
    JSON_LD = "application/ld+json"
    LDP_INBOX = "http://www.w3.org/ns/ldp#inbox"

    def __init__(self, **kwargs):
        self.accept_headers = kwargs.get('accept_headers', self.ACCEPT_HEADERS)

    def __discover_head(self, target, **kwargs):
        r = requests.head(target, allow_redirects=True,
                          auth=kwargs.get('auth'))
        r.raise_for_status()
        if self.LDP_INBOX in r.links:
            return r.links[self.LDP_INBOX].get('url')

    def __discover_get(self, target, **kwargs):
        headers = {'accept': self.accept_headers}
        r = requests.get(target, auth=kwargs.get('auth'), headers=headers)
        r.raise_for_status()
        # TODO -- check for HTML
        g = Graph().parse(data=r.text, format=self.content_type_to_mime_type(
            r.headers['content-type']))

        for (subject, inbox) in g[:URIRef(self.LDP_INBOX)]:
            return str(inbox)

    def content_type_to_mime_type(self, content_type):
        """
        A utility method to convert a content-type header into a
        mime-type string.
        """
        return content_type.split(";")[0].strip()

    def discover(self, target, **kwargs):
        """Discover the inbox for a resource."""
        return self.__discover_head(target, **kwargs) or self.__discover_get(
                target, **kwargs)
