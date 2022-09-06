import requests


class TestProducts:
    url_products = "http://127.0.0.1:8000/bookstore/product/"

    def test_get_products(self):
        response = requests.get(url=self.url_products)
        assert response.status_code == 200

    def test_get_product(self):
        response = requests.get(url=f"{self.url_products}2")
        assert response.status_code == 200

    def test_post_product(self):
        novo = {
            "title": "O Senhor dos Aneis",
            "description": "Um hobbit que tem a missao de destruir o Anel do Poder, para salvar seu mundo da destruicao",
            "price": 45,
            "active": True,
            "categories_id": [4, 2],
        }

        response = requests.post(url=self.url_products, data=novo)
        assert response.status_code == 201
        assert response.json()["title"] == novo["title"]


"""
    def test_put_product(self):
        atualizado = {
            "title" : "Test Book Update",
            "description" : "The book is about children.",
            "price" : "10",
            "active" : True,
            "category" : ""   
        }

        response = requests.put(url=f'{self.url_products}2', headers=self.headers, data=atualizado)
        assert response.status_code == 200
        assert response.json()['title'] == atualizado['title']

    def test_delete_product(self):
        response = requests.delete(url=f'{self.url_products}2', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0
"""
