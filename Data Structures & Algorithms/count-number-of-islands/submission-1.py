class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = {}
        for i, rows in enumerate(grid):
            for j, land in enumerate(rows):
                if str(str(i) + str(j)) in visited:
                    continue
                if grid[i][j] != "1":
                    continue
                stack = [(i, j)]
                while stack:
                    i_new, j_new = stack.pop()
                    if i_new < 0 or j_new < 0:
                        continue
                    visited[str(i_new) + str(j_new)] = True
                    print(i_new)
                    print(j_new)
                    if grid[i_new][j_new] == "1":
                        added_coords = [(i_new, j_new + 1), (i_new+1, j_new), (i_new, j_new-1), (i_new-1, j_new)]
                        cleaned_coords = []
                        for coord in added_coords:
                            print(coord)
                            if str(coord[0]) + str(coord[1]) not in visited and coord[0] >= 0 and coord[1] >= 0 and coord[0] <= len(grid) - 1 and coord[1] <= len(rows)-1:
                                print("added:", str(coord[0]) + str(coord[1]))
                                cleaned_coords.append(coord)
                        stack.extend(cleaned_coords)
                print("island found")
                count += 1
                    
        return count

                    