

class student:
    def __init__(self, age, name, subject):
        self.age = age
        self.name = name
        self.subject = subject


    def print(self):
        print(f"age: {self.age},  name: {self.name},   subject: {self.subject}")




student = student(18, "Lee", "software engineer" )
student.print()




number = 123.456
template = "{0:10.2f}"
template_format = template.format(number)
print(float(template_format))
