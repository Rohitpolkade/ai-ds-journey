marks = [90, 80, 70, 85]

def average(marks):
    sum = 0
    for mark in marks:
        sum += mark
    return sum / len(marks)

print(average(marks))


def calculateFeatures(*features):
    total = 0
    for feature in features:
        total += feature
    return total

print(calculateFeatures(12, 45, 67))