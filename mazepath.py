def find_paths(maze, path="", row=0, col=0):
    n = len(maze)
    m = len(maze[0])
    if row >= n or col >= m or maze[row][col] == 0:
        return
    if row == n-1 and col == m-1:
        print(path)
        return
    find_paths(maze, path + "R", row, col + 1)
    find_paths(maze, path + "D", row + 1, col) 
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
maze=[]
for i in range(n):
  maze.append([1] * m)
print("All possible paths:")
find_paths(maze)
