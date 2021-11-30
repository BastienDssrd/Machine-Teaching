import numpy as np
from computer_init import *
from human_init import *
from mixed_init import *

""" 1: Computer Initated
    2: Human Initated
    3: Mixed Initated """

if __name__ == "__main__":
    mode=int(input("What teaching methode do you want to launch ?\nModes:\n1: Computer Initated\n2: Human Initated\n3: Mixed Initated \n"))

    if(mode == 1):
        computer_init(eps = 0.1, theta_opt =0.5)
    elif (mode == 2):
        human_init(eps = 0.01, theta_opt =0.5)
    elif (mode == 3):
        mixed_init(eps = 0.01, theta_opt =0.5, nb_td = 5)
    else:
        print("The entry is incorrect, it must be [1,2 or 3]")