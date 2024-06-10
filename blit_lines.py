import pygame
from fonts import reg_font


screen_w = 1920
screen_h = 1000
size = (screen_w, screen_h)
screen = pygame.display.set_mode(size)

def sentence_list(sentence):
    word_list = []
    word = ""
    for i in sentence:
        if i != " ":
            word += i
        else:
            word_list.append(word)
            word = ""
    word_list.append(word)
    return word_list

def line_sentence(sentence, w):
    mcpl = w/10
    lines = []
    line = ""
    for word in sentence:
        if len(line + word) <= mcpl:
            line += f"{word} "
        else:
            lines.append(line)
            line = f"{word} "
    lines.append(line)
    return lines

def blit_lines(sentence, x, y, w, color):
    lines = line_sentence(sentence_list(sentence), w)
    displays = []
    for line in lines:
        displays.append(reg_font.render(line, True, color))
    for display in displays:
        screen.blit(display, (x ,y))
        y += 40
    return len(lines)