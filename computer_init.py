import numpy as np

def human_advice(x, theta_opt):
    print("The value to be labelized is", x, "\nIs it less or more than the threshold to learn", theta_opt ," ?")
    y=int(input("Less : -1 / More : +1\n"))

    if( abs(int(y))!=1 ):
        print("The value must be -1 or +1\n")
        human_advice(x, theta_opt)
    else:
        return y

def pick_new_val(thr_l, thr_r, mode):
    if mode == 0:
        #Random val bewteen thresholds
        X=np.random.uniform(thr_l, thr_r, 1)[0]

    if mode == 1:
        #Dichotomie
        X=(thr_r+thr_l)/2

    return X

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

def computer_init(eps, theta_opt):
 
    nb_iteration = 0
    #List of xi and yi computed
    list_x, list_y= [], []
    #Initial values of threshold_right and threshold_left
    thr_r, thr_l, thresh = 1, 0, 0
    #Initialize the first x to test
    x = np.random.rand(1)[0]
 
    while ( (thr_r-thr_l) > eps ):

        nb_iteration += 1
        #Add the example to the list
        list_x.append(x)
        #Ask the human to classify the example
        y=human_advice(x, theta_opt)

        thr_l, thr_r=compute_thresh(x, y, thr_l, thr_r)
        thresh = thr_r-thr_l

        # print("l:", thr_l,"r:", thr_r)
        #Add the label to the list
        list_y.append(y)
        #Pick a new value for x
        x=pick_new_val(thr_l, thr_r, mode=1)

    print("<=========Convergence========>")
    print("Final threshold is ", thr_r-thr_l)
    print("It took ", nb_iteration, "iterations to converge")
        

if __name__ == "__main__":
    computer_init(eps = 0.1, theta_opt =0.5)
