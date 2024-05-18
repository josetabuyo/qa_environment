import os

def create_file_with_random_word():
    # Generate a random word
    
    # Get the root path of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Create the file path
    file_path = os.path.join(project_root, 'output/after_run.txt')
    
    # Write the random word to the file
    with open(file_path, 'w') as file:
        file.write("DEBUGDEBUGDEBUGDEBUG")
    
    return file_path


# Call the function to create the file
file_path = create_file_with_random_word()
print(f"File created at: {file_path}")