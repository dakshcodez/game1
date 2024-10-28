from_direction='W'
to_direction='E'
west=['c','f','g']
east=[]

def swtich_sets(from_direction, to_direction, west, east, items_carried):
    if to_direction=='E':
        if items_carried=='n':
            pass
        elif items_carried in west:
            west.remove(items_carried)
            east.append(items_carried)
        else:
            pass


    elif to_direction=='W':
        if items_carried=='n':
            pass
        elif items_carried in east:
            east.remove(items_carried)
            west.append(items_carried)
        else:
            pass


def switch_dir(from_direction,to_direction):
    return to_direction, from_direction
    

print('A farmer with a fox, a goose, and a sack of corn needs to cross a river.\nNow he is on the west side of the river and wants to go to the east side.\nThe farmer has a rowboat, but there is room for only the farmer and one of his three items.\nUnfortunately, both the fox and the goose are hungry. The fox cannot be left alone with the goose, or the fox will eat the goose.\nLikewise, the goose cannot be left alone with the sack of corn, or the goose will eat the corn.\nGiven a sequence of moves, find if all three items—fox, goose, and corn—are safe.\nThe input sequence indicates the item carried by the farmer along with him in the boat.\n‘F’ – Fox, ‘C’ – Corn, ‘G’ – Goose, ‘N’ – Nothing.\nAs he is now on the western side, the first move is to the east, and the direction alternates for each step.')

while True:
    
    items_carried=input("Enter the item u r carrying (c,f,g,n): ") 
    
    swtich_sets(from_direction, to_direction, west, east, items_carried)
    
    print("west: ",west)
    print("east: ",east)

    from_direction, to_direction=switch_dir(from_direction, to_direction) #SHOUTOUT X.COM/SOFASPAWN

    
    if from_direction=='E':
        print("Headed W--------->E")
        print("Now heading W<---------E")
        if set(['g', 'f']).issubset(set(west)) or set(['g', 'c']).issubset(set(west)):
            
        
            print("You failed the task")
            break

    elif from_direction=='W':
        print("Headed W<---------E")
        print("Now heading W--------->E")
        if set(['g', 'f']).issubset(set(east)) or set(['g', 'c']).issubset(set(east)):
            
        
            print("You failed the task")
            break

   
    if west==[]:
        print("Congratulations you won the game.")
        print()
        print("Thanks for the playing the beta version of this game, we will be updating it with much more features. Please follow me @dakshcodez on Github")
        print("Credits\nDeveloped and Designed by Daksh Arora\nGame idea mentioned in my Python Lab professor's ppt\nThis game is the property of Daksh Arora")
        print("Acknowledgements")
        print("This game CAN be copied and reused, it has no copyright policy, as long as u mention that I have made this game")
        print("Game Studio: Arora Studios")
        print("Beta Launch 2024")
        break

a=input() #only exists to run this on terminal
