import os
import sys

def main():
    # Printing Header
    print("=" * 60)
    print("The Ultimate CSV/Text File Manipulation Script")
    print("Developed by Sebastian Caballero")
    print("=" * 60)
    
    # Initiating Path Tracker; Action Selection
    source_path = []
    action_choice = ["Keyword Search"]
    print("\nEnter the name of the file you'd like to work on.")
    print("Please include the file path as well. Type 'done' once you've processed all desired files.\n")
    
    # Prompting User to select filepath
    while True:
        filepath = input("Please locate the file(s) you'd like to work on (Type 'done' if there are no more files to manipulate): ").strip()
        
        # Checks if user is done
        if filepath.lower() == 'done':
            break
        
        # Removes leading/trailing double-quotes if detected
        if '\"' in filepath:
            filepath = filepath.strip('\"')
        
        # Validate path
        if not os.path.exists(filepath):
            print(f"Error: Path not found: {filepath}")
            continue
        
        # Keeps record of all files accessed
        source_path.append(filepath)
    
    # Returns Message If No Valid Input
    if not source_path:
        print("Error: No valid paths entered")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Prompting User to Identify which file they'd like to manipulate
    print("\n")
    print("=" * 60)
    print("\nBelow is the list of files you selected:\n")
    
    for index, value in enumerate(source_path):
        print(f"{index+1}. {value}")
    
    # File Selection
    while True:
        try:
            inputvalue = int(input("\nPlease select the file you would like to manipulate: "))
            
            # Checks to ensure valid user input
            if inputvalue < 1 or inputvalue > len(source_path):
                print(f"Error: {inputvalue} is not a valid selection.")
                continue
            
            # Adjust index to match list indexing (subtract 1)
            selected_file = source_path[inputvalue - 1]
            print(f"You selected {selected_file}")
            break
        
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Action Selection
    print("\n")
    print("=" * 60)
    print("\nBelow is a list of actions available:\n")
    for index, value in enumerate(action_choice):
        print(f"{index+1}. {value}")
    
    while True:
        try:
            inputaction = int(input("\nPlease select the action you would like to apply: "))
            
            # Checks to ensure valid user input
            if inputaction < 1 or inputaction > len(action_choice):
                print(f"Error: {inputaction} is not a valid selection.")
                continue
            
            # Adjust index to match list indexing (subtract 1)
            selected_action = action_choice[inputaction - 1]
            print(f"You selected {selected_action}")
            break
        
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()