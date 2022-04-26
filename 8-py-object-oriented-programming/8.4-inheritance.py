# Inheritance (Kalıtım): Miras Alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created.")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created.')

    # override
    def who_am_i(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person('ramazan','erduran')
s1 = Student('erduran','ramazan',21821809)
t1 = Teacher('İbarhim', 'Zor', 'Bilg. Progr.')

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))
print(t1.firstName + " " + t1.lastName + " " + t1.branch)

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()