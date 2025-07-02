def choose(options):
    print("You can:")
    for option in options:
        print(option)
    
    while True:
        choice = input("What will you do? ")
        if choice in options: 
            return choice
        else:
            continue 
            
            
            




choose(['quit', 'nap', 'fight'])
