from django.test import TestCase

import requests

# Create your tests here.

"""
class TestProducts:
    url_products = ''

    def test_get_products(self):
        response = requests.get(url=self.url_categories)
        assert response.status_code == 200

    def test_get_product(self):
        response = requests.get(url=f'{self.url_categories}1')
        assert response.status_code == 200

    def test_post_product(self):
        novo = {
            "title" : "Test Book",
            "description" : "The book is about children.",
            "price" : "100",
            "active" : True,
            "category" : ""   
        }

        response = requests.post(url=self.url_categories, headers=self.headers, data=novo)
        assert response.status_code == 201
        assert response.json()['title'] == novo['title']

    def test_put_product(self):
        atualizado = {
            "title" : "Test Book Update",
            "description" : "The book is about children.",
            "price" : "10",
            "active" : True,
            "category" : ""   
        }

        response = requests.put(url=f'{self.url_categories}2', headers=self.headers, data=atualizado)
        assert response.status_code == 200
        assert response.json()['title'] == atualizado['title']

    def test_delete_product(self):
        response = requests.delete(url=f'{self.url_categories}2', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0
"""

"""
class TestCategories:
    url_categories = ''

    def test_get_categories(self):
        response = requests.get(url=self.url_categories)
        assert response.status_code == 200

    def test_get_categoy(self):
        response = requests.get(url=f'{self.url_categories}1')
        assert response.status_code == 200

    def test_post_category(self):
        novo = {
            "title" : "Romance",
            "slug" : "",
            "description" : "Love between people",
            "active" : True 
        }

        response = requests.post(url=self.url_categories, headers=self.headers, data=novo)
        assert response.status_code == 201
        assert response.json()['title'] == novo['title']

    def test_put_category(self):
        atualizado = {
            "title" : "Action",
            "slug" : "",
            "description" : "Action, adrenaline in the movie.",
            "active" : True 
        }

        response = requests.put(url=f'{self.url_categories}2', headers=self.headers, data=atualizado)
        assert response.status_code == 200
        assert response.json()['title'] == atualizado['title']

    def test_delete_category(self):
        response = requests.delete(url=f'{self.url_categories}2', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0
"""