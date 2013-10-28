#!/usr/bin/env python2.7

"""Unittests for Configuration service webapp"""

import unittest
import json
from flaskgevent import webapp

class ConfigWebappTestCase(unittest.TestCase):
    """unittest.TestCase subclass for webapp"""

    def setUp(self):
        self.app = webapp.app.test_client()

    def test_static_json(self):
        """Test getting index which is static json"""
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200,
                         msg = "Should have got 200, got %s instead - %s" % (resp.status_code,
                                                                             resp.data,))
        expected = { "somekey": "somedata" }
        self.assertEqual(resp.data, json.dumps(expected),
                         msg = "Static data not what it should be - got %s - should be %s" % (resp.data,
                                                                                              json.dumps(expected),
                                                                                              ))

