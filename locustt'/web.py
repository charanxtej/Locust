from locust import HttpUser, task, constant

class MyUser(HttpUser):
    host = "https://cdn.segment.com/"
    wait_time = constant(3)

    @task
    def browse_home(self):
        self.client.get("v1/projects/TNQ3krVkHTWg6Gx2PEkaCYEXaNrwbGXG/settings")
        print("Reached home")

    @task
    def Abtext(self):
        self.client.get("v1/projects/TNQ3krVkHTWg6Gx2PEkaCYEXaNrwbGXG/settings")
        print("Reached home")

    @task(1)
    def CheckBoxes(self):
            self.client.get("checkboxes")
            print("Reached checkboxes")


    @task(2)
    def HomePage(self):
            self.client.get("")
            print("Reached Home")

    @task(3)
    def Dropdown(self):
            self.client.get("dropdown")
            print("Dropdown")

    @task
    def Login(self):
            self.client.post("login", data ={"username": "user1231", "password": "pass123"})
            print("login")

    @task
    def upload_file(self):
        file_data = open("/home/qb_user/Documents/aravindtodo/todo21.css", "r")
        response = self.client.post("upload", files={"todo21.css": file_data})
        if response.status_code == 200:
            print("File uploaded successfully")