import random

from locust import TaskSet, HttpUser, constant
from locust.user import task


class HTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")

    @task
    def get_random_status(self):
        status_codes = [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305,
                        307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416,
                        417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 444, 451, 499, 500, 501, 502, 503, 504, 505,
                        506, 507, 508, 510, 511, 599]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)
        print(f"Random http status: {res}")


class HTTPCatLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [HTTPCat]
    wait_time = constant(1)
