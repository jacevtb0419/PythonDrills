file_path = "names.txt"
file = open(file_path)

for name in file:
    last_name, first_name = name.strip().split(",")
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print(first_name, last_name)

file.close()