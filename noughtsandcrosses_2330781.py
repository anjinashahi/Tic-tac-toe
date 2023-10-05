'''
    this program is  a tic tac toe game.
'''
import random
import os.path
import json
random.seed()

def draw_board(board):
    '''
        It develops a board containing elements(numbers)
    '''
    # develop code to draw the board
    divider = " ----------- "
    print(divider) #prints a dotted line to separate rows.
    for element in board:
        print(f"| {element[0]} | {element[1]} | {element[2]} |")
        print(divider)


def welcome(board):
    '''
        prints a welcome message and also displays the board
    '''
    print("WELCOME! TO TIC TAC TOE") #printing a awelcome message.
    draw_board(board) #calling the board
    # prints the welcome message
    # display the board by calling draw_board(board)

def initialise_board(board):
    '''
        It initializes the board.
    '''
    # develop code to set all elements of the board to one space ' '
    for i in range(3): #loops runs form 0 to 2.
        for j in range(3):  #loops runs form 0 to 2.
            board[i][j] = " " #places blank space in place of numbers.
    return board

def get_player_move(board):
    '''
        It asks user to input their move.
    '''
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            player_move = int(input("Enter your move [1-9]: ")) - 1
            #asks user to input their move
            #  and it subtract the move by 1 as computer process from 0 to 8.
            if 0 <= player_move <= 8:#checks if the move is greater than equals 0
                 #and smaller than equlas to 8.
                col = player_move % 3 #the remainder will be stored in col.
                row = 0 if 0 <= player_move <=2 else (1 if 3 <= player_move <=5 else 2)
                # if the number is from 0 to 2 then it will 0,
                #if the number is bertween 3 to 5 then it will be 1 otherwise it will be 2.
                if board[row][col] != " ": #checks if the cell is already packed or not
                    print("This cell is packed.")# if packed then this message will print
                    continue #abpve line code are run again.
                break# if not then the loop will break.
            raise ValueError("You must enter a number between 1 to 9")
            #the number is not from 1 to 9 then this message will print.
        except ValueError:
            print("The number is not valid. Please enter a valid number.")
    return row, col#returns value of the number in coordinate form.

def choose_computer_move(board):
    '''
        Its turn of the computer to input its move.
    '''
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    clone_board = board.copy() #it just copies the board.
    row, col = 0,0

    #check if computer can win in the next move
    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                #if there is any spaces in the board it will fill that space.
                #  and check if it can win by making that move.
                clone_board[i][j] = "O"
                if check_for_win(board, "O"):
                    #if it wills by making that move, it will enter the loop.
                    row, col = i, j #the coordinates will store in row and column.
                    return row, col
                clone_board[i][j] = " "

    #check if player can win in the next move, then block
    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                clone_board[i][j] = "X"
                #it checks if the player can win by placing X
                if check_for_win(board, "X"):
                    #if the player can win then it will place X in that coordinate
                    row, col = i, j
                    return row, col
                clone_board[i][j] = " "#otherwise there will be blank place

    if clone_board[1][1] == " ":
        #this checks if the center is filled or not.
        #if the center is balnk then it will place its move.
        row, col = 1, 1
        return row, col

    # check empty 4 corners
    for i in [0,2]:
        for j in [0,2]:
            if clone_board[i][j] == " ":
                #if there is empty space in corners then it will place its move there.
                row, col = i, j
                return row, col

    for i in range(3):
        for j in range(3):
            if clone_board[i][j] == " ":
                #if the places 1, 3, 5 and 7 are empty then it will place its move there.
                row, col = i, j
                return row, col
    return None


def check_for_win(board, mark):
    '''
        It checks for win for both user and computer.
    '''
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    win_conditions = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    #conditions for win
    for win in win_conditions: #this loop runs in above win conditions
        cell0_r, cell0_c = win[0] #it gets the coordinates by index.
        cell1_r, cell1_c = win[1] #it gets the coordinates by index.
        cell2_r, cell2_c = win[2] #it gets the coordinates by index.
        if (
            board[cell0_r][cell0_c] == mark and #checks if the coordinates have mark.
            board[cell1_r][cell1_c] == mark and
            board[cell2_r][cell2_c] == mark
        ):
            return True #if there is mark then it returns true otherwise false
    return False

def check_for_draw(board):
    '''
        It checks if the game is draw.
    '''
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
            #if the board contains atleast one empty position.
            # then it returns false as the game could continue otherwse it returns true.
                return False
    return True

def play_game(board):
    '''
        It return 1 for win -1 for computer's win and 0 for draw.
    '''
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            #if the player wins it returns 1 and is added to score
            return 1
        if check_for_draw(board):
            #if the game is draw then it returns 0.
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            #if the computer wins it will return -1
            #and the player's score is subtracted
            return -1
        if check_for_draw(board):
            #if the game is draw then it returns 0.
            return 0

def menu():
    '''
        to get user's input, to play or to save score or to display or to end the program.
    '''
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    choice = ""
    while True:
        try:
            display_message = """Enter one of the following options:
                        1 - play the game
                        2 - Save your score in the leaderboard
                        3 - Load and display the leaderboard
                        q - End the program"""
            print(display_message)#dispplays the above messages.
            choice = input("1, 2, 3, or q? ") #choice to select the options
            if choice in ["1", "2", "3", "q", "Q"]:
                break
            raise ValueError("The input is invalid")
            #if the player enters invalid input it will print the above message.
        except ValueError:
            print("The is choice invalid")
    return choice

def load_scores():
    '''
        Scores are loaded here.
    '''
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    leaders = {} #creating an empty variable
    file_path = (os.path.dirname(__file__)+ "\\leaderboard.txt")
    try:
        with open(file_path, "r", encoding="utf8") as file:
            #using open for reading the leaderboard file
            file_content = file.read()
            leaders = json.loads(file_content)
            # the value stored in string format is converted into the key and value pair.
    except IOError:
        print("Error reading leaderboard.txt")
    return leaders

def save_score(score):
    '''
        It asks for user's name and saves their score.
    '''
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    leaders = load_scores()
    while True:
        try:
            user_name = input("Enter your name: ")
            #asks players's name.
            if user_name == "":
                #if name is empty it will show error
                raise EOFError
            file_path = (os.path.dirname(__file__)+ "\\leaderboard.txt")
            with open(file_path, "w", encoding="utf8") as file:
            #using open to write in the file
                leaders[user_name] = score
                file_content = json.dumps(leaders)
                #above key value pair is changed into string
                file.write(file_content)
                break
        except EOFError:
            print("invalid input")

def display_leaderboard(leaders):
    '''      This part prints the leader board
    '''
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("Leaderboard")
    for key, value in leaders.items():#changes dictionary key value pair into lists.
        print(f"{key}: {value}")


# print(play_game(board1))

# display_leaderboard(load_scores())
