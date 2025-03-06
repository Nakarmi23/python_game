# You are doing some gardening, and need exactly 4 liters of water to mix up some special formula for your award winning roses.

# But you only have a 5-liter and a 3-liter bowl, but do have access to plenty of water.

# How would you measure exactly 4 liters?

def main():
    state = [0,0]
    while 1:
        print(f"5 liter Bucket: {state[0]}")
        print(f"3 liter Bucket: {state[1]}")
        
        if(state[0] == 4 and state[1] == 0):
            print("\nYou've successfully mixed up some special formula for your award winning roses.")
            break

        action = input("\nAction (1 = Fill, 2 = Empty, 3 = Transfer): ")

        match action:
            case "1":
                bucket = input("Choose a bucket to fill (1 = 5 Liter Bucket, 2 = 3 Liter Bucket): ")
                
                if(bucket == "1"):
                    state[0] = 5
                else:
                    state[1] = 3
            case "2":
                bucket = input("Choose a bucket to empty (1 = 5 Liter Bucket, 2 = 3 Liter Bucket): ")

                if(bucket == "1"):
                    state[0] = 0
                else:
                    state[1] = 0
            case "3":
                bucket = input("Choose a bucket to transfer from (1 = 5 Liter Bucket, 2 = 3 Liter Bucket): ")
                match bucket:
                    case "1":
                        toFill = 3 - state[1]

                        if(state[0] < 1):
                            print("The 5 Liter Bucket is empty")
                        elif(toFill != 0):
                            state[1] = state[1] + min(toFill, state[0])
                            state[0] = state[0] - min(toFill, state[0])
                        elif(toFill == 3):
                            print("The 3 Liter Bucket is already full")
                    case "2":
                        toFill = 5 - state[0]

                        if(state[1] < 1):
                            print("The 3 Liter Bucket is empty")
                        elif(toFill != 0):
                            state[0] = state[0] + min(toFill, state[1])
                            state[1] = state[1] - min(toFill, state[1])
                        elif(toFill == 5):
                            print("The 5 Liter Bucket is already full")
                    case _:
                        print("Invalid Input!")
            case _:
                print("Invalid Input!")
        
        print("\n-------------------\n")



main()