try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")