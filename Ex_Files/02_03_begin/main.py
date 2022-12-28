NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] #prints everything before index 2 (3rd item)
GEORGE_RINGO = NAMES[2:] #prints everything after index 2 (3rd item)
REVERSE = NAMES[::-1]   #start point = 0, end point = 0, step -1 (backwards), so print the list backwards
EVERY_OTHER = NAMES[::2] #start point = 0, end point = 0, step by 2, so print every other item

# Theses lines use built in functions to calculate:
print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
