from computer_init import *
from human_init import *

def mixed_init(eps, theta_opt, nb_td):

    list_x, list_y = [], []
    thr_r, thr_l = 1, 0
    nb_it = nb_td
    print("The number of Human initiated iterations is :", nb_td)
    print("You can always stop if you don't want to keep teaching")

    for i in range(nb_td):

        if int(input("Wanna stop ? Please enter 1 / To continue enter 0\n")):
            break
        else:
            print("<====== Human Initiated ======>")
            #Ask the human for an example and its classification
            x,y=human_advice_xy(theta_opt)
            #Add the example to the list
            list_x.append(x)
            #Add the label to the list
            list_y.append(y)
            
            #Compute thresholds
            thr_l, thr_r=compute_thresh(x, y, thr_l, thr_r)
            #print("l:", thr_l,"r:", thr_r)

    #Pick a new value for x
    x=pick_new_val(thr_l, thr_r, mode=0)
    
    while ( (thr_r-thr_l) > eps ):

        nb_it+=1
        #Add the example to the list
        list_x.append(x)
        #Ask the human to classify the example
        y=human_advice(x, theta_opt)
        #Add the label to the list
        list_y.append(y)

        thr_l, thr_r=compute_thresh(x, y, thr_l, thr_r) 
        # print("l:", thr_l,"r:", thr_r)
        
        #Pick a new value for x
        x=pick_new_val(thr_l, thr_r, mode=0)
        

    print("<========= Convergence ========>")
    print("Final threshold is ", thr_r-thr_l)
    print("It took ", nb_it, "iterations to converge")

if __name__ == "__main__":

    mixed_init(eps = 0.01, theta_opt =0.5, nb_td = 2)

