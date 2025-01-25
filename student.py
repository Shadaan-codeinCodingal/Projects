class student:
    grade = 4
    name = 'Shadaan'
    def intro(self):
        print("Hi! i am a student.")
    def information(self):
        print("My name is", self.name)
        print("I am in class", self.grade)
objectstudent = student()
objectstudent.intro()
objectstudent.information()