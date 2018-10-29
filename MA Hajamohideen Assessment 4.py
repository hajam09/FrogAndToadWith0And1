#(5,4)(3,5)(2,3)(4,2)(6,4)(7,6)(5,7)(3,5)(1,3)(2,1)(4,2)(6,4)(5,6)(3,5)(4,3)
#(3,4)(5,3)(6,5)(4,6)(2,4)(1,2)(3,1)(5,3)(7,5)(6,7)(4,6)(2,4)(3,2)(5,3)(4,5)
import time

def play():
    print("Game Rules: (READ VERY CAREFULLY!)")
    time.sleep(1)
    print("You must move all the frogs (F1, F2 and F3) to right side")
    print("and all the toads (T1, T2 and T3) to the left side")
    time.sleep(2)
    print("Enter a 'From' number to choose your position of the frog/toad")
    time.sleep(1)
    print("enter a 'To' number to send your frod/toad")
    time.sleep(1)
    print("Remember, the frogs can only move right and toads can only move left")
    time.sleep(1)
    print("You can move the frogs/toads to one place that is an empty space")
    print(" or jump over another frog/toad into an empty space.")
    time.sleep(1)
    print("You WIN if you move the frogs and toads to opposite sides")
    time.sleep(1)
    print("If you want to reset the game in the middle of the gameplay")
    print("simply enter the position of an empty space ' ' on (To) input")
    
    def left1():
        temp = frogList[userIndex-1]
        frogList[userIndex-1] = frogList[userIndex]
        frogList[userIndex] = temp
        print(frogList)
        return(frogList)
    
    def right1():
        temp1 = frogList[userIndex+1]
        frogList[userIndex+1] = frogList[userIndex]
        frogList[userIndex] = temp1
        print(frogList)
        return(frogList)

    def left2():
        temp2 = frogList[userIndex-2]
        frogList[userIndex-2] = frogList[userIndex]
        frogList[userIndex] = temp2
        print(frogList)
        return(frogList)

    def right2():
        temp3 = frogList[userIndex+2]
        frogList[userIndex+2] = frogList[userIndex]
        frogList[userIndex] = temp3
        print(frogList)
        return(frogList)

    def invalid():
        print("Invalid Move, Choose Again")

    def won():
        print("You've Won!")


    print("LET'S PLAY!")
    #index       0     1     2     3    4     5     6
    frogList = ['F1', 'F2', 'F3', ' ', 'T1', 'T2', 'T3']

    print(frogList)
    userIndex1 = int(input("From: "))
    userIndex = userIndex1-1

    while userIndex == ' ' or frogList[userIndex] == ' ':
        invalid()
        userIndex1 = int(input("From: "))
        userIndex = userIndex1-1

    while frogList[userIndex] != ' ':
        userMove1 = int(input("To: "))
        userMove = userMove1-1
        difference = userIndex - userMove
        if difference == 1 and frogList[userIndex-1] == ' ' and frogList[userIndex] == 'T1':
            left1()
        elif difference == 1 and frogList[userIndex-1] == ' ' and frogList[userIndex] == 'T2':
            left1()
        elif difference == 1 and frogList[userIndex-1] == ' ' and frogList[userIndex] == 'T3':
            left1()
        elif difference == 2 and frogList[userIndex-2] == ' ' and frogList[userIndex] == 'T1':
            left2()
        elif difference == 2 and frogList[userIndex-2] == ' ' and frogList[userIndex] == 'T2':
            left2()
        elif difference == 2 and frogList[userIndex-2] == ' ' and frogList[userIndex] == 'T3':
            left2()
        elif difference == -1 and frogList[userIndex+1] == ' ' and frogList[userIndex] == 'F1':
            right1()
        elif difference == -1 and frogList[userIndex+1] == ' ' and frogList[userIndex] == 'F2':
            right1()
        elif difference == -1 and frogList[userIndex+1] == ' ' and frogList[userIndex] == 'F3':
            right1()
        elif difference == -2 and frogList[userIndex+2] == ' ' and frogList[userIndex] == 'F1':
            right2()
        elif difference == -2 and frogList[userIndex+2] == ' ' and frogList[userIndex] == 'F2':
            right2()
        elif difference == -2 and frogList[userIndex+2] == ' ' and frogList[userIndex] == 'F3':
            right2()
        else:
            invalid()

        if frogList == ['T1', 'T2', 'T3', ' ', 'F1', 'F2', 'F3']:
            print("YOU'VE WON!")
            break
                            
        userIndex1 = int(input("From: "))
        userIndex = userIndex1-1

def demonstration():
    print("Step 1. [F1, F2, F3, ' ', T1, T2, T3]")
    print("Step 2. [F1, F2, F3, T1, ' ', T2, T3]")
    print("Step 3. [F1, F2, ' ', T1, F3, T2, T3]")
    print("Step 4. [F1, ' ', F2, T1, F3, T2, T3]")
    print("Step 5. [F1, T1, F2, ' ', F3, T2, T3]")
    print("Step 6. [F1, T1, F2, T2, F3, ' ', T3]")
    print("Step 7. [F1, T1, F2, T2, F3, T3, ' ']")
    print("Step 8. [F1, T1, F2, T2, ' ', T3, F3]")
    print("Step 9. [F1, T1, ' ', T2, F2, T3, F3]")
    print("Step 10. [' ', T1, F1, T2, F2, T3, F3]")
    print("Step 11. [T1, ' ', F1, T2, F2, T3, F3]")
    print("Step 12. [T1, T2, F1, ' ', F2, T3, F3]")
    print("Step 13. [T1, T2, F1, T3, F2, ' ', F3]")
    print("Step 14. [T1, T2, F1, T3, ' ', F2, F3]")
    print("Step 15. [T1, T2, ' ', T3, F1, F2, F3]")
    print("Step 16. [T1, T2, T3, ' ', F1, F2, F3]")
    print("")
    print("OR")
    time.sleep(2)
    print("")
    print("Step 1. [F1, F2, F3, ' ', T1, T2, T3]")
    print("Step 2. [F1, F2, ' ', F3, T1, T2, T3]")
    print("Step 3. [F1, F2, T1, F3, ' ', T2, T3]")
    print("Step 4. [F1, F2, T1, F3, T2, ' ', T3]")
    print("Step 5. [F1, F2, T1, ' ', T2, F3, T3]")
    print("Step 6. [F1, ' ', T1, F2, T2, F3, T3]")
    print("Step 7. [' ', F1, T1, F2, T2, F3, T3]")
    print("Step 8. [T1, F1, ' ', F2, T2, F3, T3]")
    print("Step 9. [T1, F1, T2, F2, ' ', 'F3, T3]")
    print("Step 10. [T1, F1, T2, F2, T3, F3, ' ']")
    print("Step 11. [T1, F1, T2, F2, T3, ' ', F3]")
    print("Step 12. [T1, F1, T2, ' ', T3, F2, F3]")
    print("Step 13. [T1, ' ', T2, F1, T3, F2, F3]")
    print("Step 14. [T1, T2, ' ', F1, T3, F2, F3]")
    print("Step 15. [T1, T2, T3, F1, ' ', F2, F3]")
    print("Step 16. [T1, T2, T3, ' ', F1, F2, F3]")
    main()
    
def main():
    global entranceInput
    print(" 1. Play")
    print(" 2. Demonstration")
    print(" 3. Exit")
    entranceInput = int(input("Enter your Option: "))        
    if entranceInput ==1:
        play()
        main()
    elif entranceInput ==2:
        demonstration()
    elif entranceInput ==3:
        print("Leaving")
    else:
        main()

main()
