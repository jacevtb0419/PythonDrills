file_path = "rainfall.txt"
file = open(file_path)

total = 0
for line in file:
    line = line.strip()
    value = float(line)
    total = total + value

file.close()
print(total)

