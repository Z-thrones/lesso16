print("We are making a right angle triangle")
n = int(input("Please enter a number that will be the number of rows: "))
for i in range(0 , n):
    for j in range(i+1):
        print(" *" , end = "")
    print()