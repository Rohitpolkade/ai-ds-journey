'''Condition Statements!'''
marks = 87

if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Good")

else:
    print("Needs Improvement")


'''Loops!'''
numb = [1,2,3]

for num in numb:
    print(num, end = " ")

print()

# nested loop!
for i in range(3):
    for j in range(3):
        print(i, j)

count = 0
while count < 5:
    print(count, end = " ")
    count += 1