def find_word(word, array):
    word_list = list(word)
    directions = ["right", "down right", "down" "down left", "left", "up left", "up", "up right"]
    # Iterate the letters for the word to find
    for i in range(len(word_list)):

        # Assign to variable to readability
        word_letter_to_check = word_list[i]

        # Iterate the row
        for row in range(len(array)):

            # Iterate the columns in that row
            for col in range(len(array[row])):

                # Assign to variable to readability
                array_letter_to_check = array[row][col]

                # Check if any letters in the row match what we are looking for as a start
                if word_letter_to_check == array_letter_to_check:

                    # Next check the 8 possible directions
                    for direction in directions:
                        coordinates_list = []
                        result = is_word_going_direction(direction, array, word, row, col, coordinates_list)\

                        # If we found a match print it and return
                        if result:
                            print(replace_letters_with_asterisks(array, coordinates_list))
                            return
    return array


def replace_letters_with_asterisks(array, coordinate_list) -> list:
    for values in coordinate_list:
        first_index = values[0]
        second_index = values[1]
        array[first_index][second_index] = "*"
    return array


def is_word_going_direction(direction, array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    number_of_cols = len(array[row]) - 1
    number_of_rows = len(array) - 1
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            return True
        if letter_to_check != value:
            coordinates_list.clear()
            return False
        if direction == "right":
            if is_within_boundary(row, col, number_of_rows, number_of_cols, direction):
                col += 1
        elif direction == "down right":
            row += 1
            col += 1
        elif direction == "down":
            row += 1
        elif direction == "down left":
            row += 1
            col -= 1
        elif direction == "left":
            col -= 1
        elif direction == "up left":
            col -= 1
            row -= 1
        elif direction == "up":
            row -= 1
            pass
        elif direction == "up right":
            row -= 1
            col += 1
        i += 1


def is_within_boundary(row, col, max_rows, max_cols, direction) -> bool:
    if direction == "right":
        if col >= max_cols:
            return False
    elif direction == "down right":
        if col >= max_cols or row >= max_rows:
            return False
    elif direction == "down":
        if row >= max_rows:
            return  False
    elif direction == "down left":
        if col <= 0 or row >= max_rows:
            return False
    elif direction == "left":
        if col <= 0:
            return False
    elif direction == "up left":
        if col <= 0 or row <= 0:
            return False
    elif direction == "up":
        if row <= 0:
            return False
    elif direction == "up right":
        if row <= 0 or col >= max_rows:
            return False
    return True


def main():
    grid = [['a', 'c', 'e', 'a'],
            ['d', 'c', 'f', 'f'],
            ['a', 'd', 'a', 'e']]
    find_word('ace', grid)


if __name__ == '__main__':
    main()
