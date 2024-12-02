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



total_value = 0
for i in range(1000):
    count = list2.count(list1[i])
    total_value = total_value + (list1[i] * count)
    print(f"Count  [{i}] {list1[i]} and {count}: {total_value}")

print("Similarity score?", total_value)