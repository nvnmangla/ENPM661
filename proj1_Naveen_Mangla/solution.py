
import ast
import numpy as np


def Reverse(lst):
    return [ele for ele in reversed(lst)]


def repair(node):
    return np.reshape(np.array(node), 9).tolist()


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def move(node, direction):
    node2 = node.copy()
    i = node2.index(0)
    if direction == 3 and i not in [0, 1, 2]:
        return swapPositions(node2, i, i-3)

    if direction == 2 and i not in [2, 5, 8]:
        return swapPositions(node2, i, i+1)

    if direction == 1 and i not in [6, 7, 8]:
        return swapPositions(node2, i, i+3)

    if direction == 0 and i not in [0, 3, 6]:
        return swapPositions(node2, i, i-1)

    else:
        return node.copy()

def generate_path(index, visited, parents):
    print("Backtracking------------")
    path = [ast.literal_eval(visited[len(visited)-1])]
    while index != 0:
        node = ast.literal_eval(visited[index])
        path.append(node)
        index = parents[index]
    path.append(ast.literal_eval(visited[0]))
    path2 = Reverse(path)

    return path2


def RUN(data, goal, visited):
    print("Running----------------")
    parent_i = [0]
    while str(goal) not in data:
        node = data.pop(0)
        nodei = ast.literal_eval(node)
        for d in range(4):
            if str(goal) not in visited:
                test = move(nodei, d).copy()
                if str(test) not in visited:
                    parent_i.append(visited.index(node))
                    visited.append(str(test))
                    data.append(str(test))
    else:
        print("Goal Reached !!!")
    return parent_i


def BFS(start,goal):
    # Change this Location to your own directory :)
    ##################
    location = "/home/naveen/ENPM663/"
    ##################

    node_i = repair(start)
    node_goal = repair(goal)
    data = [str(node_i)]
    visited = [str(node_i)]
    parents = RUN(data, node_goal, visited)
    index = parents[len(parents)-1]
    path = generate_path(index, visited, parents)

    textfile = open(location+"proj1_Naveen_Mangla/nodePath.txt", "w")
    print("Writing Path File")
    for element in path:
        for i in element:
            textfile.write(str(i)+' ')
        textfile.write('\n')
    textfile.close()

    textfile = open(location+"proj1_Naveen_Mangla/NodesInfo.txt", "w")
    print("Writing Node Info")
    textfile.write('Node_index  Patrent_index  cost')
    textfile.write('\n')
    for i in range(len(visited)):
        textfile.write(str(i)+'             ' +
                       str(parents[i])+'              '+str(0))
        textfile.write('\n')
    textfile.close()
    print("All Done!")

    textfile = open(location+"proj1_Naveen_Mangla/Nodes.txt", "w")
    print("Writing Node File")
    for element in visited:
        temp = ast.literal_eval(element)
        for i in temp:
            textfile.write(str(i)+' ')
        textfile.write('\n')
    textfile.close()


# Change these start and goal nodes
##############
node_start = [1, 4, 7], [5, 0, 8], [2, 3, 6]
node_goal1 = [1, 4, 7], [2, 5, 8], [3, 6, 0]
node_goal2 = [0, 1, 4], [2, 5, 7], [3, 6, 8]

##############

BFS(node_start,node_goal1)
print("\nFor second goal\n")
BFS(node_start, node_goal2)
