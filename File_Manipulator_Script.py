import os
import sys

#def keywordSearch(filepath):



def main():
	#Printing Header
	print("=" * 60)
	print("The Ultimate CSV/Text File Manipulation Script")
	print("Developed by Sebastian Caballero")
	print("=" * 60)

	#Initiating Path Tracker
	source_path = []
	print("\nEnter the name of the file you'd like to work on.")
	print("Please include the file path as well. Type 'done' once you've processed all desired files.\n")

	while True:
		filepath = input("Please locate the file(s) you'd like to work on (Type 'done' if there are no more files to manipulate): ").strip()

		#Checks if user is done
		if filepath.lower() == 'done':
			break

		#Removes leading/trailing double-quotes if detected
		if '\"' in filepath:
			filepath = filepath.strip('\"')
	        
	    # Validate path
		if not os.path.exists(filepath):
			print(f"Error: Path not found: {filepath}")
			continue

		#Keeps record of all files accessed
		source_path.append(filepath)

	#Returns Message If No Valid Input
	if not source_path:
		print("Error: No valid paths entered")
		input("Press Enter to exit...")
		sys.exit(1)
	



if __name__ == "__main__":
    main()