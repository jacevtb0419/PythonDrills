from cisc108 import assert_equal
def render_introduction():
    '''
    Create the message to be displayed at the start of your game.

    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return '''

    -Introduction-

    Welcome to the Corrupt Mayor!
    -----------------------------
    The city needs your help! The corrupt mayor is acting unethically to make himself
    rich while disregarding the needs of the people and preventing an election from being held.
    You will need to rally the people together to save the city and its residents. 
    Serve the citizens and they will support your mission.
    Get the ballots from the courthouse and place them in the ballot box to hold an election.
    You will need to convince the majority of the citizens to vote for you and not the corrupt mayor.
    Be careful, the mayor may try to seduce you to join his ranks!

    -How to Play-
    To navigate the city, you can use the following commands:
    goto: Move to a different location
    use: Use an item in your inventory, you will also use this command to complete tasks
    completing tasks will help you progress in the game and gain the trust of the citizens. 
    talkto: Talk to a person at your current location
    quit: Exit the game
    take: Pick up an item 

    after you put in a command, you will be prompted to enter a location or an action.
    Example:
    >talkto
    You can talk to: guide
    Who do you want to talk to?>guide
    
    -Inventory and Actions-
    Your inventory will be displayed at the bottom of the screen whenever you move.
     You can use the inventory to keep track of items you have collected.
    Any actions you can take will be displayed as well.
    Example:
    You are in town square
    You can talk to: guide  --- people you can talk to and help
    You can go to: main street, joe's bar, park --- places you can go
    You can take: city map --- items you can take and use. Some items can only be used in certain locations 
    You can: quit, goto, use, talkto, take --- actions you can take


    -MAP-
    You can also use the city map to help you navigate the city.
    The map shows the layout of the city and the locations of important places.
    You can use the map to find your way around the city and to find the locations of important places.
    The map is located in the town square. You can take it and use it to help you navigate the city.
    

   -Ending-
   The game will end when the ballots are placed in the ballot box and the election is held.
   You will count the votes and see if the citizens have voted for you or the corrupt mayor.
   If you win, you will be the new mayor of Sadrena and the city will be free from corruption.
   If you lose, the corrupt mayor will remain in power and will continue be even more evil than before.
   You will be given a message at the end of the game to let you know if you won or lost.
   You can also quit the game at any time by typing 'quit' at the prompt.

   Good luck, and may the citizens of Sadrena be with you!


    '''

def create_world():
    '''
    Creates a new version of the world in its initial state.

    Returns:
        World: The initial state of the world
    '''
    return {
      'map': create_map(),
      'player': create_player(),
      'status': "playing"
  }

def create_map():
  #List of all the locations in the game
  #town square, main street, mayor's house, park, city hall, the courthouse, 
  #joe's bar, widower's house, jack and jane, joe's house, abandoned house

  #list of all the people in the game
  #{guide: read map, mayor:show document  judge: open door, jack:give cash, jane:feed cat, joe:clean floor, widower:place picture}, 
  #
  #List of all the items in the game
  #city map, document, booze, broom, old picture, cat food, cash pile, courthouse key

#list of all the tasks in the game
    #open door, clean, place picture, feed cat, 


  return {
      'town square': {
          'neighbors': ["main street", "joe's bar", "park"],
          'about': 
          '''
          This is the center of the city of Sadrena! You woke up here in enough pain to make you regret waking up.
          To your North is the Main Street, the East has a local bar, the South you can see a park and the city hall beyond it, 
          ''',
          'stuff': ["city map"],
          'people': {"guide":{'dialogue 1': 
        '''
        Hello! Welcome to Sadrena! 

        Try taking the city map. It will help you navigate the city.
        use the command 'take' and press enter, then type 'city map' and press enter again.
        After that, you can use the command 'use' and press enter, then type 'city map' and press enter again.
        ''',
          'status': False }},
          'tasks': []
        
      },
      'main street': {
          'neighbors': ["mayor's house", "joe's house", "town square"],
          'about': 
          '''
          Main street: Lots of businesses and homes are here.
          Old man 'joe's house' is to the east. 
          You see a large house to the north that appears to be the 'mayor's house' and the 'town square' to the south.' 
          ''',
          'stuff': [],
          'people': {},
          'tasks': []
      },
      "mayor's house": {
          'neighbors': ["main street", "abandoned house"],
          'about': 
          '''
          This is the corrupt mayor's house, He's usually at the city hall. I wonder what's inside... 
          There seems to be a document in the mailbox.
          You can see 'main street' to the south 
          ''',
          'stuff': ['document'],
          'people': {},
          'tasks': []
      },
      "park": {
          'neighbors': ["city hall", "town square"],
          'about': 
          '''
          A beautiful park. There's so many people here enjoying the day.
          There's a broken down broom in the corner of the park.
          I wonder if it belongs to someone?
          there's the bustling 'town square' to the north. 
          You can see the sublime 'city hall' to the south. It looks like it's really important to the city.
          ''',
          'stuff': ["broom"],
          'people': {},
          'tasks': []
      },
      "city hall": {
          'neighbors': ["courthouse", "park"],
          'about': 
          '''
            This is the city hall. The mayor's office is here.
            he's just inside the door. You can see him watching you from the window.
            It's almost like he knows you're here to stop him.
          ''',
          'stuff': [],
          'people': {"mayor":{'dialogue 1': 
          '''
          Hello there! I'm the mayor of this city. 
          I hope you're ready for election day friend. 
          I just need you to not do anything stupid and everything will be fine.
          You better stay out of my way or else I'll have to take care of you myself.                
          ''',                     
         'status': False }},
          'tasks': []
      },

      "courthouse": {
          'neighbors': ["city hall",],
          'about': 
          '''
          You see a large building with a sign that says "Courthouse" on it.
          This is where the election will be held. The judge is waiting for you to open the door.
          The courthouse is locked and you need to find the key to open it.
          ''',
          'stuff': ['ballots'],
          'people': {"judge":{'dialogue 1': '''
            Hello! I'm the judge of this city. I need your help to hold an election.
            I lost the key to the courthouse and I can't open the door.
            I need you to find the key and open the door for me so that the election can be held.
        ''',
          'status': False }},
          'tasks': []
      },
      "joe's bar": {
          'neighbors': ["joe's house", "town square"],
          'about': 
          '''
          It's a bar. It's a bit run down, but it's a nice place to relax.
          You can see joe's house to the north behind the bar
          the 'town square' to the west is bustling with noise.
          An old widower sits outside his house to the east.
          ''',
          'stuff': ["booze"],
          'people': {"jack":{'dialogue 1': 
          '''
          Old Joe is a good guy. He runs this bar and takes care of the people in the city.
          But the mayor is trying to shut him down. He wants to take over the bar and turn it into a casino.
          I don't know why, but the mayor is corrupt and greedy. He doesn't care about the people.
          It's out of my control. 
            
          I'm out of money for drinks though, can you run to my house and get me some cash?
          ''', 'status': False }},
          'tasks': []
      },
      "widower's house": {
          'neighbors': ["jack and jane", "joe's bar",],
          'about': "An old widower sits outside his house. He looks sad and lonely.",
          'stuff': ["old picture"],
          'people': {"widower": { 'dialogue 1': 
          '''
          I used to be the mayor of this town. I was a good mayor, but the new mayor is evil.
          He doesn't care about the people. I want to help you replace him.
          But first, I need you to take this picture to our old home and place it on my wife's grave.
          It would mean a lot to me.
          ''', 
          'status': False }},
          'tasks': []
      },
      "jack and jane": {
          'neighbors': ["abandoned house", "widower's house", "joe's house"],
          'about': "This is the house of Jack and Jane. They are a newly wed couple who live here. You see Jane outside the house with her cat",
          'stuff': ["cash"],
          'people': {"jane":{'dialogue 1': 
            '''
            You must be new, I'm Jane. I live here with my husband Jack. We just got married and we're very happy.
            But I can't find Jack anywhere. He was supposed to be home by now. I hope he's okay.
            I think he went to the bar to get some drinks. Can you go check on him?
            Take this cash pile to him. He'll be happy to see you.
            If you have a moment, can you help me with my cat? He's pretty hungry and I need to feed him.
            ''', 
            'status': False }},
          'tasks': []
      },
      "joe's house": {
          'neighbors': ["main street", "joe's bar", "jack and jane"], 
          'about': "",
          'stuff': ["courthouse key"],
          'people': {"joe":{'dialogue 1': '''
          Hello sir, The name's Joe. I own the bar in town. Life has been crazy lately.
            The mayor is trying to shut me down and take over my bar. I don't know why, but he won't leave me alone.
            I need your help to keep the bar open. I need you to clean the bar and make it look nice.
            If you can do that, you'll have my gratitude and vote. 
          ''', 'status': False }},
          'tasks': []
      },
      "abandoned house": {
          'neighbors': ["jack and jane"],
          'about': '''
          It's empty and abandoned. There's a grave outside with a lot of pictures and flowers
          You can see 'jack and jane' to the south.
          ''',
          'stuff': ["cat food"],
          'people': {},
          'tasks': []
  }
  }

def create_player():
  return {
      'location': 'town square',
      'inventory': [],
  }

def render_location(world):
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    inventory = world['player']['inventory']
    inventory_str = ', '.join(inventory) if inventory else "nothing"

  # ...
    return "You are in "+ location +"\n"+ about  +"\nYou have " + inventory_str + " in your inventory" 
    

def render_visible_stuff(world):
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']

    visible_stuff = []
    for thing in stuff:
        if thing not in inventory:
            visible_stuff.append(thing)
    if visible_stuff:
        return "\nYou see: " + ', '.join(visible_stuff)
    else:
        return ""
        

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the world.
    '''
    return (render_location(world) +
          render_visible_stuff(world))

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.

    Args:
        world (World): The current world to get options for.

    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    location = world['player']['location']
    here = world['map'][location]
    commands = ["quit"] # Always include quit
    if here['neighbors']:
        commands.append("goto")
        print("You can go to: " + ', '.join(world['map'][location]['neighbors']))
    if here['tasks']:
        print("You can: " + ', '.join(world['map'][location]['tasks']))
    if here['people']:
        commands.append("talkto")
        print("You can talk to: " + ', '.join(world['map'][location]['people']))
    if here['stuff']:
        commands.append("take")
        print("You can take: " + ', '.join(world['map'][location]['stuff']))
    if world['player']['inventory']:
        commands.append("use")
        print("You can use: " + ', '.join(world['player']['inventory']))



 
  # ...
  # Add more commands here
  # ...
    return commands
    

    

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.

    Args:
        world (World): The current world to modify.

    Returns:
        str: A message describing the change that occurred in the world.
    '''
    location = world['player']['location']
    here = world['map'][location]
    neighbors = here['neighbors']
    people = here['people']
    inventory = world['player']['inventory']
    
    if command == "quit":
        world['status'] = "quit"
        return "You have quit the game."
    if command == "goto":
        print("You can go to: " + ', '.join(neighbors))
        destination = input("Where do you want to go? ")
        if destination in neighbors:
            world['player']['location'] = destination
            return "You have moved to " + destination
        else:
            return "You can't go there."
    if command == "talkto":
        print("You can talk to: " + ', '.join(people))
        interaction = input("Who do you want to talk to? ")
        if interaction in people: 
            return people[interaction]['dialogue 1']
        else: 
            return "You can't talk to that person."
    if command == "take":
        print("You can take: " + ', '.join(here['stuff']))
        item = input("What do you want to take? ")
        if item in here['stuff']:
            world['player']['inventory'].append(item)
            here['stuff'].remove(item)

            item_to_task_and_location = {
                "city map": ("read map", "town square"),
                "broom": ("clean", "joe's bar"),
                "old picture": ("place picture", "abandoned house"),
                "cat food": ("feed cat", "jack and jane"),
                "courthouse key": ("open door", "courthouse"),
                "cash": ("give cash", "joe's bar"),
                "document": ("show document", "city hall"),
                "ballots": ("place ballots", "courthouse")
        }

        # Append the task to the correct location
        if item in item_to_task_and_location:
            task, location = item_to_task_and_location[item]
            if task not in world['map'][location]['tasks']:  # Avoid duplicate tasks
                world['map'][location]['tasks'].append(task)
            return "You have taken the " + item
        else:
            return "You can't take that."


    if command == "use":
        print("You can use: " + ', '.join(inventory))
        item = input("What do you want to use? ")
        if item in inventory:
            #
            #Use the City Map anywhere
            if item == 'city map':
                if location == "town square":
                    if "read map" in here['tasks']:
                        here['tasks'].remove("read map")
                    world['map']['town square']['people']['guide']['status'] = True
                    return '''
                        Great! You read the map. This is what it shows:
                        Now you can use the map to navigate the city.
                        Try using the command 'goto' and press enter, then type the name of the
                        location you want to go to and press enter again.
                        You can only go to locations that are connected to the current location.

                        |--mayor's house--------------abandoned house|
                        |---main street--joe's house--jack and jane--|
                        |--town square--joe's bar--widower's house---|
                        |--park--------------------------------------|
                        |--city hall--courthouse---------------------|
                        '''
                else: 
                    return '''
                    You look at the map. It shows the layout of the city.

                    |--mayor's house--------------abandoned house|
                    |---main street--joe's house--jack and jane--|
                    |--town square--joe's bar--widower's house---|
                    |--park--------------------------------------|
                    |--city hall--courthouse---------------------|
                    '''
                
#use broom to clean the bar sets Joe to True 

            elif item == "broom" and location == "joe's bar":
                here['tasks'].remove("clean")
                world['player']['inventory'].remove(item)
                world['map']["joe's house"]['people']["joe"]['status'] = True
                return "You sweep the floor with the broom. It makes Old Joe happy."
                
#Use the old picture on the grave to set the widower to True
            elif item == "old picture" and location == "abandoned house":
                here['tasks'].remove("place picture")
                world['player']['inventory'].remove(item)
                world['map']["widower's house"]['people']["widower"]['status'] = True
                return "You place the picture on the grave. The widower is grateful."
            
#just a fun item to use
            elif item == "booze":
                world['player']['inventory'].remove(item)
                return "You drink the booze. It takes the pain away."
            
#use the document to set the mayor to True
            elif item == "document" and location == "city hall":
                    here['tasks'].remove("show document")
                    world['player']['inventory'].remove(item)
                    world['map']["city hall"]['people']["mayor"]['status'] = True
                    return '''You show the document to the mayor. He is not happy.
                    What is this? I can't believe that the towns people think of me this way.
                    How could I let them all down? I thought I was doing the right thing.
                    I thought I was helping the city. I thought I was making it better.
                    How could I even run again? I'll vote for you instead. 
                    '''
#use the cat food to set Jane to True
            elif item == "cat food" and location == "jack and jane":
                here['tasks'].remove("feed cat")
                world['player']['inventory'].remove(item)
                world['map']["jack and jane"]['people']["jane"]['status'] = True
                return "You feed the cat. It purrs happily."

#use the courthouse key to set the judge to True and give the player the task to place ballots to win or lose the game
            elif item == "courthouse key" and location == "courthouse":
                here['tasks'].remove("open door")
                world['player']['inventory'].remove(item)
                world['map']["courthouse"]['tasks'].append("place ballots")
                world['map']['courthouse']['people']["judge"]['status'] = True
                return '''
                You unlock the door to the courthouse. You can now place the ballots and find out the result.
                The judge is happy to see you. He says, "Thank you for unlocking the door. Now we can hold the election."
        
                
                '''
#use the cash to set Jack to True 
            elif item == "cash" and  location == "joe's bar":
                    here['tasks'].remove("give cash")
                    world['player']['inventory'].remove(item)
                    world['map']["joe's bar"]['people']["jack"]['status'] = True
                    return "You give the cash to Jack. He is happy to see you. He says, 'Thank you for the cash. I can buy more drinks now.'"
           


#use the ballots to win or lose the game
            elif item == "ballots" and location == "courthouse":
                if "place ballots" in here['tasks']:   
                    here['tasks'].remove("place ballots")
                    world['player']['inventory'].remove(item)
                    total_true_status = 0
                    total_false_status = 0
                    for place in world['map'].values():
                        for person in place['people'].values():
                            if person['status'] == True:
                                total_true_status += 1
                            elif person['status'] == False:
                                total_false_status += 1
                    if total_true_status > total_false_status:
                        world['status'] = "victory"
                    elif total_true_status < total_false_status:
                        world['status'] = "defeat"
                    elif total_true_status == total_false_status:
                        world['status'] = "defeat"
                else:
                    return "You can't use that yet."
            else:
                return "You can't use that."
        else:
            return "You don't have that item."



def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.

    Args:
        world (World): The final world state to use in describing the ending.

    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world['status'] == "quit":
        return "Thanks for playing! Goodbye!"
    elif world['status'] == "victory":
        return '''
        Congratulations! You have successfully rallied the citizens of Sadrena
        and overthrown the corrupt mayor. The city is now free, and democracy
        has been restored. The people will remember your heroic efforts forever!

        Thank you for playing!
        '''
    elif world['status'] == "defeat":
        return '''
        Unfortunately, the corrupt mayor has outsmarted you. The city remains
        under his control, and the citizens continue to suffer. Better luck next time!

        Thank you for playing!
        '''
    else:
        return "The game has ended. Thanks for playing!"
   
    

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.

    Note:
        Use your answer to Programming Problem #42.3

    Args:
        options (list[str]): The potential commands to select from.

    Returns:
        str: The command that was selected by the user.

    '''
    print("You can: " + ', '.join(options))
    
    while True:
        choice = input("What will you do? ")
        if choice in options: 
            return choice.lower()
        else:
            print("Invalid command. Please try again.")
            

############# Main Function ##############
# Do not modify anything below this line #
##########################################
def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()