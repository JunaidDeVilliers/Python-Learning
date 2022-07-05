# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

# Personally added the start parameter so that the user can choose where they want to start
def my_enumerate(iterable, start):  # add your arguments
      # add your code implementation
      new_iterable = []
      num = 0
      num += start
      for element in iterable:
            new_iterable.append((num, element))
            num += 1
      return new_iterable

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

for index, course in my_enumerate(courses, 1):
    print(f"{index}: {course} Python")
