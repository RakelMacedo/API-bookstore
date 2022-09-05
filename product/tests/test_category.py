import requests


class TestCategories:
    url_categories = "http://127.0.0.1:8000/bookstore/category/"

    def test_get_categories(self):
        response = requests.get(url=self.url_categories)
        assert response.status_code == 200

    def test_get_categoy(self):
        response = requests.get(url=f"{self.url_categories}1")
        assert response.status_code == 200

    def test_post_category(self):
        novo = {
            "title": "Comedia",
            "slug": "comedia",
            "description": "Engracado, divertido.",
            "active": True,
        }

        response = requests.post(url=self.url_categories, data=novo)
        assert response.status_code == 201
        assert response.json()["title"] == novo["title"]


"""
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
