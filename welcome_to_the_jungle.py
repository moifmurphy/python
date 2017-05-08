import os
import random

# draw a grid
# pick a random location for player
# pick a random location for exit door
# pick a random location for the monster
# draw the player in the grid
# take the input for movement
# move the player, unless it's an invalid move (past edges of grid)
# check for a win/loss
# clear the screen and redraw the grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True
    
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            
            if player == monster:
                print("\n ** Oh no! You were consumed and spat out like chicken bones. Better luck next time! **\n")
                playing = False
            if player == door:
                print("\n ** You're free, take a moment to reflect on your success and live your life accordingly. **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Mind your face, you might want to get that looked at. **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()


clear_screen()
print("Welcome to the jungle, sorry, dungeon!")
input("Press return to start!")
clear_screen()
game_loop()