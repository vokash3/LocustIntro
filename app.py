from locust import User, task, constant


class FirstTest(User):
    weight = 2
    wait_time = constant(5)

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching...")


class SecondTest(User):
    weight = 2
    wait_time = constant(5)

    @task
    def launch(self):
        print("Second test")

    @task
    def search(self):
        print("Second Search task...")
