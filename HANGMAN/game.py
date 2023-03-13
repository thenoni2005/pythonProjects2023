import settings as settings
import random


def game():
    word = random.choice(settings.WORDS)
    soFar = "?"*len(word)
    usedLetters = []

    print("Welcome to Bowser's Big Bean Burrito.   Good luck")
    while settings.guesses < settings.maxGuess and soFar != word:
        print(settings.HANGMAN[settings.guesses])
        print("You have used these letters")
        print(usedLetters)
        print()
        print()

        print("\nSo far, the word is:\n", soFar)

        guess = ""
        while guess in usedLetters:
            guess = input("\n\n pick a letter: ")
            if guess.isalpha():
                guess = guess.lower()
            else:
                continue
        usedLetters.append(guess)

        if guess in word:
            print("\nYes!", guess, "is in the word")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                     new += soFar[i]
            soFar = new

        else:
            print("Incorrect you almost failed Bowser's Big Bean Burrito")
            settings.guesses =+ 1

def displayInstructions():
    print("Welcome")
    print("# 0-9")
    displayBoard([1,2,3,4,5,6,7,8,9])
    print("Get ready")
    input("enter to continue")

def displayBoard(curboard):
    print(str.format("""
    \t{0} | {1} | {2}
    \t---------------
    \t{3} | {4} | {5}
    \t---------------
    \t{6} | {7} | {8}
    
    
    """,curboard[0],curboard[1],curboard[2],curboard[3],curboard[4],curboard[5],curboard[6],curboard[7],curboard[8]))

def newBoard():
    board = []
    for i in range(settings.MAXSPOTS):
        board.append(settings.E)

    return board
def rockPaperScissors():
    while True:
        options = ["Rock","Paper","Scissors"]
        choice = settings.display_menu(options,"choose?")
        player = options[choice-1]
        comp = random.choice(options)
        print("you",player)
        print("comp",comp)
        if (comp == options[0] and player == options[2]) or (comp == options[1] and player == options[0]) or \
                (comp == options[2] and player == options[1]):
            return "lose"
        elif comp == player:
            print("tie")
            continue
        else:
            print("player wins")



def setPieces():
    win = rockPaperScissors()
    if win == "win":
        human = settings.X
        comp = settings.O
    else:
        human = settings.O
        comp = settings.X
    return human,comp

def humanTurn(board, human):
    legal = legalMoves(board)
    choice = -1
    while choice not in legal:
        choice = settings.getNumberInRange("What square would you like",1,settings.MAXSPOTS)-1
        if choice in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")

    return choice








def compMove(board,comp,human):

    diff = input("what is your difficulty? easy,normal,hard: ")
    copyOfBoard = board[:]
    legal = legalMoves(board)

    diff = "easy"
    if diff == "easy":
        # easy
        choice = 0
        choice = random.choice(legal)
        return choice
    elif diff == "normal":
        if(comp == settings.X):
            bestMovesList = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        else:
            bestMovesList = [1, 3, 5, 7, 4, 0, 2, 6, 8]
    elif diff == "hard":
        if (comp == settings.X):
            bestMovesList = [3, 6, 7]
        else:
            bestMovesList = [1, 3, 5, 7, 4, 0, 2, 6, 8]

        #checking if comp can win
        for move in legal:
            copyOfBoard[move] = comp
            if winner(copyOfBoard) == comp:
                print("I shall take square number"+ str(move +1))
                return move

            copyOfBoard[move] = settings.E
        # if human can win
        for move in legal:
            copyOfBoard[move] = human
            if winner(copyOfBoard) == human:
                print("I shall take square number" + str(move + 1))
                return move

            copyOfBoard[move] = settings.E

        for move in bestMovesList:
            if move in legal:
                print("I shall take square number" + str(move + 1))
                return move



def winner(board):
    winner = ""
    waysToWin = [[0,1,2],[3,4,5,],[6,7,8],[1,4,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8],[3,6,7]]
    for row in waysToWin:
        if board[row[0]] == board[row[1]] == board[row[2]] != settings.E:
            winner = board[row[0]]
            return winner
    if settings.E not in board:
        return "Tie"

    return None


def legalMoves(board):
    moves = []
    for i in range(settings.MAXSPOTS):
        if board[i] == settings.E:
            moves.append(i)
    return moves

def nextTurn(turn):
    if turn == settings.X:
        return settings.O
    else:
        return settings.X

def congrats(win,comp,human):
    if win != "Tie":
        print(win, "has won!/n")
    if win == comp:
        print("Hee Hee Haw")
    elif win == human:
        print("clash royal - angry face - ")
    elif win == "Tie":
        print("Im going to akinator your home address for mischievous purposes")

def gameTikTacToe():
    displayInstructions()
    board = newBoard()
    human, comp = setPieces()
    turn = settings.X
    displayBoard(board)


    while not winner(board):
        if turn == human:
            move = humanTurn(board,human)
            board[move] = human
        else:
            move = compMove(board,comp,human)
            board[move] = comp
        displayBoard(board)
        turn = nextTurn(turn)
    win = winner(board)
    congrats(win,comp,human)