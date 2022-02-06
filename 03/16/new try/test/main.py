import random
from locust import HttpUser, task, between


# class SampleMobileUser(HttpUser):
    # weight = 5


class SampleWebUser(HttpUser):
    wait_time = between(.3, .6)
    # wait_time = constant(.3)
    # wait_time = constant_pacing(1)
    weight = 1
    

    # def on_start(self):
        # pass


    @task(10)
    def get_stats(self):
        self.client.get('/api/stats/')


    @task
    def get_delay(self):
        self.client.get('/api/delay/')


    @tag('order')
    @task(2)
    def create_order(self):
        data = {
            "order_id": random.randint(1, 100),
            "user_id": random.randint(1, 100),
            "product_id": random.randint(1, 100),
            "discount": random.randint(1, 100),
        }
        self.client.post('api/order/create/' , json=data)


    @tag('get_detail')
    @task(2)
    def orders_list(self):
        self.client.get('api/order/list/')


    @tag('test_network')
    @task()
    def test_html(self):
        self.client.get('/')

        
    # def on_stop(self):
        # pass


