# locust
# -f httpcatseq.py
# -u 5 -r 1 -t 1m
# --headless --print-stats --csv httpcat.csv --csv-full-history
# --host=https://http.cat

from locust import SequentialTaskSet, task, HttpUser, constant


class HTTPCatSeq(SequentialTaskSet):

    @task
    def get_status_200(self):
        self.client.get("/200")
        print("Get status of 200")

    @task
    def get_status_500(self):
        self.client.get("/500")
        print("Get status of 500")


class CatUser(HttpUser):
    host = "https://http.cat"
    tasks = [HTTPCatSeq]
    wait_time = constant(1)
