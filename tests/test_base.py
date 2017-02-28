import unittest
from unittest.mock import Mock, patch

from ldnlib.base import BaseLDN


class TestBase(unittest.TestCase):

    @patch('requests.head')
    def test_discover_head(self, mock_head):
        inbox = "http://example.org/inbox"
        mock_res = Mock()
        mock_res.links = {"http://www.w3.org/ns/ldp#inbox": {"url": inbox}}

        mock_head.return_value = mock_res

        ldn = BaseLDN()
        self.assertEqual(ldn.discover("http://example.org/resource"), inbox)

    @patch('requests.get')
    @patch('requests.head')
    def test_discover_get(self, mock_head, mock_get):
        inbox = "http://example.org/inbox"
        links = {"type": {"url": "http://www.w3.org/ns/ldp#Container"}}
        headers = {"content-type": "application/n-triples"}

        mock_res1 = Mock()
        mock_res1.links = links
        mock_res1.headers = headers
        mock_head.return_value = mock_res1

        mock_res2 = Mock()
        mock_res2.links = links
        mock_res2.headers = headers
        mock_res2.text = "<http://example.org/resource> " + \
                         "<http://www.w3.org/ns/ldp#inbox> " + \
                         "<http://example.org/inbox> .\n"
        mock_get.return_value = mock_res2

        ldn = BaseLDN()
        self.assertEqual(ldn.discover("http://example.org/resource"), inbox)

    def test_content_type(self):
        ldn = BaseLDN()
        self.assertEqual("application/ld+json",
                         ldn.content_type_to_mime_type(
                             "application/ld+json ; " +
                             "profile=\"http://example.org/profile.json\""))
        self.assertEqual("text/turtle",
                         ldn.content_type_to_mime_type(
                             "text/turtle;charset=utf-8"))
