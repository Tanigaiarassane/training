global board
board = ["-","-","-","-","-","-","-","-","-"]

def print_board():
    k = 0
    for count in range(0, 3):
        print("{}  {} {}".format(board[k], board[k+1], board[k+2]))
        k+=3

def print_location():
    print ("Board Location")
    k = 1
    for i in range(0,3):
        print ("{}  {} {}".format(k, k+1, k+2))
        k+=3
def play_game():
    player = 1
    i = 0
    while i < 9:

        print(i)
        if player == 1:
            print_location()
            value = int(input("Player 1 input"))
            if board[value-1] == "-":
                board[value-1] = "X"
                player = 2
                i += 1
                print("Current board {}".format(board))
                print ("*"*20)
                print_board()
            else:
                print ("Invalid input..Enter again")
        elif player == 2:
            print_location()
            value = int(input("Player 2 input"))
            if board[value-1] == "-":
                board[value-1] = "O"
                player = 1
                i += 1
                print("Current board {}".format(board))
                print_board()
            else:
                print ("Invalid input..Enter again")

        if check_result('X'):
            print ("Player 1 won the game")
            return
        if check_result('O'):
            print ("Player 1 won the game")
            return

def check_result(symbol):
    if board[0] == board[1] == board[2] == symbol or \
       board[3] == board[4] == board[5] == symbol or \
       board[6] == board[7] == board[8] == symbol or \
       board[0] == board[3] == board[6] == symbol or \
       board[1] == board[4] == board[7] == symbol or \
       board[2] == board[5] == board[8] == symbol or \
       board[0] == board[4] == board[8] == symbol or \
       board[2] == board[4] == board[6] == symbol:
        return 1

if __name__ == "__main__":
    print_location()
    print_board()
    play_game()
