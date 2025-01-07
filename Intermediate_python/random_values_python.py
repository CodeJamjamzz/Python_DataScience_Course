import numpy as np

np.random.seed(123)
random = np.random.randint(0,2)
    # if no range use np.random.rand() for float

if (random == 1):
    print("heads")
else:
    print("tails")


# Notes
    # # NumPy is imported, seed is set

    # # Starting step
    # step = 50

    # # Roll the dice
    # dice = np.random.randint(1,7)

    # # Finish the control construct
    # if dice <= 2 :
    #     step = step - 1
    # elif dice >= 3 and dice <= 5:
    #     step += 1
    # else :
    #     step = step + np.random.randint(1,7)

    # # Print out dice and step
    # print(str(dice) + " " + str(step))