import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("600x600")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
    
    def create_widgets(self):
        self.board_frame = tk.Frame(self.root, bg='light blue', width=600, height=400)
        self.board_frame.pack_propagate(0)
        self.board_frame.pack()
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.board_frame, text="", font=('Helvetica', 24), width=6, height=3,
                                                command=lambda i=i, j=j: self.place_mark(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=10, pady=10)
        
        self.control_frame = tk.Frame(self.root, bg='light grey', width=600, height=200)
        self.control_frame.pack_propagate(0)
        self.control_frame.pack()
        
        self.start_button = tk.Button(self.control_frame, text="Start", font=('Helvetica', 18), command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.restart_button = tk.Button(self.control_frame, text="Restart", font=('Helvetica', 18), command=self.restart_game)
        self.restart_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.draw_button = tk.Button(self.control_frame, text="Draw", font=('Helvetica', 18), command=self.draw_game)
        self.draw_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.stop_button = tk.Button(self.control_frame, text="Stop", font=('Helvetica', 18), command=self.stop_game)
        self.stop_button.pack(side=tk.LEFT, padx=20, pady=20)
    
    def start_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.update_board()
    
    def restart_game(self):
        self.start_game()
    
    def draw_game(self):
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    self.board[i][j] = "D"
        self.update_board()
        self.end_game("It's a draw!")
    
    def stop_game(self):
        self.root.destroy()
    
    def place_mark(self, row, col):
        if not self.board[row][col]:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.end_game(f"{self.current_player} wins!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
            self.update_board()
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = self.board[i][j]
    
    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.start_game()

root = tk.Tk()
app = TicTacToe(root)
root.mainloop()
