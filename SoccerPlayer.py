class Player:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city


    def get_status(self):
        print(self.name + self.age + self.city)