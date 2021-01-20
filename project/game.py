import pygame, os, sys, random, time
from pygame.locals import *
from pygame.locals import QUIT

winw=400
winh=650

# print any text on the screen
def msg(screen, text, color = (0, 0, 0), bgcolor = (255, 255, 255), size = 36, pos = (-1, -1)):
    if pos[0] == -1: pos = (screen.get_rect().centerx, pos[1])
    if pos[1] == -1: pos = (pos[0], screen.get_rect().centery)
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, color, bgcolor)
    textpos = text.get_rect()
    textpos.centerx = pos[0]
    textpos.centery = pos[1]
    screen.blit(text, textpos)

class button():
    x = 0
    y = -winh // 5
    w = winw // 4-1
    h = winh // 5
    notclick = True
    def __init__(self, n):
        self.x = n*winw // 4

class black(button):
    score = 100
    def update(self, screen):
        if self.notclick: pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.w, self.h])
        else: pygame.draw.rect(screen, (180, 180, 180), [self.x, self.y, self.w, self.h])
    def clicked(self):
        self.notclick = False

class grey(button):
    score = -100
    def update(self, screen):
        if self.notclick: pygame.draw.rect(screen, (200,200,200), [self.x, self.y, self.w, self.h])
        else: pygame.draw.rect(screen, (180, 180, 180), [self.x, self.y, self.w, self.h])
    def clicked(self):
        self.notclick = False
    
class white(button):
    score = -100
    def update(self, screen):
        if self.notclick: pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, self.w, self.h])
        else: pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.w, self.h])
        self.notclick = True
    def clicked(self):
        self.notclick = False

