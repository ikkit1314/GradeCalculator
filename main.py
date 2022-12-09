CG = []
AW= []
want = input("Do you want to calculate? (y/n): ")


def gradeneed():
    currentGrade = WG
    finalWeight = float(input("How much does your final worth?  "))
    finalWeight = finalWeight / 100

    gradeWanted = float(input("What is your percentage is your goal? "))

    otherWorkWeight = 1 - finalWeight

    gradeNeeded = (gradeWanted - (currentGrade * otherWorkWeight)) / finalWeight

    print(f"You need to score at least {gradeNeeded:.2f} on the final exam.")


while True:

        if want.lower() == "n":
            WG = (sum(CG)/sum(AW))
            print(f"Your current grade of final grade is {WG:.2f} %")
            wan1 = input("Do you want to find  grade needed for final? (y/n): ")
            if wan1 == "y":
                gradeneed()
            break
        else:
            assignGrade = float(input("Enter the grade for this  assignment: "))
            assignWeight = float(input("Enter the weight for this assignment: "))
            CG.append(assignGrade * assignWeight)
            AW.append(assignWeight)
        want = input("Do you want to continue calculate? (y/n) ")


