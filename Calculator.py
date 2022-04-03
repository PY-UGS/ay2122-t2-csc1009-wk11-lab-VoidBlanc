class Calculator:
    # Constructor to take in first input and second input number
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Sum function
    def adder(self):
        return self.num1 + self.num2

    # Subtract function
    def subtractor(self):
        return self.num1 - self.num2

    # Multiply function
    def multiplier(self):
        return self.num1 * self.num2

    # Division function
    def divider(self):
        return self.num1 / self.num2

    # Reset function
    def clear(self):
        self.num1 = 0
        self.num2 = 0
        if self.num1 == 0 and self.num2 == 0:
            return 0
        else:
            return -1


if __name__ == '__main__':

    # Input for first and second numbers
    input1 = float(input("Enter 1st number: "))
    input2 = float(input("Enter 2nd number: "))

    # To create calculator object with the input values
    c = Calculator(input1, input2)

    print("Addition: ", c.adder())
    print("Subtraction: ", c.subtractor())
    print("Multiplication: ", c.multiplier())
    print("Division: ", c.divider())
    print("Clearing.")
    if c.clear() == 0:
        print("Value of number have been reset to zero.")
    else:
        print("Clearing of number has failed")
