#import random module
import random

#fake News = subject+ action + object
#create subjects
subjects = ["Shahrukh Khan", "Virat Kolhi", "Nirmala Sitharaman", "John Cena", "Naruto Uzumaki", "Narendra Modi", "Vladimir Putin"]

actions = ["eats", "cancels", "launches","declares war on","orders", "celebrates", "dances"]

objects = ["at Red fort", "in Mumbai local train", "samosa", "at ganga river", "IPL match"]

while True: 
    subj = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)

    headline = f"BREAKING NEWS: {subj} {action} {obj}"
    print("\n" + headline)

    userInput = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if userInput == "no":
        break

print("Thank you for using the Fake News Generator!")