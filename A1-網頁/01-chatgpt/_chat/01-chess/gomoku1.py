import turtle

# 繪製棋盤
def draw_board(size, line_color, fill_color1, fill_color2):
    turtle.speed(0)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color1)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size * 8)
        turtle.right(90)
    turtle.end_fill()
    for i in range(10):
        for j in range(8):
            turtle.penup()
            turtle.goto(size * (j - 4), size * (4 - i))
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor(fill_color1 if (i + j) % 2 else fill_color2)
            for k in range(4):
                turtle.forward(size)
                turtle.right(90)
            turtle.end_fill()

# 繪製棋子
def draw_piece(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(40, color)

# 主函數
if __name__ == '__main__':
    # 繪製棋盤
    draw_board(40, 'black', '#ADD8E6', '#87CEEB')
    # 繪製棋子
    draw_piece(-40, 40, 'black')
    draw_piece(40, -40, 'white')
    turtle.mainloop()
