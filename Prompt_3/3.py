
#! 3) Calculate the average of 10 numbers


#! bit more complex, dynamic version
elements = int(input("Enter the value of elements you want to find the average of: "))

mainArr = []

for i in range(0, elements):
    print("Enter a number")
    arr = int(input())

    mainArr.append(arr)

print("Finding the average now...")

average = 0.0


average = (sum(mainArr)/elements)

print("Oringal list of values: " , mainArr)

print("Average of the list: ", average)



#! Simple version, not dynamic
# print("Please enter 10 values to find the average of")

# mainArr = []

# for i in range(10):
#     arr = int(input())

#     mainArr.append(arr)

# print("Finding the average now...")

# average = 0.0

# for i in range(10):
#     average = (sum(mainArr)/10)

# print("Oringal list of values: " , mainArr)

# print("Average of the list: ", average)

