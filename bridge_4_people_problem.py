# You have four people who need to move across a bridge. Each person moves at a different speed, and the cost of moving them is based on their individual speed. The cost of moving a person is equal to the time they take to cross.

# The movement rules are as follows:

# If a single person moves alone, the action cost is equal to their individual crossing time.
# If two people move together, they must walk at the speed of the slower person. The action cost is determined by the person with the highest crossing time in the pair.



    
def renderGameState(leftState, rightState, flashLightState, currentCost):
    leftPeople  = ', '.join(leftState) if len(leftState) else "Empty"
    rightPeople  = ', '.join(rightState) if len(rightState) else "Empty"

    print(f"{leftPeople} {'(Flashlight)' if flashLightState == 'L' else ''} ------------- {'(Flashlight)' if flashLightState == 'R' else ''} {rightPeople}")
    print(f"\nCurrent Cost: {currentCost}")

def parseSelectedOptions(individuals, validOptions, input):
    parsed = [int(selected) for selected in input.split(",") if selected]

    if(len(parsed) < 1 or len(parsed) > 2):
        raise Exception("Must select a minimum of 1 option and a maximum of 2 option")

    if(not(all([(selected >= 1 and selected <=4) for selected in parsed]))):
        raise Exception("Invalid range detected: valid range 1-4")
    
    parsed = [individuals[selected - 1] for selected in parsed]
    
    for selected in parsed:
        if(selected not in validOptions): raise Exception("Invalid selection: Valid options are: "+ ', '.join(validOptions))
    
    return parsed


def main():
    state = {
        "Teen": "L",
        "Young Adult": "L",
        "Adult": "L",
        "Elderly": "L",
    }
    individualCost = {
        "Teen": 1,
        "Young Adult": 2,
        "Adult": 5,
        "Elderly": 10,
        }
    totalCost = 0
    flashlight = "L"
    

    while 1:

        left = [key for key, value in state.items() if value == "L"]
        right = [key for key, value in state.items() if value == "R"]

        renderGameState(left, right, flashlight, totalCost)

        if(all(value == "R" for value in state.values())):
            print("\nYou've successfully moved everyone to the right.")
            break

        currentOptions = [
            f"{index+1} = {value}({individualCost[value]})" for index, value in enumerate(state.keys()) if (
                value in (left if flashlight == "L" else right)
            )
        ]

        rawSelectedOptions = input(f"\nChoose one or two individuals to cross the bridge. You can only select a max of 2 people to cross the bridge at a time ({", ".join(currentOptions)}): ")

        try:  
            parsedSelectedOptions = parseSelectedOptions(list(state.keys()), list(left if flashlight == 'L' else right), rawSelectedOptions)
        except Exception as e:
            print("Error: ", e)
            print("\n-------------------\n")
            continue

        
        flashlight = 'R' if flashlight == 'L' else 'L'

        totalCost = totalCost + max(individualCost[parsedSelectedOptions[0]], individualCost[parsedSelectedOptions[1]] if len(parsedSelectedOptions) == 2 else 0)

        for selected in parsedSelectedOptions:
            state[selected] = 'R' if state[selected] == 'L' else 'L'

                         
        
        print("\n----------Game State Updated---------\n")


        

          
main()