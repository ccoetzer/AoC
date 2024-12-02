# Open a file named 'example.txt' in read mode
with open('day2\input.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

# Split the content into lines
lines = content.splitlines()

lineArray = []


# Iterate over each line
for line in lines:
    # Split the line by three spaces
    numbers = line.split(' ')
    lineArray.append(numbers)

safeReports = 0

def isIncreasing(array, isGoingUp):
    # Iterate through the array and check if each element is less than the next one
    for i in range(len(array) - 1):
        if abs(int(array[i]) - int(array[i + 1])) > 3:
            return False
        if abs(int(array[i]) - int(array[i + 1])) == 0:
            return False
        if not isGoingUp and (int(array[i]) < int(array[i + 1])) :
            return False
        if isGoingUp and (int(array[i]) > int(array[i + 1])) :
            return False
    return True


# Iterate through each line in lineArray
for line in lineArray:
    # Iterate through each item in the line
    print(line) 
    isGoingUp = int(line[1]) > int(line[0])
    isSafe = isIncreasing(line, isGoingUp)

    if not isSafe:
       for i in range(len(line)):
          new_array = line.copy()
          new_array.pop(i)
          print(new_array) 
          isStillGoingUp = int(new_array[1]) > int(new_array[0])
          isSafe = isIncreasing(new_array, isStillGoingUp)
          if isSafe:
              break

    if isSafe:
        safeReports += 1

    print(isGoingUp, isSafe, safeReports) 


