print(" iterative factorial")

n=int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is", factorial)   

print("recursive factorial")
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial of ", n, "is", recursive_factorial(n))