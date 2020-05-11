'''
I split the code into three parts for each task.
'''
try:
    # LISTS USED
    Mid_Temp = []
    Night_Temp = []

    Mid_Total = 0
    Night_Total = 0

    max1 = 0
    max2 = 0

    # TASK 1
    for i in range(2):
        print("Please enter today's Midday Temperature-")
        MT = int(input())  # MT stands for Mid Temp
        Mid_Temp.append(MT)

        print("Please enter today's Night Temperature-")
        NT = int(input())  # NT stands for Night Temp
        Night_Temp.append(NT)

        Mid_Total = Mid_Total + MT
        Night_Total = Night_Total + NT

    # TASK 2
    i = i + 1
    Avg_MT = Mid_Total / i
    AVG_NT = Night_Total / i

    print("\n\nThe average Midday Temperature is-\n", str(Avg_MT), "\n")
    print("The average Night Temperature is-\n", str(AVG_NT))

    # TASK 3
    for mid in Mid_Temp:
        if mid > max1:
            max1 = mid

    for Ni in Night_Temp:
        if Ni > max2:
            max2 = Ni

    print("The maximum Midday Temperature of this week is", str(max1))
    print("The maximum Night Temperature of this week is", str(max2))

except:
    print("An error has occurred. Try running the code again.")
    print("If the error continues, please contact us through the number 972 1234 5678.")
