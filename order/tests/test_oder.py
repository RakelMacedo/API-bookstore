import requests


class TestOrders:
    url_orders = "http://127.0.0.1:8000/bookstore/order/"

    def test_get_orders(self):
        response = requests.get(url=self.url_orders)
        assert response.status_code == 200

    def test_post_order(self):
        novo = {"user": 1, "products_id": [1]}

        response = requests.post(url=self.url_orders, data=novo)
        assert response.status_code == 201    

    def test_get_order(self):
        response = requests.get(url=f"{self.url_orders}1")
        assert response.status_code == 200

