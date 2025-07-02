book_path = "grocery_list.txt"
book_file = open(book_path)

for line in book_file:
    line = line.strip()
    print(line)
    
book_file.close()