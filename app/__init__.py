# app.py
from app.plugin_loader import load_plugins
import multiprocessing

class App:
    def __init__(self, plugin_folder):
        self.plugins = load_plugins(plugin_folder)
        self.commands = {plugin.name: plugin.description for plugin in self.plugins}

    def start(self):
        print("Hello World. Type 'exit' to exit.")
        self.display_menu()

        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            elif user_input.lower() == "menu":
                self.display_menu()
            else:
                for plugin in self.plugins:
                    if user_input.startswith(plugin.name):
                        _, num1, num2 = user_input.split()
                        p = multiprocessing.Process(target=self.execute_plugin, args=(plugin, float(num1), float(num2)))
                        p.start()
                        break
                else:
                    print("Unknown command. Type 'menu' to see available commands.")

    def execute_plugin(self, plugin, num1, num2):
        try:
            result = plugin.execute(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def display_menu(self):
        print("Available commands:")
        for command, description in self.commands.items():
            print(f"{command}: {description}")