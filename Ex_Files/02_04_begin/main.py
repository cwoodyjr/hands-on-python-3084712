NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
print("This is a while loop:")
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

print("This is a for in (for each) Loop")

for name in NAMES:
    print(name)

print("This is a for zip loop ")

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate
#this will iterate through the list and print
#the index number with the item
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
