from random import random

from locust import constant,HttpUser, TaskSet, task
import random

class MyHttpCat(TaskSet):
    @task
    def get_users(self):
        self.client.get("/200")
        print("get status of 200")

    @task
    def get_random_status(self):
        status_codes=[100,101,102,200,201,202,203,3011,301,302,400,401,402,500]
        random.url="/"+str(random.choice(status_codes))
        print("random http status")

class MyLoadTest(HttpUser):
    host= "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)