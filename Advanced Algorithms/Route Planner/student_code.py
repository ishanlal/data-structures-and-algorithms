import math
import sys
import heapq

def shortest_path(M,start,goal):
    print("shortest path called")
    shortest_path = []
    # check if goal isn't on a disconnected graph
    if (len(M.roads[goal]) == 1):
        if (len(M.roads[M.roads[goal][0]]) == 1):
            print("Goal intersection is located on a disconnected graph")
            if ( M.roads[M.roads[goal][0]] != start):
                print("can't calculate path because there is no road between the goal and start")
                return shortest_path
    # perform A* search
    path_dict = a_star_search(M, start, goal)
    haha = goal
    out_list = []
    while haha != start:
        out_list.append(haha)
        haha = path_dict[haha]
    out_list.append(haha)
    out_list.reverse()
    return out_list

def point_distance(x, y):
    euclidean = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return euclidean

def a_star_search(M, start, goal):
    # start A* search
    a_star_path = {}
    minHeap = list()
    total = 0
    visited = [False]*(len(list(M.intersections))+1)
    heapq.heappush(minHeap, (0, 0, 0, start, start))
    a_star_path[start] = None
    while len(minHeap) > 0:
        f, g, h, curr, p = heapq.heappop(minHeap)
        #print("f = {}, g = {}, h = {}, curr = {} popped".format(f, g, h, curr))
        if curr == goal:
            #print(a_star_path)
            break
        if visited[curr]:
            continue
        for neighbor in M.roads[curr]:
            if not visited[neighbor]:
                neighbor_curr_dist = point_distance(M.intersections[curr], M.intersections[neighbor])
                heuristic = point_distance(M.intersections[goal], M.intersections[neighbor])
                total = g + neighbor_curr_dist + heuristic
                if neighbor in [v for f, g, h, v, p in minHeap]:
                    for f, g, h, v, p in minHeap:
                        if v==neighbor:
                            if total > f:
                                a_star_path[neighbor] = p
                                #print(a_star_path)
                            else:
                                a_star_path[neighbor] = curr
                else:
                    heapq.heappush(minHeap, (total, g + neighbor_curr_dist, heuristic, neighbor, curr))
                    a_star_path[neighbor] = curr
                heapq.heappush(minHeap, (total, g + neighbor_curr_dist, heuristic, neighbor, curr))
        visited[curr] = True
    return a_star_path
