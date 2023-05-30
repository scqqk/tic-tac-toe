import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

def drawBoard():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 20), height=2, width=5, background="lightgray", command=lambda row=i, col=j: click_Event(row, col))
            button.grid(row=i, column=j)
drawBoard()

board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]
current_player = 1

def click_Event(row, col):
    global current_player

    if board[row][col] == 0:
        if current_player == 1:
            board[row][col] = "X"
            current_player = 2
        else:
            board[row][col] = "O"
            current_player = 1

        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])
        checkWinner()

def equals3(a,b,c):
    return (a==b and b==c and a==c)

def checkWinner():
    winner = None

    for i in range (3):
        if (equals3(board[i][0],board[i][1],board[i][2]) and board[i][0] != 0):
            winner = board[i][0]
    for j in range (3):
        if (equals3(board[0][j],board[1][j],board[2][j]) and board[0][j] != 0):
            winner = board[0][j]
    if (equals3(board[0][0],board[1][1],board[2][2])):
        winner = board[0][0]
    if (equals3(board[2][0],board[1][1],board[0][2])):
        winner = board[2][0]
    if all([all(row) for row in board]) and winner is None:
        print ("tie")
    if winner:
        print (f"Player {winner} wins!")
window.mainloop()