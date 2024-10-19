import os

files = "file.txt"


def open_new_file():
    if not os.path.exists(files):  
        with open(files, 'w') as file:
            pass  # Create the file if it doesn't exist


# Create a new note
def create():
    user_input = input("Enter the note: ")
    with open(files, 'a') as file:
        file.write(user_input + '\n')  
        print("Note added successfully!")


# Read (list) all notes
def read():
    if os.stat(files).st_size == 0:  # Check if the file is empty
        print("No notes available.")
        return
    
    with open(files, 'r') as file:
        notes = file.readlines()  

    
    print("Notes:")
    for i, note in enumerate(notes, start=1):  
        
        print(f"{i}. {note.strip()}")  


# Update a note
def update():
    read() 
    note_number = int(input("Enter the note number to update: ")) 
    with open(files, 'r') as file:
        notes = file.readlines()  

        
    if note_number < 1 or note_number > len(notes):
        print("Invalid note number!")
        return

    new_content = input("Enter the new content: ")
    notes[note_number - 1] = new_content + '\n'  # Update the selected note

    with open(files, 'w') as file:
        file.writelines(notes)  # Write the updated notes list back to the file

    print("Note updated successfully!")


# Initialize the file and test the functions
if __name__ == "__main__":
    open_new_file() 

    # Simple testing
    while True:
        print("\n1. Create a note")
        print("2. Read notes")
        print("3. Update a note")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
