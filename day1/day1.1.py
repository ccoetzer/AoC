# Open a file named 'example.txt' in read mode
with open('day1-input.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

# Split the content into lines
lines = content.splitlines()

# Initialize two lists to hold the numbers
list1 = []
list2 = []

# Iterate over each line
for line in lines:
    # Split the line by three spaces
    numbers = line.split('   ')
    # Convert the split strings to integers and add to the respective lists
    if len(numbers) == 2:
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

# Sort list1 from smallest to largest
list1.sort()
list2.sort()

total_abs_value = 0
for i in range(1000):
    abs_value = abs(list1[0] - list2[0])
    total_abs_value += abs_value
    print(f"Absolute [{i}] {list1[0]} and {list2[0]}: {abs_value}")
    list1.pop(0)
    list2.pop(0)


print("Total absolute difference:", total_abs_value)