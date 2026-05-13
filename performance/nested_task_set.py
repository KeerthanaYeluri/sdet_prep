from random import random

from locust import constant,HttpUser, TaskSet, task


class MyHttpCat(TaskSet):
    @task
    def get_users(self):
        self.client.get("/200")
        print("get status of 200")
    @task
    class MyAnotherHttpCat(TaskSet):
        @task
        def get_500_status(self):
            self.client.get("/500")
            print("get status of 500")
            self.interrupt(reschedule=True)


class MyLoadTest(HttpUser):
    host= "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)