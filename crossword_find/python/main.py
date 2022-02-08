def find_word(word, array):
    word_list = list(word)

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

                    # Check the 8 directions we can go
                    coordinates_list = []
                    if is_word_going_right(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_down_right(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_down(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_down_left(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_left(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_up_left(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_up(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
                    elif is_word_going_up_right(array, word, row, col, coordinates_list):
                        print(replace_letters_with_asterisks(array, coordinates_list))
                        return
    return array


def replace_letters_with_asterisks(array, coordinate_list) -> list:
    for values in coordinate_list:
        first_index = values[0]
        second_index = values[1]
        array[first_index][second_index] = "*"
    return array


def is_word_going_right(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    number_of_cols = len(array[row]) - 1
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if col >= number_of_cols:
            coordinates_list.clear()
            v = False
            break
        i += 1
        col += 1
    return v


def is_word_going_down_right(array, word, row, col, coordinates_list) -> bool:
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
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if col >= number_of_cols or row >= number_of_rows:
            v =False
            coordinates_list.clear()
            break
        i += 1
        row += 1
        col += 1
    return v


def is_word_going_down(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    number_of_rows = len(array) - 1
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break
        # Don't exceed boundary
        if row >= number_of_rows:
            coordinates_list.clear()
            v = False
            break
        i += 1
        row += 1
    return v


def is_word_going_down_left(array, word, row, col, coordinates_list) -> bool:
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
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if col <= 0 or row >= number_of_rows:
            coordinates_list.clear()
            v = False
            break
        i += 1
        row += 1
        col -= 1
    return v


def is_word_going_left(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    number_of_cols = len(array[row]) - 1
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if col <= 0:
            coordinates_list.clear()
            v = False
            break
        i += 1
        col -= 1
    return v


def is_word_going_up_left(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if col <= 0 or row <= 0:
            coordinates_list.clear()
            v = False
            break
        i += 1
        col -= 1
        row -= 1
    return v


def is_word_going_up(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if row <= 0:
            coordinates_list.clear()
            v = False
            break
        i += 1
        row -= 1
    return v


def is_word_going_up_right(array, word, row, col, coordinates_list) -> bool:
    f = 0
    i = 0
    v = True
    number_of_cols = len(array[row]) - 1
    while v:
        value = array[row][col]
        letter_to_check = word[i]
        if letter_to_check == value:
            f += 1
            coordinates_list.append((row, col))
        if f == len(word):
            v = True
            break
        if letter_to_check != value:
            coordinates_list.clear()
            v = False
            break

        # Don't exceed boundary
        if row <= 0 or col >= number_of_cols:
            coordinates_list.clear()
            v = False
            break
        i += 1
        row -= 1
        col += 1
    return v


def main():
    grid = [['d', 'e', 'e', 'a'],
            ['d', 'c', 'f', 'f'],
            ['a', 'd', 'a', 'e']]
    find_word('ace', grid)


if __name__ == '__main__':
    main()
