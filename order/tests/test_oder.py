import requests


class TestOrders:
    headers = {"Authorization": "Token dfabda91c99d7dbd3b1d185834b72627859f748d"}
    url_orders = "http://127.0.0.1:8000/bookstore/order/"

    def test_get_orders(self):
        response = requests.get(url=self.url_orders, headers=self.headers)
        assert response.status_code == 200

    def test_get_order(self):
        response = requests.get(url=f"{self.url_orders}1", headers=self.headers)
        assert response.status_code == 200

    def test_post_order(self):
        novo = {"user": 1, "products_id": [9]}

        response = requests.post(url=self.url_orders, headers=self.headers, data=novo)
        assert response.status_code == 201
