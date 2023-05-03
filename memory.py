import simplegui
import random

def new_game():
    global deck, exposed, state, cIndex1, cIndex2, nScore, nMoves
    state, nScore, nMoves, cIndex1, cIndex2 = 0, 0, 0, -1, -1
    deck = [x for x in range(8)]*2
    random.shuffle(deck)
    exposed = [False]*16

def mouseclick(pos):
    global state, nScore, cIndex1, cIndex2, nMoves
    cardIndex = list(pos)[0]//50 
    if not exposed[cardIndex]:
        if state == 0: 										
            cIndex1 = cardIndex
            exposed[cardIndex] = True
            state = 1
        elif state == 1: 								
            cIndex2 = cardIndex
            exposed[cardIndex] = True
            if deck[cIndex1] == deck[cIndex2]:
                nScore += 1
            state = 2
            nMoves += 1
            label.set_text("Turns = " + str(nMoves))
        else: 													
            if deck[cIndex1] != deck[cIndex2]:
                exposed[cIndex1], exposed[cIndex2] = False, False
                cIndex1, cIndex2 = -1, -1
            cIndex1 = cardIndex
            exposed[cardIndex] = True
            state = 1   
  
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(deck[i]), (i*50+11, 69), 55, "Black")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
    label.set_text("Turns = " + str(nMoves))

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()