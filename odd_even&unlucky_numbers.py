for number in range(1,21):
    if number == 4:
        print(str(number)+": unlucky")

    elif number == 13:
        print(str(number)+": unlucky")
    elif number%2 == 0 and number != 4:
        print(str(number)+": even")

    elif number%2 ==1 and number !=13:
        print(str(number)+": odd")