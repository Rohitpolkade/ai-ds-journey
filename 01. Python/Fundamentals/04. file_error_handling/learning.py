#file handling
with open(r"C:\Users\rohit\OneDrive\Desktop\AI-Journey\Python\Revision\Day5\learning.txt", "a") as f:
    f.write("This is a new line")
print("File written successfully!")

with open("learning.txt", "r") as f:
    data = f.read()
    print(data)

# Exception handling
try: 
    with open("sample.txt", "r") as file:
        print(data = file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed!")
