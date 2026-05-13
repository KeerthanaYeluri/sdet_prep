from locust import HttpUser, task, between,SequentialTaskSet

class My_test(SequentialTaskSet):
    @task
    def get_users(self):
        res=self.client.get("/users")
        print("Get Method  status is ",res.status_code) 

    @task
    def post_status(self):
        res=self.client.post("/status")
        print("Post Method  status is ",res.status_code)

class MySeqTest(HttpUser):
    wait_time = between(1, 2)
    host="http://operator-qa.qmaastech.com/login"
    tasks=[My_test]
