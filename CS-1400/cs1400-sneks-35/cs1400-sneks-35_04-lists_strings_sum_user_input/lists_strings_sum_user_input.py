sum = 0
list = input("Write a list of numbers separated by commas:") 
for item in list.split(","):
    sum = sum + int(item)
print(sum) 
 