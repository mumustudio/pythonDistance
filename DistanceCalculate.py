# -*- coding: utf-8 -*
import math
import os

class vector:
    def __init__(self, index, posx, posy):
        self.index = index
        self.posx = posx
        self.posy = posy

    def toString(self):
        print "index:"+str(self.index)+" x:"+ str(self.posx)+",y:"+ str(self.posy)


def search_distance(pos_index1, pos_index2):
    print "求以下兩點距離:"
    vectors[pos_index1-1].toString()
    vectors[pos_index2-1].toString()
    x_dis = float(vectors[pos_index1-1].posx) - float(vectors[pos_index2-1].posx)
    y_dis = float(vectors[pos_index1-1].posy) - float(vectors[pos_index2-1].posy)
    distance = math.sqrt((x_dis**2)+(y_dis**2))
    return distance


if __name__ == "__main__":
    vectors = []
    index = 0
    # read info from sample txt and save to object
    print os.getcwd()
    with open(os.getcwd()+'\sample.txt', 'r') as f:
        for line in f:
            index = index + 1
            vector_info = vector(index, line.split()[1], line.split()[2])
            vectors.append(vector_info)
            print "index:"+str(index)
            print "座標:"+str(vector_info.posx)+", "+str(vector_info.posy)
    f.close()
    print index
    # creat list with 2 dimensions
    vector_distance_result = [[1]*index for i in range(index)]
    # calculate all vectors distance and save in list
    for i in range(1, index):
        for j in range(1, index):
            vector_distance_result[i][j] = search_distance(i, j)
            print "點:"+str(i)+"到點:"+str(j)+"距離:"+str(vector_distance_result[i][j])

    #search result list by user input
    search_index = "none"
    while search_index is not "e":
        search_index = raw_input("請輸入想求的兩點編號 1~"+str(index)+"(空白間隔 e 結束): ")
        if search_index == "e":
            break
        vector1 = int(search_index.split()[0])
        vector2 = int(search_index.split()[1])
        print "兩點距離為:"+str(vector_distance_result[vector1][vector2])


