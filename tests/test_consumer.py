import unittest
from unittest.mock import Mock, patch

from ldnlib import Consumer


class TestConsumer(unittest.TestCase):

    @patch('requests.get')
    def test_notifications_ntriples(self, mock_get):
        mock_res = Mock()
        mock_res.headers = {"content-type": "application/n-triples"}
        with open("tests/inbox.nt", "r") as f:
            mock_res.text = f.read()

        mock_get.return_value = mock_res

        notifications = Consumer().notifications("http://example.org/inbox")

        self.assertEqual(5, len(notifications))
        self.assertTrue("http://example.org/inbox/1" in notifications)
        self.assertTrue("http://example.org/inbox/2" in notifications)
        self.assertTrue("http://example.org/inbox/3" in notifications)
        self.assertTrue("http://example.org/inbox/4" in notifications)
        self.assertTrue("http://example.org/inbox/5" in notifications)

    @patch('requests.get')
    def test_notifications_jsonld_compacted(self, mock_get):
        mock_res = Mock()
        mock_res.headers = {"content-type": "application/ld+json"}
        with open("tests/inbox.jsonld", "r") as f:
            mock_res.text = f.read()

        mock_get.return_value = mock_res

        notifications = Consumer().notifications("http://example.org/inbox")

        self.assertEqual(5, len(notifications))
        self.assertTrue("http://example.org/inbox/1" in notifications)
        self.assertTrue("http://example.org/inbox/2" in notifications)
        self.assertTrue("http://example.org/inbox/3" in notifications)
        self.assertTrue("http://example.org/inbox/4" in notifications)
        self.assertTrue("http://example.org/inbox/5" in notifications)

    @patch('requests.get')
    def test_notifications_jsonld_expanded(self, mock_get):
        mock_res = Mock()
        mock_res.headers = {"content-type": "application/ld+json"}
        with open("tests/inbox_expanded.jsonld", "r") as f:
            mock_res.text = f.read()

        mock_get.return_value = mock_res

        notifications = Consumer().notifications("http://example.org/inbox")

        self.assertEqual(5, len(notifications))
        self.assertTrue("http://example.org/inbox/1" in notifications)
        self.assertTrue("http://example.org/inbox/2" in notifications)
        self.assertTrue("http://example.org/inbox/3" in notifications)
        self.assertTrue("http://example.org/inbox/4" in notifications)
        self.assertTrue("http://example.org/inbox/5" in notifications)

    @patch('requests.get')
    def test_notifications_turtle(self, mock_get):
        mock_res = Mock()
        mock_res.headers = {"content-type": "text/turtle; charset=utf-8"}
        with open("tests/inbox.ttl", "r") as f:
            mock_res.text = f.read()

        mock_get.return_value = mock_res

        notifications = Consumer().notifications("http://example.org/inbox")

        self.assertEqual(5, len(notifications))
        self.assertTrue("http://example.org/inbox/1" in notifications)
        self.assertTrue("http://example.org/inbox/2" in notifications)
        self.assertTrue("http://example.org/inbox/3" in notifications)
        self.assertTrue("http://example.org/inbox/4" in notifications)
        self.assertTrue("http://example.org/inbox/5" in notifications)
