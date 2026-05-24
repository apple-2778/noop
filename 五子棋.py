import tkinter as tk
from tkinter import messagebox

# 棋盘参数
BOARD_SIZE = 15  # 15x15棋盘
GRID_SIZE = 40   # 每个格子的像素大小
MARGIN = 20      # 棋盘边距

class Wuziqi:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋 - WuZiQi")
        canvas_size = MARGIN * 2 + GRID_SIZE * (BOARD_SIZE - 1)
        self.canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="burlywood")
        self.canvas.pack()

        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # 0:空 1:黑 2:白
        self.turn = 1  # 黑棋先手
        self.draw_board()

        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        for i in range(BOARD_SIZE):
            x0 = MARGIN
            y0 = MARGIN + i * GRID_SIZE
            x1 = MARGIN + (BOARD_SIZE - 1) * GRID_SIZE
            y1 = y0
            self.canvas.create_line(x0, y0, x1, y1)

            x0 = MARGIN + i * GRID_SIZE
            y0 = MARGIN
            x1 = x0
            y1 = MARGIN + (BOARD_SIZE - 1) * GRID_SIZE
            self.canvas.create_line(x0, y0, x1, y1)

    def handle_click(self, event):
        col = round((event.x - MARGIN) / GRID_SIZE)
        row = round((event.y - MARGIN) / GRID_SIZE)

        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if self.board[row][col] == 0:
                self.board[row][col] = self.turn
                self.draw_piece(row, col, self.turn)

                if self.check_win(row, col):
                    winner = "黑棋" if self.turn == 1 else "白棋"
                    messagebox.showinfo("游戏结束", f"{winner} 获胜！")
                    self.canvas.unbind("<Button-1>")
                else:
                    self.turn = 3 - self.turn  # 切换玩家

    def draw_piece(self, row, col, player):
        x = MARGIN + col * GRID_SIZE
        y = MARGIN + row * GRID_SIZE
        r = GRID_SIZE // 2 - 2
        color = "black" if player == 1 else "white"
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="black")

    def check_win(self, row, col):
        def count(dx, dy):
            count = 1
            for dir in [1, -1]:
                i = 1
                while True:
                    r = row + dir * i * dy
                    c = col + dir * i * dx
                    if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.turn:
                        count += 1
                        i += 1
                    else:
                        break
            return count

        # 检查四个方向
        return (count(1, 0) >= 5 or   # 横向
                count(0, 1) >= 5 or   # 纵向
                count(1, 1) >= 5 or   # 主对角线
                count(1, -1) >= 5)    # 副对角线

# 启动游戏
if __name__ == "__main__":
    root = tk.Tk()
    game = Wuziqi(root)
    root.mainloop()
