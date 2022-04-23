from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/winequality?free_sulfur_dioxide=3.3&fixed_acidity=3.3&alcohol=3.3&density=3.3&sulphates=3.3&residual_sugar=3.3&citric_acid=3.3&total_sulfur_dioxide=3.3&pH=3.3&chlorides=3.3&volatile_acidity=3.3")