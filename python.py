class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            print('Error: division by 0 is not possible.')

    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b


try:
    num1 = float(input("Enter first num : "))
    num2 = float(input("Enter second num : "))

    print(f"{num1} * {num2} = {Math.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {Math.divide(num1, num2)}")
    print(f"{num1} + {num2} = {Math.plus(num1, num2)}")
    print(f"{num1} - {num2} = {Math.minus(num1, num2)}")

except ValueError:
    print("Error: Please enter valid numbers.")
