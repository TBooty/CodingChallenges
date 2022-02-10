def searchword(word, board, row, col, max_rows, max_cols):
    if board[row][col] != word[0]:
        return False

    first_letter = (row, col)
    coordinates_list = []
    for x, y in directions:


        # Add the directions to the pointer based on where we need to go, left, right, etc ..
        row_direction, col_direction = row + x, col + y
        flag = True

        for k in range(1, len(word)):
            if (0 <= row_direction < max_rows and
                    0 <= col_direction < max_cols and
                    word[k] == board[row_direction][col_direction]):

                # Append coordinate to the list
                coordinates_list.append((row_direction, col_direction))

                # Increment the direction based on where we are going
                row_direction += x
                col_direction += y
            else:
                # This direction search failed, clear the coordinate list
                flag = False
                break

        if flag:
            coordinates_list.append(first_letter)
            for index_x, index_y in coordinates_list:
                board[index_x][index_y] = '*'
            return True
        else:
            coordinates_list.clear()
    return False


def find_word(word, board):
    ROWS = len(board)
    COLS = len(board[0])

    for row in range(ROWS):
        for col in range(COLS):
            if searchword(word, board, row, col, ROWS, COLS):
                print(board)


directions = [[-1, 0], [1, 0], [1, 1],
              [1, -1], [-1, -1], [-1, 1],
              [0, 1], [0, -1]]


def main():
    grid = [['t', 'b', 'e', 'a', 'q', 'a'],
            ['d', 'h', 'f', 'f', 'o', 'x'],
            ['d', 'c', 'o', 'f', 'p', 'j'],
            ['d', 'c', 'f', 'm', 'w', 'i'],
            ['d', 'c', 'f', 'a', 'a', 'r'],
            ['s', 'd', 'a', 'e', 'z', 's']]
    find_word('thomas', grid)


if __name__ == '__main__':
    main()
