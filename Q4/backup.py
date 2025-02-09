# Python script to create backups of the files in the source directory into the destination directory.

# Provides functions to interact with the operating system
import os  

# Allows file operations such as copying
import shutil  

# Enables command-line argument handling
import sys  

# Used to generate timestamps
import datetime  

def backup():
    """
    Reads command-line arguments, checks directories, and copies files.
    Ensures unique file names by appending a timestamp if necessary.
    """
    
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        return
    
    # Get source and destination directory paths from command-line arguments
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists
    if not os.path.exists(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        create_dir = input("Do you want to create it? (yes/no): ").strip().lower()
        if create_dir == "yes":
            os.makedirs(destination_dir)
            print(f"Created destination directory '{destination_dir}'.")
        else:
            print("Exiting program.")
            return
    
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        
        # Full path of the source file
        source_path = os.path.join(source_dir, filename)  
        
        # Full path for the destination file
        destination_path = os.path.join(destination_dir, filename)  
        
        # Check if the current item is a file
        if os.path.isfile(source_path):
            
            # If a file with the same name already exists in the destination, rename it with a timestamp
            if os.path.exists(destination_path):
                
                # Generate a timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
                
                # Split filename into name and extension
                filename_parts = os.path.splitext(filename)  
                
                # Append timestamp to filename
                new_filename = f"{filename_parts[0]}_{timestamp}{filename_parts[1]}"  
                
                # New destination path
                destination_path = os.path.join(destination_dir, new_filename)  
                
                print(f"File '{filename}' already exists. Renaming to '{new_filename}'.")
            
            # Copy the file from source to destination
            shutil.copy2(source_path, destination_path)
            print(f"Copied '{filename}' to '{destination_path}'.")

# Execute function
backup()
