# Challenge 3 - Arithmetic Operators

#Read two integers from STDIN and print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

#The first line contains the first integer, a. The second line contains the second integer, b.

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print("\nAddition: " + str(a + b))
print("Subtraction: " + str(a - b))
print("Multiplication: " + str(a * b))