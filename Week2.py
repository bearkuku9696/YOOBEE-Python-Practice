

class student:
    def __init__(self, age, name, subject):
        self.age = age
        self.name = name
        self.subject = subject


    def print(self):
        print("age:" + self.age + ", name:" + self.name + " ,subject:" + self.subject)




student = student("18", "Lee", "software engineer" )
student.print()

