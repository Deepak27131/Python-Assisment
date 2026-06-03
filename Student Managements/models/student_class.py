
class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Course: {self.course}"