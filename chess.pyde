def setup():
    global white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8
    global black_pawn_1,black_pawn_2,black_pawn_3,black_pawn_4,black_pawn_5,black_pawn_6,black_pawn_7,black_pawn_8
    global white_rook_1, white_rook_2,white_knight_1,white_knight_2, white_bishop_1,white_bishop_2,white_queen, white_king
    global black_rook_1, black_rook_2, black_knight_1, black_knight_2, black_bishop_1, black_bishop_2, black_queen, black_king

    white_pawn_1 = loadImage("white_pawn_1.png")
    white_pawn_2 = loadImage("white_pawn_2.png")
    white_pawn_3 = loadImage("white_pawn_3.png")
    white_pawn_4 = loadImage("white_pawn_4.png")
    white_pawn_5 = loadImage("white_pawn_5.png")
    white_pawn_6 = loadImage("white_pawn_6.png")
    white_pawn_7 = loadImage("white_pawn_7.png")
    white_pawn_8 = loadImage("white_pawn_8.png")
    black_pawn_1 = loadImage("black_pawn_1.png")
    black_pawn_2 = loadImage("black_pawn_2.png")
    black_pawn_3 = loadImage("black_pawn_3.png")
    black_pawn_4 = loadImage("black_pawn_4.png")
    black_pawn_5 = loadImage("black_pawn_5.png")
    black_pawn_6 = loadImage("black_pawn_6.png")
    black_pawn_7 = loadImage("black_pawn_7.png")
    black_pawn_8 = loadImage("black_pawn_8.png")
    white_bishop_1 = loadImage("white_bishop_1.png")
    white_bishop_2 = loadImage("white_bishop_2.png")
    white_knight_1 = loadImage("white_knight_1.png")
    white_knight_2 = loadImage("white_knight_2.png")
    white_rook_1 = loadImage("white_rook_1.png")
    white_rook_2 = loadImage("white_rook_2.png")
    white_queen = loadImage("white_queen.png")
    white_king=loadImage("white_king.png")
    black_bishop_1 = loadImage("black_bishop_1.png")
    black_bishop_2 = loadImage("black_bishop_2.png")
    black_knight_1 = loadImage("black_knight_1.png")
    black_knight_2 = loadImage("black_knight_2.png")
    black_rook_1 = loadImage("black_rook_1.png")
    black_rook_2 = loadImage("black_rook_2.png")
    black_king = loadImage("black_king.png")
    black_queen = loadImage("black_queen.png")
    
    
    size(1000,1000)
    
def draw():
    for i in range(8):
        for j in range(8):
                if (i+j) % 2 == 0:
                    
                     fill(186,104,219)
                else:
                       fill(237,225,242)
        
                rect(i*100,j*100,100,100)
    image(white_pawn_1, 616.5, 716.5,62.5,62.5)
    image(white_rook_1, 16.5, 416.5,62.5,62.5)
    image(black_pawn_8, 16.5, 716.5,62.5,62.5)
    image(black_pawn_2, 516.5, 716.5,62.5,62.5)
    image(black_rook_1, 416.5, 316.5,62.5,62.5)
    image(black_pawn_3, 616.5, 116.5,62.5,62.5)
    image(black_pawn_4, 416.5, 716.5,62.5,62.5)
    image(white_pawn_2, 716.5, 316.5,62.5,62.5)
    image(white_king, 416.5, 616.5,62.5,62.5)
    image(white_bishop_2, 316.5, 216.5,62.5,62.5)
    image(white_pawn_5, 516.5, 716.5,62.5,62.5)
    image(black_king, 716.5, 516.5,62.5,62.5)
    image(white_pawn_6, 416.5, 416.5,62.5,62.5)
    image(black_bishop_2, 116.5, 716.5,62.5,62.5)
    image(white_pawn_3, 116.5, 416.5,62.5,62.5)
    image(black_pawn_7, 616.5, 16.5,62.5,62.5)
