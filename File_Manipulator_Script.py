import os
import sys

#Prompts the user for keyword, returns list
def PromptKeyword():
    keywordlist = []
    index = 1
    while True:
        keyword = input(f"Keyword #{index} (or 'done' to finish): ").strip()
        if keyword.lower() == 'done':
            break
        # Adds keyword to list
        keywordlist.append(keyword)
    
    return keywordlist

#Searches keyword across file; consider studying memory mapped file handling for future optomization/speed improvements
def KeywordSearch(filepath, keywordlist):
    # Prepare output filename 
    file_name, file_ext = os.path.splitext(filepath)
    output_filepath = f"{file_name}_keyword_matches{file_ext}"
    
    # Initialize counter for matched lines
    matched_lines_count = 0
    
    # Open input and output files with efficient line-by-line reading
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(output_filepath, 'w', encoding='utf-8') as outfile:
        
        # Process file line by line to handle large files efficiently
        for line in infile:
            # Check if any keyword is in the line (case-insensitive)
            if any(keyword.lower() in line.lower() for keyword in keywordlist):
                outfile.write(line)
                matched_lines_count += 1
    
    return matched_lines_count


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

        # Validate filetype DEBUG
        if not filepath.lower().endswith(('.txt', '.csv')):
            print(f"Error: Incorrect filetype. Please only select .txt or .csv")
            continue
        
        # Keeps record of all files accessed
        source_path.append(filepath)
    
    # Returns Message If No Valid Input
    if not source_path:
        print("Error: No valid paths entered")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # File Selection
    print("\n")
    print("=" * 60)
    print("\nBelow is the list of files you selected:\n")
    
    for index, value in enumerate(source_path):
        print(f"{index+1}. {value}")
    
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

    # Keyword Search **QC AND DEBUG THIS**
    if inputaction is 1:
        keyword_list = PromptKeyword()
        matched_lines = KeywordSearch(selected_file, keyword_list)

        print(f"{matched_lines} lines matched the keyword list. Please check the output file for results.")
        

if __name__ == "__main__":
    main()