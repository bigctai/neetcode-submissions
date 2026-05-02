class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = {}
        for i, rows in enumerate(grid):
            for j, land in enumerate(rows):
                if str(i) + str(j) in visited or grid[i][j] != "1":
                    continue
                stack = [(i, j)]
                while stack:
                    i_new, j_new = stack.pop()
                    visited[str(i_new) + str(j_new)] = True
                    if grid[i_new][j_new] == "1":
                        added_coords = [(i_new, j_new + 1), (i_new+1, j_new), (i_new, j_new-1), (i_new-1, j_new)]
                        cleaned_coords = []
                        for coord in added_coords:
                            if str(coord[0]) + str(coord[1]) not in visited and 0<=coord[0]<= len(grid)-1 and 0<=coord[1]<=len(rows)-1:
                                cleaned_coords.append(coord)
                        stack.extend(cleaned_coords)
                count += 1
                    
        return count

                    