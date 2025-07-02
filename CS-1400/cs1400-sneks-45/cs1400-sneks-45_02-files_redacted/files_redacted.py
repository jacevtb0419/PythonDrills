file_path = "messages.txt"
file = open(file_path)

for line in file:
    line = line.strip()
    line = line.replace("James Bond", "[Redacted]")
    print(line)


file.close()