import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def grid_dim(a):
    return np.zeros((a,a))

def filled_grid(grid):
    x = [[1,1,0,0,0,0,0],
        [1,1,1,0,0,0,0],
        [0,0,1,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,0,0,0],
        [1,1,1,0,0,0,0],
        [1,1,0,0,0,0,0]]
    grid[5:12, 10:17] = x   

    return grid

def update(grid,size):
    for i in range(size):
        for j in range(size):
            n = 0
            if i==0 and j==0:
                n = (grid[i,j+1] + grid[i+1,j+1] + grid[i+1,j])
            elif i==100 and j==100:
                n = (grid[i-1,j] + grid[i-1,j-1] + grid[i,j-1])
            elif i==0 and j==100:
                n = 
            elif i==100 and j==0:
            elif i==0 and (j!=0 or j!=100):
            elif i==100 and (j!=0 or j!=100):
            elif (i!=0 or i!=100) and j==0:
            elif (i!=0 or i!=100) and j==100:
            else:



    return grid2


def main():
    alive = 1
    dead = 0

    grid = grid_dim(100)
    grid2 = filled_grid(grid)
    

    plt.imshow(grid2,cmap='binary')
    plt.show()

if __name__ == '__main__':
    main()


