import os
import numpy as np
from flask import abort


class RoomFill:

    def __init__(self, filename=None):
        """Constructor
        The filename must be on data dir
        if file name is none, take default room.txt
        :params: filename: text
        """
        if not filename:
            filename = "room.txt"
        if not os.path.exists(f"data/{filename}"):
            abort(404)
        with open(f"data/{filename}", "r") as f:
            l = [line.split() for line in f]
        self.lines = [list( map(int,i) ) for i in l] 

    def bulbs(self):
        """
        Fill room whit bulbs
        0 = darkness
        1 = wall
        2 = light from a bulb
        3 = bulb
        :return: res: array: fillet foom whit light
        """
        arr = np.array(self.lines)        
        res = arr.copy()
        rows = arr.shape[0]
        cols = arr.shape[1]        
        for x in range(0, rows):
            for y in range(0, cols):                
                if res[x, y] != 2 and res[x, y] == 0:
                    res[x, y] = 3                    
                    for ix in range(x + 1, rows):
                        if res[ix, y] == 1:                            
                            break
                        if res[ix, y] != 1 and res[ix, y] != 3:                            
                            res[ix, y] = 2
                    for iy in range(y + 1, cols):
                        if res[x, iy] == 1:                            
                            break
                        if res[x, iy] != 1 and res[x, iy] != 3:                            
                            res[x, iy] = 2
        return res

