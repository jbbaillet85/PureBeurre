from locust import HttpUser, task


class HomepagePerformanceTest(HttpUser):
    @task(6)
    def test_homepage(self):
        self.client.get("/homepage")

    @task(6)
    def test_identification(self):
        self.client.get("/spaceUser/login")
