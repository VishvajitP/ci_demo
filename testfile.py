''' 
Module to test upload functionality
'''

import unittest
from app import app
from cStringIO import StringIO


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_upload(self):
        filename = 'test.txt'
        filetext = StringIO('test me')
        res = self.client.post('/', data=dict(file=(filetext, filename)))

        assert res.status_code == 200
        assert filename in res.data

if __name__ == '__main__':
    unittest.main()