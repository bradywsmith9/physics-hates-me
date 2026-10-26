import random
import math
g = 9.81
gameLoop = True
output = [0,0,0,0,0,0,0] #[0mass, 1height, 2time, 3speed_final, 4force, 5kill?, 6accel]
#subject the user to an infinite loop of physics
def kill_victorian_child(output):
    if output[0]*output[6] >= 100.0:
        output[5] = True
    else:
        output[5] = False


#drops a ball of rand mass from a rand height
def ball_drop(): 
    output[1] = random.randint(1, 10000000000000)
    output[0] = random.randint(1, 10000000000000)
    output[3] = 2*g*output[2]
    output[2] = output[3]/g
    output[4] = output[6] * output[0]
    kill_victorian_child(output)
    return output

def ball_ramp(rampH, theta):
    rampH = random.randint(0,1000000000)
    theta = random.randint(2, 90)
    output[0] = random.randint(1, 100000)
    output[3] = 2*g*math.sin(theta)*rampH 
    output[6] = g*math.sin(theta)
    output[2] = output[3]/output[6]
    output[4] = output[0] * output[6] 
    output[1] = rampH/math.sin(theta)
    kill_victorian_child(output)
    return output

def printr(output):
    print("The ball strikes the ground with a velocity of", output[3], 'm/s, \nfrom a height of', output[1], 'meters,\nwith a mass of', output[0], 'kilograms.')
    if output[5]:
        print("This generates enough force to kill a victorian child.")
    else:
        print("This is not enough force to kill a victorian child.")

def hell_loop(): #game loop technically
    counter = 0 
    print("Welcome to eternal pain and suffering. \n You will be endlessly forced to do physics problems.")
    while gameLoop:
        output = [0,0,0,0,0,0]
        answer = input("Please enter the physics problem you would like to painfully experience. r for Ramp or d for Drop. \n")
        if answer == 'r':
            printr(ball_ramp(0,0))
        elif answer == 'd':
            printr(ball_drop())
        output.clear()
        if counter == 100:
            print("You have suffered enough.")

hell_loop()