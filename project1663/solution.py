import numpy as np
import matplotlib.pyplot as plt


def check(node,visited):
    visited = np.array(visited)
    # array_to_check = np.array([1., 2.])
    is_in_list = np.any(np.all(node == visited))
    list(visited)
    return is_in_list


def move_up(node):
    x, y = np.where(node == 0)
    if x != 0:
        node2 = node
        node[x, y] = node2[x-1, y]
        node[x-1, y] = 0
    else: 
        print("Can not move up")
    return node

def move_down(node):
    x, y = np.where(node == 0)
    if x != node.shape[0]-1:
        node2 = node
        node[x, y] = node2[x+1, y]
        node[x+1, y] = 0
    else:
        print("Can not move down")
    return node


def move_left(node):
    x, y = np.where(node == 0)
    if y != 0:
        node2 = node
        node[x, y] = node2[x, y-1]
        node[x, y-1] = 0
    else:
        print("Can not move left")
    return node


def move_right(node):
        x, y = np.where(node == 0)
        if y != node.shape[1]-1:
            node2 = node
            node[x, y] = node2[x, y+1]
            node[x, y+1] = 0
            
        else:
            print("Can not move right")
        return node

def RUN(test,goal,visited):
    while(np.any(test.all() == goal.all())):
        test1 = move_up(test)
        if check(test1,visited)==False:
            visited.append(test1)
            node1 = test1
            print(node1)
            
        test2 = move_down(test)
        if check(test2, visited)==False:
            visited.append(test2)
            node2 = test2
            print(node2)
            # RUN(node2, goal, visited)
            
        test3 = move_left(test)
        if check(test3, visited)==False:
            visited.append(test2)
            node3 = test3
            print(node3)
            # RUN(node3, goal, visited)
            
        test4 = move_right(test)
        if check(test4, visited)==False:
            visited.append(test4)
            node4 = test4
            print(node4)
            # RUN(node4, goal, visited)
    return goal


visited = []
node_i = np.array([8, 7, 6, 5, 4, 3, 2, 1, 0])
node_i = np.reshape(node_i,(3,3))
node_goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
node_goal= np.reshape(node_goal, (3, 3))
test = node_i
test = RUN(node_i,node_goal,visited)
print(test)


