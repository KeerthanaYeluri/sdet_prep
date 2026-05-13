from locust import HttpUser, task, between

class My_test(HttpUser):
    wait_time = between(1, 2)
    @task
    def hello(self):
        print("Hello World")
    @task
    def hii(self):
        print("hii")
