from locust import SequentialTaskSet, TaskSet, task, constant, HttpUser

class MySeqTaskSet(SequentialTaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("get status of 200")
    @task
    def get_status(self):
        self.client.get("/500")
        print("get status of 500")

class MyLoadTest(HttpUser):
    host= "https://http.cat"
    tasks = [MySeqTaskSet]
    wait_time = constant(1)