state = input("Are you ill or not ill?(Write in small caps as 'ill' or 'not ill')")
present = int(input("What percentage of the year have you been present?(Write number only)")) 
if state == "not ill":
    if present >= 75:
        print("You may enter the exam")
    else:
        print("You cannot enter the exam.")
elif state == "ill":
    print("You cannot enter the exam")
