class Studaint:
    def __init__(self, name, last_name, age, height):
        self.name = name,
        self.last_name = last_name,
        self.age = age,
        self.height = height

    def print_info(self):
        print(self.name + self.last_name + self.age)


class Techer(Studaint):
    def __init__(self,name,last_name,age,height):
        self.name = name,
        self.last_name = last_name,
        self.age = age,
        self.height = height
    def print_info(self):
        print( self.name )
