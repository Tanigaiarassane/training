board = ["-","-","-","-","-","-","-","-","-"]


def print_board():
    k = 0
    for i in range(0, 3):
        print("{}  {} {}".format(board[k], board[k+1], board[k+2]))
        k+=3

def print_location():
    print ("Board Location")
    k = 1
    for i in range(0,3):
        print ("{}  {} {}".format(k, k+1, k+2))
        k+=3
def play_game():
    global board
    player = 1
    i = 0
    while i <= 9:
        i += 1
        print(i)
        if player == 1:
            value = int(input("Player 1 input"))
            if board[value-1] == "-":
                board[value-1] = "X"
                player = 2
                print_board()
            else:
                print ("Invalid input..Enter again")
        if player == 2:
            value = int(input("Player 2 input"))
            if board[value-1] == "-":
                board[value-1] = "O"
                player = 1
                print_board()
            else:
                print ("Invalid input..Enter again")



if __name__ == "__main__":
    print_location()
    print_board()
    play_game()
