def cube():
    for i in range(5):
        yield i**3 # we can use yield to save memory
                   # thx to yield we dont take up space to memory

iterator = cube() # xyield return as a iterable obj.
for i in iterator:
    print(i)

# but list obj take up space to memory
list = [i**3 for i in range(5)]
print(list)