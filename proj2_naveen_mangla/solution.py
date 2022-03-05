
from tkinter.filedialog import Open
from joblib import parallel_backend
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
arr = np.ones((250, 400))*(np.exp(50))

pts = np.array([[36, 185], [115, 210], [80, 180], [105,100]], np.int32)

pts2 = np.array([[200, 100+70*np.tan(np.pi/6)], [235, 100+35/(2*np.cos(np.pi/6))],
                [235, 100-17.5/np.cos(np.pi/6)], [200, 100-70*np.tan(np.pi/6)],
                [165, 100-17.5/np.cos(np.pi/6)], [165, 100+17.5/np.cos(np.pi/6)]], np.int32)

cv2.circle(arr, (300, 185), 40, -1, -1)

pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(arr, [pts], -1)
cv2.fillPoly(arr, [pts2], -1)

###############################################

display = np.zeros((arr.shape[0],arr.shape[1],3))
display[:,:,2] = arr.copy()
display[:,:,2][arr == -1] = 255   #Displaying Obstacles
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
    if valid(start, closedList, arr) and valid(goal, closedList, arr) and start != goal:
        flag = True
    else:
        print("You have entered an invalid value, try again\n")


##### Change Your Path here #################
#############################################
path = "/home/naveen/ENPM663/project2/"  ####
#############################################

OpenList[start] = 0
arr[start] = 0
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
        temp = move(arr, node, dir)
        if valid(temp, closedList, arr):
            if temp not in OpenList or arr[temp]>np.exp(10):
                parent[temp] = node
                arr[temp] = arr[node]+cst
                OpenList[temp] = arr[temp]
            elif arr[temp]>arr[node]+cst:
                parent[temp] = node
                arr[temp]=arr[node]+cst
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

    
