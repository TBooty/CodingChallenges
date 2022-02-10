def search(word, board):
    # Get max rows and cols in a tuple
    ROWS, COLS, = len(board), len(board[0])

    # Keep track of visited nodes
    path = set()

    def dfs(row, col, i):
        # Check if we reached the end of the word on the i incrementer
        if i == len(word):
            return True

        # Assign to variable for readability

        # If we are below the bounds of the board
        # If we are outside the bounds of the max board
        # If the character doesn't match the row we are looking at
        # If we already visited the node in the set
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or word[i] \
                != board[row][col] or (row, col) in path:
            return False

        # Found a character that matches, add it to the visited node list
        path.add((row, col))

        # Since we found a matching character recurse each direction possible
        result = (dfs(row + 1, col, i + 1)) # ↑ ← go up left

        # If one of the searches came back with true remove it from visited list and return
        path.remove((row, col))
        return result

    # Loop through each row
    for rows in range(ROWS):
        # Loop through each column
        for cols in range(COLS):
            # Run search on current pointer
            if dfs(rows, cols, 0):
                # We found a match
                return True

def main():
    grid = [['d', 'a', 'e', 'a'],
            ['d', 'c', 'f', 'f'],
            ['a', 'd', 'a', 'e']]
    search('ace', grid)
    print(grid)


if __name__ == '__main__':
    main()
