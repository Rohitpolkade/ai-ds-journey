# file handling
with open("student.txt", "w") as file:
    file.write("This file is created for students details:\n")
    file.write("Rohit\n")
    file.write("Kabir")

with open("student.txt", "r") as file:
        data = file.read()
        print(data)

with open("student.txt", "a") as file:
      file.write("\nDev")

# exeception handling
try:
      with open("abc.txt", "r") as file:
            print(file.read())

except FileNotFoundError:
      print("File does not exist")

finally: 
      print("Execution completed!")
  