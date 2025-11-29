# Basic Operation Functions
def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


# Input Validation
def read_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid numeric value.")


# Menu Printing
def display_menu():
    print("\n----------- Calculator Menu -----------")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit")
    print("---------------------------------------")


# Object-Oriented Calculator Class

class Calculator:

    def add(self, x, y):
        return add_numbers(x, y)

    def subtract(self, x, y):
        return subtract_numbers(x, y)

    def multiply(self, x, y):
        return multiply_numbers(x, y)

    def divide(self, x, y):
        return divide_numbers(x, y)

    def run(self):
        print("Welcome! This is an interactive calculator.\n")

        while True:
            display_menu()
            option = input("Choose an option (1-5): ")

            if option == "5":
                print("Thank you. Have a great day!")
                break

            if option not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please pick a number between 1 and 5.")
                continue

            # Get numbers
            n1 = read_number("Enter the first value: ")
            n2 = read_number("Enter the second value: ")

            print("\nResult:")
            print("---------------------------------------")

            if option == "1":
                print(f"{n1} + {n2} = {self.add(n1, n2)}")

            elif option == "2":
                print(f"{n1} - {n2} = {self.subtract(n1, n2)}")

            elif option == "3":
                print(f"{n1} × {n2} = {self.multiply(n1, n2)}")

            elif option == "4":
                print(f"{n1} ÷ {n2} = {self.divide(n1, n2)}")


# Run the Program

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
