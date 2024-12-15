import os

def Create_File(filename):
    try:
        with open(filename, "x") as f:
            print(f"{filename} successfully created.")
    except FileExistsError:
        print("{filename} already exists")
    except Exception as e:
        print("Error occured")

def Remove_file(filename):
    try:
        os.remove(filename)
        print("File successfully deleted")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error occured")

def view_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        for file in files:
            print(file)

def read_files(filename):
    try:
        with open(filename, "r") as f:
            store = f.read()
            if not store:
                print(f"Content of the {filename} is empty.")
            else:
                print(f"Contents of the {filename} are:\n {store}")
    except FileNotFoundError:
        print("No files were founded")
    except Exception as e:
        print("An error occured")


def main():
    while True:
        print("1: Create_File")
        print("2: Remove_file")
        print("3: view_files")
        print("4: read_files")
        print("5: to exit")

        choose = input("Enter your choice: ")
        while choose not in["1","2","3","4", "5"]:
            choose = input("Enter your choice: ")
        
        if choose == "1":
            filename = input("Enter a file name: ")
            Create_File(filename)
        elif choose == "2":
            filename = input("Enter a file name to remove: ")
            Remove_file(filename)
        elif choose == "3":
            view_files()
        elif choose == "4":
                filename = input("Enter a file name: ")
                read_files(filename)
        elif choose == "5":
            print("Thank you.")
            break
        else:
            continue

main()


