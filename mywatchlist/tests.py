from audioop import reverse
from urllib import response 
from django.test import TestCase, Client
from django.urls import resolve

class Test(TestCase):
    
    def test_xml(self):
        response = Client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    def test_json(self):
        response = Client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    def test_html(self):
        response = Client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
   