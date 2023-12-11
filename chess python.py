chess_pieces = {1: 'white_pawn_1', 2: 'white_pawn_2', 3: 'white_pawn_3', 4: 'white_pawn_4', 5: 'white_pawn_5', 6: 'white_pawn_6',
                7: 'white_pawn_7', 8: 'white_pawn_8', 9: 'white_rook_1', 10: 'white_knight_1', 11: 'white_bishop_1',
                12: 'white_queen', 13: 'white_king', 14: 'white_bishop_2', 15: 'white_knight_2', 16: 'white_rook_2',
                17: 'black_pawn_1', 18: 'black_pawn_2', 19: 'black_pawn_3', 20: 'black_pawn_4', 21: 'black_pawn_5', 22: 'black_pawn_6',
                23: 'black_pawn_7',
                24: 'black_pawn_8', 25: 'black_rook_1',
                26: 'black_knight_1', 27: 'black_bishop_1', 28: 'black_queen', 29: 'black_king',
                30: 'black_bishop_2', 31: 'black_knight_2', 32: 'black_rook_2'}

import random
included={}
for x in range(1,random.randint(1,32)):
    y=random.randint(1,32)
    included[y]=chess_pieces[y]
    

def generate(chess_pieces):
    coordinates = {}

    
    for key,value in included.items():
            i = random.randint(0, 7)
            j = random.randint(0, 7)
            coordinates[key] = (50 + (i * 100)-33.5, 50 + (j * 100)-33.5)

    return coordinates


chess_coordinates =generate(chess_pieces)

for key, coordinates in chess_coordinates.items():
    a, b = coordinates
    name = chess_pieces[key]
    command_string = f'image({name}, {a}, {b},62.5,62.5)'
    print(command_string)
