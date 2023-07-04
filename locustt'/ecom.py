from locust import HttpUser, task, constant, between

class MyUser(HttpUser):
    host = "https://www.saucedemo.com/"
    wait_time = constant(1)

    @task
    def swaglab(self):
        self.client.get("")
        print("Reached home")

    @task
    def login(self):
        response = self.client.get('')

        username = 'standard_user'
        password = 'secret_sauce'

        login_data = {
            'username': username,
            'password': password,
        }

        self.client.post('', data=login_data)

        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed!")
