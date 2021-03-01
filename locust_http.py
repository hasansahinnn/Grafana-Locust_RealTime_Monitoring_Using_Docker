from locust import HttpUser,task,between

class JsonAPI(HttpUser):
  wait_time = between(1, 2.5)
  
  @task
  def get_posts(self):
    self.client.get("/api/Data")
















