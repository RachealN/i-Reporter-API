import unittest
from flask import Flask,json
from  app.views import redflag_view
from app import app


class TestRedFlag(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    
    def test_index(self):
        result = self.client.get('/', content_type='application/json')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {"message": "Welcome to i-Reporter"})


    def test_created_redflag(self):
        pass
    
        

    def test_get_redflags(self):
        pass

    def test_get_single_redflag_by_id(self):
        pass

    def test_edit_redflag_location(self):
        pass

    def test_edit_redflag_comment(self):
        pass

    def test_delete_redflag(self):
        pass
        

