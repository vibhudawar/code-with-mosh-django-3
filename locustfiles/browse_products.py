from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    # under this we are doing performance testing for the following:
    # Viewing Products
    @task(2)
    def view_products(self):
        print('View all products')
        collection_id = randint(2, 6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name='/store/products')

    # Viewing Product details
    @task(4)
    def view_product_details(self):
        print('View products details')
        product_id = randint(1, 1000)
        self.client.get(f'/store/products/{product_id}', name='/store/products/:id')

    # Add product to the cart
    @task(1)
    def add_to_cart(self):
        print('Add product to cart')
        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/', name='/store/carts/items', json={'product_id': product_id, 'quantity': 1})

    # inbuilt method to generate the unique cart_id whenever the user first browse the website
    def on_start(self):
        response = self.client.post('/store/carts')
        result = response.json()
        self.cart_id = result['id']