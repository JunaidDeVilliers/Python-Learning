# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers):
  print(f"Maximum: {max(numbers)}")
  print(f"Average: {sum(numbers) / len(numbers)}")
  print(f"Minimum: {min(numbers)}")


# call the function below here
stats(example_list)