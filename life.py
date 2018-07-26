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

def update(frameNum, img, grid, size):

    newGrid = np.zeros((size,size))

    for i in range(size):
        for j in range(size):
            n = 0
            if i==0 and j==0:
                n = (grid[i,j+1] + grid[i+1,j+1] + grid[i+1,j])
            elif i==(size-1) and j==(size-1):
                n = (grid[i-1,j] + grid[i-1,j-1] + grid[i,j-1])
            elif i==0 and j==(size-1):
                n = (grid[i,j-1] + grid[i+1,j-1] + grid[i+1,j])
            elif i==(size-1) and j==0:
                n = (grid[i-1,j] + grid[i-1,j+1] + grid[i,j+1])
            elif i==0 and (j!=0 and j!=(size-1)):
                n = (grid[i,j-1] + grid[i+1,j-1] + grid[i+1,j] + grid[i+1,j+1] + grid[i,j+1])
            elif i==(size-1) and (j!=0 and j!=(size-1)):
                n = (grid[i,j-1] + grid[i-1,j-1] + grid[i-1,j] + grid[i-1,j+1] + grid[i,j+1])
            elif (i!=0 and i!=(size-1)) and j==0:
                n = (grid[i-1,j] + grid[i-1,j+1] + grid[i,j+1] + grid[i+1,j+1] + grid[i+1,j]) 
            elif (i!=0 and i!=(size-1)) and j==(size-1):
                n = (grid[i-1,j] + grid[i-1,j-1] + grid[i,j-1] + grid[i+1,j-1] + grid[i+1,j])
            else:
                n = (grid[i,j-1] + grid[i,j+1] + grid[i-1,j] + grid[i+1,j] + grid[i-1,j-1] + grid[i-1,j+1] + grid[i+1,j-1] + grid[i+1,j+1])
  
            if grid[i,j]==1:
                if (n<2) or (n>3):
                   newGrid[i,j] = 0
                else:
                   newGrid[i,j] = 1
            else:
                if n==3:
                   newGrid[i,j] = 1

    img.set_data(newGrid)
    grid[:]=newGrid[:]
    return img


def main():
  

    N = 100
    updateInterval =500

    grid = grid_dim(100)
    grid2 = filled_grid(grid)

    #Animation
    fig,ax = plt.subplots()
    img = ax.imshow(grid2)
    anim = animation.FuncAnimation(fig,update,fargs=(img, grid2, N, ),interval=updateInterval)
    plt.show()

if __name__ == '__main__':
    main()


