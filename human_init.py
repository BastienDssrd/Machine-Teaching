import numpy as np

def human_advice_xy(theta_opt):
    print("What value would to enter ? knowing that the threshold to learn", theta_opt)
    x=float(input("Value :"))
    if( x<0 or x>1 ):
        print("The value must be in [0,1]\n")
        human_advice_xy(theta_opt)
    
    print("The value to be labelized is", x)
    print("\nIs it less or more than the threshold to learn", theta_opt ," ?")
    y=int(input("Less : -1 / More : +1\n"))

    if( abs(int(y))!=1 ):
        print("The value must be -1 or +1\n")
        human_advice_xy(x, theta_opt)

    else:
        return x,y

def print_env(x,y, thresh_l, thresh_r):

    return

def compute_thresh(x, y, thr_l, thr_r):
    #x the new example and y its label
    #thr_l = max value closer to the threshold from the left
    #thr_r = min value closer to the threshold from the right

    #If the x value is into the tresholds interval, we update them
    if( x<thr_r and x>thr_l ):
        if(y==1):
            thr_r=x
        else: 
            thr_l=x

    return [thr_l, thr_r]

def human_init(eps, theta_opt):
 
    nb_it = 0
    #List of xi and yi computed
    list_x, list_y= [], []
    #Initial values of threshold_right and threshold_left
    thr_r, thr_l = 1, 0
    nb_iteration=int(input("For how many iterations would you like to teach ?"))

    while ( (thr_r-thr_l) > eps ):
        if(nb_it>=nb_iteration):
            print("End of the number of iterations provided")
            break
        nb_it += 1
        #Ask the human an example and its classification
        x,y=human_advice_xy(theta_opt)

        #Add the example to the list
        list_x.append(x)
        
        #Compute thresholds
        thr_l, thr_r=compute_thresh(x, y, thr_l, thr_r)
        print("l:", thr_l,"r:", thr_r)

        #Add the label to the list
        list_y.append(y)

    print("<=========Convergence========>")
    print("Final threshold is ", thr_r-thr_l)

    if(nb_it<=nb_iteration):
        print("It took ", nb_iteration, "iterations to converge")
        

if __name__ == "__main__":

    human_init(eps = 0.01, theta_opt =0.5)

