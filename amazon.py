# opened input txt file and readlines
file = open("input.txt", "r")
files_1 = file.readlines()
print(files_1)

# used a for loop
for lines in files_1:
    files = lines[4:]
    files = files.strip("\n").strip("ï»¿min:")
    files = files.split(",")
     

    # used a for loop 
    for x in range(0,len(files)):
        files[x] = int(files[x])

# created a function that calculates the minimum number
def minimum(numbers):
    minimum_number = min(numbers)
    return minimum_number

# created a function that calculates the maximum number
def maximum(numbers):
    maximum_number = max(numbers)
    return maximum_number

# created a function that calculates the average number
def average(numbers):
    average_number = sum(numbers)/len(numbers)
    return average_number

# calculate the min,max and average and stored it in a variable 
minimum_value = f"The minimum of {files} is {minimum(files)}"
maximum_value = f"The maximum of {files} is {maximum(files)}"
average_value = f"The average of {files} is {average(files)}"

# writing to my output.txt file
file_2 = open("output.txt", "w")
file_2.write(str(minimum_value + "\n"))
file_2.write(str(maximum_value + "\n"))
file_2.write(str(average_value))

# closed my files
file.close()
file_2.close()