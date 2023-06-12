import string
import time
import datetime  #gives time in hours

start_time = time.time() #keeps the time the program began to run

power = input("Does your computer have power? (yes/no):") 

if power == "yes":
    print("Seek other help")

    end_time = time.time() #tells currrent time
    print(datetime.timedelta(seconds = end_time - start_time)) #gives the time it took to run the program

elif power == "no":
    plugged = input("Is it plugged in? (yes/no):")

    if plugged == "no":
        print("Plug it in")

        end_time = time.time()
        print(datetime.timedelta(seconds = end_time - start_time))

    elif plugged == "yes":
        switch = input("Is the switch on? (yes/no):")

        if switch == "no":
            print("Turn switch on")

            end_time = time.time()
            print(datetime.timedelta(seconds = end_time - start_time))


        elif switch == "yes":
            fuse = input("Is the fuse ok? (yes/no):")

            if fuse == "no":
                print("Check fuse")

                end_time = time.time()
                print(datetime.timedelta(seconds = end_time - start_time))

            elif switch == "yes":
                print("Seek other help")

                end_time = time.time()
                print(datetime.timedelta(seconds = end_time - start_time))
