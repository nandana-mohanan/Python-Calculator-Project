def read_my_file():
    filename = "sample.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("--- File Content ---")
            print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it first.")

read_my_file()