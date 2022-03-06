

import numpy as np
import cv2
import matplotlib.pyplot as plt
import heapq as hq

def valid(node, list, array):
    pad = 5 ##### Padding of 5mm on boundering
    if  node not in list and 0 +pad <= node[0] < 250-pad and 0 +pad <= node[1] < 400-pad and array[node] > 0:
        return True
    else:
        return False


def Reverse(lst):
    return [ele for ele in reversed(lst)]

def move(array, node, dir):
    x, y = node
    if dir == 0:
        y -= 1
    elif dir == 1:
        x -= 1
        y -= 1
    elif dir == 2:
        x -= 1
    elif dir == 3:
        x -= 1
        y += 1
    elif dir == 4:
        y += 1
    elif dir == 5:
        x += 1
        y += 1
    elif dir == 6:
        x += 1
    elif dir == 7:
        x += 1
        y -= 1
    return(x, y)

############ Making a Problem Array ######


def make_line(p1, p2):
    if p1[0]-p2[0] == 0:
        m = (p1[1]-p2[1])/0.00000001
    else:
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
    c = -1*p1[0]*m + p1[1]
    return m, c


prob = np.ones((250, 400))*np.exp(50)

pad = 5

pp1 = (36, 185)
pp2 = (115, 210)
pp3 = (80, 180)
pp4 = (105, 100)
ph = [(200, 100+70*np.tan(np.pi/6)), (235, 100+35/(2*np.cos(np.pi/6))),
    (235, 100-17.5/np.cos(np.pi/6)), (200, 100-70*np.tan(np.pi/6)),
    (165, 100-17.5/np.cos(np.pi/6)), (165, 100+17.5/np.cos(np.pi/6))]
for y in range(250):
    for x in range(400):
        m1, c1 = make_line(pp1, pp2)
        m2, c2 = make_line(pp2, pp3)
        m3, c3 = make_line(pp3, pp4)
        m4, c4 = make_line(pp4, pp1)
        if (y-m1*x < c1 and y-m4*x > c4) and (y-m2*x > c2 or y-m3*x < c3):
            prob[y, x] = 1
        mh1, ch1 = make_line(ph[0], ph[1])
        mh2, ch2 = make_line(ph[1], ph[2])
        mh3, ch3 = make_line(ph[2], ph[3])
        mh4, ch4 = make_line(ph[3], ph[4])
        mh5, ch5 = make_line(ph[4], ph[5])
        mh6, ch6 = make_line(ph[5], ph[0])
        if y-mh1*x < ch1 and y-mh2*x > ch2 and y-mh3*x > ch3 and y-mh4*x > ch4 and y-mh5*x > ch5 and y-mh6*x < ch6:
            prob[y, x] = 1

        xc, yc = 300, 185

        if np.sqrt((x-xc)**2 + (y-yc)**2) <= 40:
            prob[y, x] = 1
prob[prob==1]=-1

###############################################

display = np.zeros((prob.shape[0],prob.shape[1],3))
display[:,:,2] = prob.copy()
display[:,:,2][prob == -1] = 255   #Displaying Obstacles
display = display.astype(np.uint8)
flag = False


OpenList = {}

closedList = []

parent = {}

########### Getting User Input ####################
while flag == False:
    xs = int(input("Enter X value of Start node  "))
    ys = int(input("Enter Y value of Start node  "))
    xg = int(input("Enter X value of goal node  "))
    yg = int(input("Enter Y value of goal node  "))
    start = (xs,ys)
    goal = (xg,yg)
    if valid(start, closedList, prob) and valid(goal, closedList, prob) and start != goal:
        flag = True
    else:
        print("You have entered an invalid value, try again\n")


##### Change Your Path here #################
#############################################
path = "/home/naveen/ENPM663/proj2_naveen_mangla/"
#############################################

OpenList[start] = 0
prob[start] = 0
closedList.append(start)
node = start
out = cv2.VideoWriter(path + 'project.avi',cv2.VideoWriter_fourcc(*'DIVX'),400,(display.shape[1], display.shape[0]))
while node != goal:
    OpenList = dict(sorted(OpenList.items(), key=lambda item: item[1]))
    node = list(OpenList.keys())[0]
    OpenList.pop(node)
    closedList.append(node)
    cst = 0
    for dir in range(8):
        if dir % 2 == 0:
            cst = 1
        else:
            cst = 1.4
        temp = move(prob, node, dir)
        if valid(temp, closedList, prob):
            if temp not in OpenList or prob[temp]>np.exp(10):
                parent[temp] = node
                prob[temp] = prob[node]+cst
                OpenList[temp] = prob[temp]
            elif prob[temp]>prob[node]+cst:
                parent[temp] = node
                prob[temp]=prob[node]+cst
        else:
            continue
        
    display[:,:,0][node] = 255
    cv2.imshow("Visualise!", np.flipud(display))
    cv2.waitKey(1)
    out.write(np.flipud(display))

node = goal
path = []
while start not in path:    
    node  = parent.pop(node)
    path.append(node)
print("Total nodes travelled are", len(path))
path = Reverse(path)
for n in path:
    display[:,:,1][n] = 255
    out.write(np.flipud(display))
cv2.imshow("Visualise!", np.flipud(display))
cv2.waitKey(0)
out.release()

    
