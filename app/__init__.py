from calculator.operations import add, subtract, multiply, divide

class App:
    commands = {
        "add": "Add two numbers",
        "subtract": "Subtract two numbers",
        "multiply": "Multiply two numbers",
        "divide": "Divide two numbers",
        "exit": "Exit the application",
        "menu": "Display available commands"
    }

    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        App.display_menu()

        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            elif user_input.lower() == "menu":
                App.display_menu()
            elif user_input.startswith("add"):
                _, num1, num2 = user_input.split()
                try:
                    result = add(float(num1),float(num2)) 
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
            elif user_input.startswith("subtract"):
                _, num1, num2 = user_input.split()
                try:
                    result = subtract(float(num1),float(num2)) 
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
            elif user_input.startswith("multiply"):
                _, num1, num2 = user_input.split()
                try:
                    result = multiply(float(num1),float(num2)) 
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
            elif user_input.startswith("divide"):
                _, num1, num2 = user_input.split()
                try:
                    if float(num2) != 0:
                        result = divide(float(num1),float(num2)) 
                        print(f"Result: {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
            else:
                print("Unknown command. Type 'menu' to see available commands.")

    @staticmethod
    def display_menu() -> None:
        print("Available commands:")
        for command, description in App.commands.items():
            print(f"{command}: {description}")