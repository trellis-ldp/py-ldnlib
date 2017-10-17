import unittest
from unittest.mock import patch
from rdflib import Graph
import json

from ldnlib import Sender


class TestSender(unittest.TestCase):

    INBOX = "http://example.org/inbox"
    HEADERS = {"content-type": "application/ld+json"}

    @patch('requests.post')
    def test_send_string(self, mock_post):
        data = None
        with open("tests/notification.json", "r") as f:
            data = f.read()

        Sender().send(self.INBOX, data)
        self.assertEquals(str, type(data))
        mock_post.assert_called_once_with(self.INBOX, data=data,
                                          headers=self.HEADERS)

    @patch('requests.post')
    def test_send_dict(self, mock_post):
        data = None
        with open("tests/notification.json", "r") as f:
            data = json.loads(f.read())

        Sender().send(self.INBOX, data)
        self.assertEquals(dict, type(data))
        mock_post.assert_called_once_with(self.INBOX, data=json.dumps(data),
                                          headers=self.HEADERS)

    @patch('requests.post')
    def test_send_list(self, mock_post):
        data = None
        with open("tests/notification.json", "r") as f:
            data = json.loads("[" + f.read() + "]")

        Sender().send(self.INBOX, data)
        self.assertEquals(list, type(data))
        mock_post.assert_called_once_with(self.INBOX, data=json.dumps(data),
                                          headers=self.HEADERS)

    @patch('requests.post')
    def test_send_graph(self, mock_post):
        data = Graph().parse("tests/notification.nt", format="ntriples")

        Sender().send(self.INBOX, data)
        self.assertEquals(Graph, type(data))
        mock_post.assert_called_once_with(self.INBOX, data=data.serialize(
            format="application/ld+json"), headers=self.HEADERS)
