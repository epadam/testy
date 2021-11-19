from locust import TaskSet, task, Locust


class WebsiteTasks(TaskSet):
    @task(1)
    def index(self):
        self.client.get('/')


class WebsiteUser(Locust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
