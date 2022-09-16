def display(position_map):
    board = (f"""
            {position_map[9]} | {position_map[8]} | {position_map[7]}
            ----|-----|----
            {position_map[4]} | {position_map[5]} | {position_map[6]}
            ----|-----|----
            {position_map[1]} | {position_map[2]} | {position_map[3]}
        """)
    print(board)


def get_position(user_x_or_o, position_map):
    valid_position = False
    position = -1
    while not valid_position:
        position = input(f"User {user_x_or_o}: Please enter empty position on board (1-9): ")
        if not position.isdigit() or int(position) not in range(1, 10):
            print("Invalid input. Please enter empty position in 1 to 9.")
        elif position_map[int(position)].strip() != '':
            print("Position already filled. Please enter empty position in 1 to 9.")
        else:
            valid_position = True
    else:
        position_map[int(position)] = f" {user_x_or_o} "
    return position_map


def start_game(position_map):
    game_on = True
    while game_on:
        position_map = get_position('X', position_map)
        display(position_map)
        position_map = get_position('O', position_map)
        display(position_map)


if __name__ == '__main__':
    one = '   '
    two = '   '
    three = '   '
    four = '   '
    five = '   '
    six = '   '
    seven = '   '
    eight = '   '
    nine = '   '

    position_map = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}

    print("\nEnjoy Tic - Tac - Toe! :)")
    display(position_map)
    start_game(position_map)
