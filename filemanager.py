import os

def create_file(filename, content=""):
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(filename, 'x') as f:
            f.write(content)
        print(f"Created file: {filename}")
    except FileExistsError:
        print(f"Error: '{filename}' already exists.")

def list_files():
    items = os.listdir()
    if not items:
        print("Directory is empty.")
    else:
        print("Files in current directory:")
        for item in items:
            print(" -", item)

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")

def main():
    while True:
        command = input(">> ").strip()

        if command.startswith("touch "):
            try:
                parts = command.split('"')
                filename = parts[1]
                content = parts[3] if len(parts) > 3 else ""
                create_file(filename, content)
            except IndexError:
                print("")

        elif command == "ls":
            list_files()

        elif command.startswith("cd "):
            parts = command.split(" ", 1)
            if len(parts) == 2:
                folder = parts[1].strip().rstrip("/")
                change_directory(folder)
            else:
                print("")

        elif command in ["exit", "quit"]:
            print("Exiting file manager.")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()