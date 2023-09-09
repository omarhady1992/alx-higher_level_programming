#!/usr/bin/python3

"""Print the numbers from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            print("Fizz ", end="")
        elif n % 5 == 0:
            print("Buzz ", end="")
        elif n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz ", end="")
        elif n == 100:
            print("{}".format(number), end="")
        else:
            print("{} ".format(number), end="")
