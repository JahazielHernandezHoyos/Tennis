print("** Super Tennis Annotator **")
player1 = input("Insert player 1's name: ")
player2 = input("Insert player 2's name: ")

print("** Welcome to the Super Tennis Annotator app **")
print("How do you want to use it?")
print("1. Manual input")
print("2. Simulation")
option = input("Choose an option: ")

def manualInput():
    print("Manual input")
    return

def simulation():
    print("Simulation")
    return

def main():   
    if option == "1":
        manualInput()
    if option == "2":
        simulation()
main()
