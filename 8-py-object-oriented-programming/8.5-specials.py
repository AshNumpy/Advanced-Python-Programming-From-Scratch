# myList = [1,2,3]
# myString = 'My String'

# print(len(myList))
# print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie object have been created!")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("movie object have been deleted")

m = Movie('Interstellar', 'Cristopher Nolan', 2*60+49)

print(str(m)) # there is string method in Movie class anymore
print(len(m)) # there is len meth too

del m