# main game part
def game(name):
    with open(name) as f:
        temp = f.read()
        temp2 = temp.split("\n")
        piano = temp2[0].split(",")
        chord = temp2[1].split(",")
        drum = temp2[2].split(",")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.display.set_caption("Just Tap The Black Tile : " + name)
    screen = pygame.display.set_mode((winw, winh))
    clock = pygame.time.Clock()
    FPS = 60
    musiclist = piano + [""] * 5
    xlist = [random.randint(0, 3) for _ in range(len(musiclist))]
    score = 0
    time = 0

    buttonlist = []
    for i in range(len(musiclist)):
        rowlist = []
        if musiclist[i] == "-":
            for j in range(4):
                temp = grey(j)
                rowlist.append(temp)
        else:
            for j in range(4):
                if j == xlist[i]:
                    if i >= 64:
                        temp = white(j)
                        rowlist.append(temp)
                    else:
                        temp = black(j)
                        rowlist.append(temp)
                else:
                    temp = white(j)
                    rowlist.append(temp)
        buttonlist.append(rowlist)

    index = 0
    result = 0
    for i in range(5):
        for j in range(4):
            buttonlist[i][j].y = winh // 5 * (4 - i)

    while len(buttonlist) > 5:
        time += 1 / FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:    
                    buttonlist[0][0].clicked()
                    result = buttonlist[0][0].score
                    score += result
                    if result == 100:
                        buttonlist.pop(0)
                        for i in range(5):
                            for j in range(4):
                                buttonlist[i][j].y = winh // 5 * (4 - i)

                        if pygame.mixer.Channel(0).get_busy() and piano[index] != "-":
                            pygame.mixer.Channel(0).stop()
                        
                        if pygame.mixer.Channel(2).get_busy() and drum[index] != "-":
                            pygame.mixer.Channel(2).stop()

                        if pygame.mixer.Channel(1).get_busy() and (index) % 8 == 0:
                            pygame.mixer.Channel(1).stop()

                        if piano[index] != "-":
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sound/piano/{piano[index]}.wav'))

                        if index % 8 == 0 and chord[index//8] != "-":
                            if not pygame.mixer.Channel(1).get_busy():
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sound/chord/{chord[index//8]}.wav'))

                        if drum[index] != "-":
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(f'sound/drum/{drum[index]}.wav'))

                        index += 1
                    
                    else:
                        if pygame.mixer.Channel(3).get_busy():
                            pygame.mixer.Channel(3).stop()
                        if not pygame.mixer.Channel(3).get_busy():
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'sound/piano/false.wav'))


                elif event.key == K_w:
                    buttonlist[0][1].clicked()
                    result = buttonlist[0][1].score
                    score += result
                    if result == 100:
                        buttonlist.pop(0)
                        for i in range(5):
                            for j in range(4):
                                buttonlist[i][j].y = winh // 5 * (4 - i)

                        if pygame.mixer.Channel(0).get_busy() and piano[index] != "-":
                            pygame.mixer.Channel(0).stop()
                        
                        if pygame.mixer.Channel(2).get_busy() and drum[index] != "-":
                            pygame.mixer.Channel(2).stop()

                        if pygame.mixer.Channel(1).get_busy() and (index) % 8 == 0:
                            pygame.mixer.Channel(1).stop()

                        if piano[index] != "-":
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sound/piano/{piano[index]}.wav'))

                        if index % 8 == 0 and chord[index//8] != "-":
                            if not pygame.mixer.Channel(1).get_busy():
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sound/chord/{chord[index//8]}.wav'))

                        if drum[index] != "-":
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(f'sound/drum/{drum[index]}.wav'))

                        index += 1

                    else:
                        if pygame.mixer.Channel(3).get_busy():
                            pygame.mixer.Channel(3).stop()
                        if not pygame.mixer.Channel(3).get_busy():
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'sound/piano/false.wav'))

                elif event.key == K_e:
                    buttonlist[0][2].clicked()
                    result = buttonlist[0][2].score
                    score += result
                    if result == 100:
                        buttonlist.pop(0)
                        for i in range(5):
                            for j in range(4):
                                buttonlist[i][j].y = winh // 5 * (4 - i)

                        if pygame.mixer.Channel(0).get_busy() and piano[index] != "-":
                            pygame.mixer.Channel(0).stop()
                        
                        if pygame.mixer.Channel(2).get_busy() and drum[index] != "-":
                            pygame.mixer.Channel(2).stop()

                        if pygame.mixer.Channel(1).get_busy() and (index) % 8 == 0:
                            pygame.mixer.Channel(1).stop()

                        if piano[index] != "-":
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sound/piano/{piano[index]}.wav'))

                        if index % 8 == 0 and chord[index//8] != "-":
                            if not pygame.mixer.Channel(1).get_busy():
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sound/chord/{chord[index//8]}.wav'))

                        if drum[index] != "-":
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(f'sound/drum/{drum[index]}.wav'))

                        index += 1

                    else:
                        if pygame.mixer.Channel(3).get_busy():
                            pygame.mixer.Channel(3).stop()
                        if not pygame.mixer.Channel(3).get_busy():
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'sound/piano/false.wav'))

                elif event.key == K_r:
                    buttonlist[0][3].clicked()
                    result = buttonlist[0][3].score
                    score += result
                    if result == 100:
                        buttonlist.pop(0)
                        for i in range(5):
                            for j in range(4):
                                buttonlist[i][j].y = winh // 5 * (4 - i)

                        if pygame.mixer.Channel(0).get_busy() and piano[index] != "-":
                            pygame.mixer.Channel(0).stop()
                        
                        if pygame.mixer.Channel(2).get_busy() and drum[index] != "-":
                            pygame.mixer.Channel(2).stop()

                        if pygame.mixer.Channel(1).get_busy() and (index) % 8 == 0:
                            pygame.mixer.Channel(1).stop()

                        if piano[index] != "-":
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sound/piano/{piano[index]}.wav'))

                        if index % 8 == 0 and chord[index//8] != "-":
                            if not pygame.mixer.Channel(1).get_busy():
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sound/chord/{chord[index//8]}.wav'))

                        if drum[index] != "-":
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(f'sound/drum/{drum[index]}.wav'))

                        index += 1
                    
                    else:
                        if pygame.mixer.Channel(3).get_busy():
                            pygame.mixer.Channel(3).stop()
                        if not pygame.mixer.Channel(3).get_busy():
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'sound/piano/false.wav'))

                elif event.key == K_SPACE:
                    if musiclist[index] == "-":
                        result = 100
                    else:
                        result = -100
                    score += result
                    if result == 100:
                        buttonlist.pop(0)
                        for i in range(5):
                            for j in range(4):
                                buttonlist[i][j].y = winh // 5 * (4 - i)

                        if pygame.mixer.Channel(0).get_busy() and piano[index] != "-":
                            pygame.mixer.Channel(0).stop()
                        
                        if pygame.mixer.Channel(2).get_busy() and drum[index] != "-":
                            pygame.mixer.Channel(2).stop()

                        if pygame.mixer.Channel(1).get_busy() and (index) % 8 == 0:
                            pygame.mixer.Channel(1).stop()

                        if piano[index] != "-":
                            if not pygame.mixer.Channel(0).get_busy():
                                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sound/piano/{piano[index]}.wav'))

                        if index % 8 == 0 and chord[index//8] != "-":
                            if not pygame.mixer.Channel(1).get_busy():
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sound/chord/{chord[index//8]}.wav'))

                        if drum[index] != "-":
                            if not pygame.mixer.Channel(2).get_busy():
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(f'sound/drum/{drum[index]}.wav'))

                        index += 1
                    
                    else:
                        if pygame.mixer.Channel(3).get_busy():
                            pygame.mixer.Channel(3).stop()
                        if not pygame.mixer.Channel(3).get_busy():
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'sound/piano/false.wav'))

                # pause
                elif event.key == K_p:
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN and event.key == K_p:
                                pause = False

            for i in range(5):
                for j in range(4):
                    buttonlist[i][j].update(screen)

        msg(screen,"SCORE " + str(score), color = (0, 0, 0), pos = (-1, 30))
        msg(screen,"TIME " + str(round(time)), color = (0, 0, 0), pos = (-1,60))
        pygame.display.update()
                
    pygame.mixer.music.stop()
    screen.fill((255, 255, 255))
    msg(screen, "your best score is " + str(score) + " point!!", color = (0, 0, 0), pos = (-1, -1))
    msg(screen, "your best time is " + str(round(time)) + " second!!", color = (0, 0, 0), pos = (-1,winh//2+60))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()

if __name__ == "__main__":
    game("1.txt")