from locust import HttpUser, task, between,constant

class User(HttpUser):
    host = "https://serving.stat-rock.com/"
    response_time=constant(1)

    #Visiting the Home page
    @task
    def BrowseHome(self):
        self.client.get("")
        print("Main")

    #Visiting the Page "Bookstore"
    @task
    def BookStore(self):
        self.client.get("BookStore/v1/Books")
        print("Bookstore")

    #Logging in using a payload of Username and password
    @task
    def Login(self):
        self.client.post("Account/v1/Login", data ={"UserName": "CJ12345", "Password": "8712177121@Qa"})
        print("Login Completed")

    #Going to page "Bookstore"
    @task
    def BackBookStore(self):
        self.client.get("BookStore/")
        print("On Store")

    #Selecting a book with Certain book ID
    @task
    def SelectBook(self):
        self.client.get("BookStore/v1/Book?ISBN=9781449325862")
        print("Selected Book")

    # Perform the action to add a book to favorites
    @task
    def AddToFav(self):
        payload = {
            "userId": "5349b754-7687-4660-878c-569a1a03baa9",
            "collectionOfIsbns": [
                {"isbn": "9781449337711"}
            ]
        }

        response = self.client.post("BookStore/v1/Book?ISBN=9781449325862", json=payload)
        if response.status_code == 201:
            print("Book added to favorites successfully")
        else:
            print("Book Already added")

    @task
    def VisitProfile(self):
        self.client.get("Account/v1/User/5349b754-7687-4660-878c-569a1a03baa9")
        print("On Profile")

    @task
    def DeleteFav(self):
        payload = {
            "userId": "5349b754-7687-4660-878c-569a1a03baa9",
            "collectionOfIsbns": [
                {"isbn": "9781449337711"}
            ]
        }

        response = self.client.post("BookStore/v1/Book", json=payload)
        if response.status_code == 204:
            print("Book Removed")
        else:
            print("Book Not found")