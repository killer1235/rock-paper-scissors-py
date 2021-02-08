import random 

# a list holding/containing The choices of the game
rsp = ['rock' , "paper" , "scissors"]

# A function to check player input
def PlayerInput():
    # a Variable to store player input
    pl = input("Choose from rock , paper and scissors\n")

    # check if input is invalid 
    if pl.lower() not in rsp:
        print("invalid selection\n")

        # if input is invalid , get player input again 
        PlayerInput()

    return pl

# A function to generate computer input (Randomly)
def CompInput():

    # Randomly Choose a choice 
    cpl = random.choice(rsp)

    # print Computer choice 
    print("computer choose " + cpl + '\n')

    return cpl

def CompareInput(in1 , in2):

    # Lambda may not be really needed but i used it 
    pl_w = lambda: print("Player won!\n")
    cl_w = lambda: print("Computer won!\n")

    # Game conditions 

    if in1 == rsp[0] and in2 == rsp[1]:
        cl_w()

    elif in1 == rsp[1] and in2 == rsp[2]:
        cl_w()

    elif in1 == rsp[2] and in2 == rsp[0]:
        cl_w()

    # if computer chooses same input as player , Tie 
    elif in1 == in2:
        print("Tie!")

    # Player wins (Not tested yet if this fails)
    else:
        pl_w()

# Main function
def main():
    print("Welcome to Rock paper Scissors.\n")

    in1 = PlayerInput()
    in2 = CompInput()
    CompareInput(in1 , in2)

    again = input("want to play again , Y/N\n")

    # doesn't work 
    if again.lower == 'y':
        main()

main()