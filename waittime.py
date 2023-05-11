import time

from locust import User, task, constant, between, constant_pacing


class MyUser(User):
    wait_time = constant_pacing(5)

    @task
    def launch(self):
        start_time = time.time()
        time.sleep(2)
        print("Pacing ")
        end_time = time.time()
        execution_time = end_time - start_time
        print("Время выполнения: ", execution_time, "секунд")



