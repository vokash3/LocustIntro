from locust import HttpUser, constant, task


class ReqResIn(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    percentiles_to_report = [0.5, 0.75, 0.99]

    @task
    def get_users(self):
        res = self.client.get("/api/users", params={"page": 2})
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_users(self):
        res = self.client.post("/api/users", data='''
                         {"name":"wain","job":"leader"}
                         ''')
        print(res.text)
        print(res.status_code)
        print(res.headers)
