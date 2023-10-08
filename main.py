# Import all necessary packages
import os
import platform
import pyfiglet

# Define the folder containing the challenge files
folder = 'challenges_folder'

# Create a dictionary to store functions
functions = {}

# Create a dictionary to store subfolders and their functions
subfolder_functions = {}

# Function to load challenge functions from Python files
def load_functions(subfolder):
    # Create the full path to the subfolder
    subfolder_path = os.path.join(folder, subfolder)
    
    # Walk through all files and subdirectories in the subfolder
    for root, _, files in os.walk(subfolder_path):
        for filename in files:
            if filename.endswith('.py'):
                # Get the module name from the filename (excluding the '.py' extension)
                module_name = os.path.splitext(filename)[0]
                
                # Open and compile the Python file
                with open(os.path.join(root, filename), 'r') as file:
                    code = compile(file.read(), filename, 'exec')
                    
                    # Create a namespace to execute the code
                    namespace = {}
                    exec(code, namespace)
                    
                    # Iterate through the items in the namespace and store callable functions
                    for name, value in namespace.items():
                        if callable(value) and not name.startswith("__"):
                            subfolder_functions[subfolder][name] = value

# Function to list available functions in a subfolder
def list_functions(subfolder_name):
    if subfolder_name not in subfolder_functions:
        subfolder_functions[subfolder_name] = {}
        load_functions(subfolder_name)
    
    # Print a list of available challenges in the subfolder
    print(f"\nHere is a list of available challenges in '{subfolder_name}' (in alphabetical order):")
    function_names = sorted(subfolder_functions[subfolder_name].keys())
    for i, function_name in enumerate(function_names, start=1):
        print(f"{i}. {function_name}")
    return function_names  # Return the list of function names

# Function to clear the terminal screen based on the OS
def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')  # Clear terminal on Windows
    else:
        os.system('clear')  # Clear terminal on Unix-like systems

# List subfolders in the main folder
subfolders = next(os.walk(folder))[1]

# Exclude '__pycache__' from the list of subfolders (Python cache folder)
subfolders = [subfolder for subfolder in subfolders if subfolder != '__pycache__']

# Main menu loop
while True:
    # Clear the terminal screen
    clear_terminal()
    
    # Print a stylized "Hello World" message using pyfiglet
    print(pyfiglet.figlet_format("Hello World"))

    print("Thank you for using Andrew and Fin's Python Challenge Launcher!")
    
    # Print a list of available subfolders
    print("\nHere is a list of challenges, ordered in difficulty groups: ")
    for i, subfolder in enumerate(subfolders, start=1):
        print(f"{i}. {subfolder}")
    print("0. ⏴ Quit")
    
    try:
        # Prompt the user to choose a subfolder
        choice = int(input("\n▶ Enter the number of the challenge's difficulty (0 to quit): "))
        
        if choice == 0:
            break  # Quit the program
        
        if choice > 0 and choice <= len(subfolders):
            subfolder_name = subfolders[choice - 1]
            function_names = list_functions(subfolder_name)  # List available functions in the selected subfolder
            print("0. ↪ Return to Main Menu")
            
            # Subfolder menu loop
            while True:
                try:
                    # Prompt the user to choose a challenge within the subfolder
                    challenge_choice = int(input(f"\n▶ Enter the number of the challenge you want to run in '{subfolder_name}' (0 to go back to Main Menu, -1 to quit): "))
                    
                    if challenge_choice == 0:
                        break  # Go back to the main menu
                    
                    if challenge_choice == -1:
                        exit()  # Quit the program
                    
                    # Check if the user entered a valid challenge number
                    elif challenge_choice > 0 and challenge_choice <= len(function_names):
                        function_name = function_names[challenge_choice - 1]
                        
                        # Execute the selected challenge function
                        print(f"\n▷ Running challenge: {function_name}\n")
                        subfolder_functions[subfolder_name][function_name]()  # Call the chosen function
                        print(f"\n▷ Challenge {function_name} has been executed")
                        
                        # Show the options again after executing a challenge
                        input("\nPress Enter to continue...")
                    
                    else:
                        print("▷ Invalid choice. Please enter a valid number.")
                    
                except ValueError:
                    print("▷ Invalid input. Please enter a valid number.")
        else:
            print("▷ Invalid choice. Please enter a valid number.")
    except ValueError:
        print("▷ Invalid input. Please enter a valid number.")


