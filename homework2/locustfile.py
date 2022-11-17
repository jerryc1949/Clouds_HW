import time
from locust import HttpUser, task, between

class QiuckstarUser(HttpUser):
    @task
    def hello_world(self):
        # self.client.get('/0/3.14159')
        self.client.get('/jerryc2049?name=0_3.14159')

