from board_class import Board
from difficulty import difficulty
from choose_xo import chooseXO
from ai_turn import AI_turn_easy, AI_turn_hard, AI_turn_impossible
from user_turn import p1_turn
from check_win import check_win
from clearScreen import clearScreen
import time

def p1vsai():
    clearScreen()

    diff = difficulty()
    time.sleep(1.5)

    board = Board()
    turns_taken = 0
    possible_nums = [str(i) for i in range (1,10)]
    last_move, AI_XO, p1_XO = chooseXO()

    while turns_taken < 9:
        clearScreen()
        board.print_board()

        if last_move == "p1":
            print("Bot's turn")
            time.sleep(1.5)
            if diff == "E":
                possible_nums = AI_turn_easy(board, possible_nums, AI_XO, p1_XO)
            elif diff == "H":
                possible_nums = AI_turn_hard(board, possible_nums, AI_XO, p1_XO)
            elif diff == "I":
                possible_nums = AI_turn_impossible(board, possible_nums, AI_XO, p1_XO)
            last_move = "AI"

        elif last_move == "AI":
            print("Player 1's turn")
            possible_nums = p1_turn(board, possible_nums, p1_XO)
            last_move = "p1"

        win = check_win(board, turns_taken)
        if win == None:
            pass
        else:
            break

        turns_taken += 1

    clearScreen()
    board.print_board()

    if win == AI_XO:
        print("Bot wins. You lose :(")
        time.sleep(1.5)
    elif win == p1_XO:
        print("You win :) Congratulations!")
        time.sleep(1.5)
    else:
        print("It was a draw")
        time.sleep(1.5)

    time.sleep(1.5)
