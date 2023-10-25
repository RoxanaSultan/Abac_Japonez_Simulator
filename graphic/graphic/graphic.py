import pygame
import time

#initializam pygame
pygame.init()

#cream ecranul
screen = pygame.display.set_mode((1530, 800))
ramaScreen = pygame.Surface([1100, 600])
ramaScreen.fill((189, 163, 131))
plusScreen = pygame.Surface([160, 130])
plusScreen.fill((189, 163, 131))
minusScreen = pygame.Surface([1100, 600])
minusScreen.fill((189, 163, 131))
inmultireScreen = pygame.Surface([1100, 600])
inmultireScreen.fill((189, 163, 131))
impartireScreen = pygame.Surface([1100, 600])
impartireScreen.fill((189, 163, 131))
egalScreen = pygame.Surface([1100, 600])
egalScreen.fill((189, 163, 131))

#titlu
pygame.display.set_caption("Abac Japonez")

#icon
icon = pygame.image.load('abacus.png')
pygame.display.set_icon(icon)

#rama abac
rama = pygame.image.load('ramaAbac.PNG')
coordX = 30
coordY = 60
rama = pygame.transform.scale(rama, (1100, 600))
bila = pygame.image.load('bilaRosie.PNG')
bila = pygame.transform.scale(bila,(86, 67))
mat = []
plusStatus = False
minusStatus = False
multiplyStatus = False
divideStatus = False
equalStatus = False

def ramaAbac():
    screen.blit(rama, (coordX, coordY))

def showinitialAbacus():
    X = 984
    Y = 560
    copieY = Y
    for i in range(0,10):
        Y = copieY
        mat.append([])
        for j in range(0,4):
            mat[i].append([bila, True, X, Y])
            screen.blit(mat[i][j][0], (X, Y))
            Y -= 60
        Y -= 223
        mat[i].append([bila, True, X, Y])
        screen.blit(mat[i][4][0], (X, Y))
        X = X - 99


def showAbacus():
    screen.blit(ramaScreen, (0, 0))
    ramaAbac()
    for i in range(0, 10):
        for j in range(0,5):
            screen.blit(bila, (mat[i][j][2], mat[i][j][3]))

def showOperators():
    plus = pygame.image.load('plus.png')
    plus = pygame.transform.scale(plus, (160, 130))
    screen.blit(plus, (1150, 150))
    minus = pygame.image.load('minus.png')
    minus = pygame.transform.scale(minus, (160,130))
    screen.blit(minus, (1330, 150))
    inmultire = pygame.image.load('inmultire.png')
    inmultire = pygame.transform.scale(inmultire, (160,130))
    screen.blit(inmultire, (1150, 300))
    impartire = pygame.image.load('impartire.png')
    impartire = pygame.transform.scale(impartire, (160,130))
    screen.blit(impartire, (1330, 300))
    egal = pygame.image.load('egal.png')
    egal = pygame.transform.scale(egal, (160,130))
    screen.blit(egal, (1240, 530))

color_active = pygame.Color(180, 199, 231) #culoare cand utilizatorul a selectat casuta
color_inactive = pygame.Color(123, 87, 51) #culoare cand utilizatorul nu a selectat casuta

textBoxes = []
active = [False, False, False]
color = [color_inactive, color_inactive, color_inactive]

def createTextBoxes():
    input_rect = pygame.Rect(1150, 72, 340, 65)
    textBoxes.append(input_rect)
    input_rect = pygame.Rect(1150, 450, 340, 65)
    textBoxes.append(input_rect)
    input_rect = pygame.Rect(1150, 680, 340, 65)
    textBoxes.append(input_rect)
    for i in range(0,3):
        pygame.draw.rect(screen, color[i], textBoxes[i])

font = pygame.font.Font(None, 40)
user_input = ['', '']

def makeNumber(string):
    number = [] 
    for j in range(len(string)-1,-1,-1):
        number.append(int(string[j]))
    return number

def makeNumberToVect(nr):
    number = []
    while nr:
        number.append(nr%10)
        nr = int(nr/10)
    print("este aici")
    print(number)
    return number

def originalColumn(i):
    for j in range(0,5):
        if mat[i][j][1] == False:
            if j == 4:
                mat[i][j][3] -= 120
                showAbacus()
                mat[i][j][1] = True
            else:
                mat[i][j][3] += 85
                showAbacus()
                mat[i][j][1] = True

def modify(i,j, status, value):
    if mat[i][j][1] == status:
        mat[i][j][3] += value
        showAbacus()
        time.sleep(0.7)
        pygame.display.update()
        mat[i][j][1] = not status

def displayNumber(number):
    for i in range(0,len(number)):
        cifra = number[i]
        if cifra >= 5:
            modify(i,4,True, 120)
        else:
            modify(i,4,False, -120)
        for j in range(0,4):
            if 4 - j > cifra % 5:
                modify(i,j,False,85)
        for j in range(3,-1,-1):
            if 4 - j <= cifra % 5:
                modify(i,j,True, -85)
        pygame.display.update()
    for i in range(len(number), 10):
        originalColumn(i)
    
def add(number1, number2):
    length1 = len(number1)
    length2 = len(number2)
    for i in range(length1, length2):
        number1.append(number2[i])
        displayNumber(number1)
    minim = min(length1, length2)
    for i in range(minim - 1, -1, -1):
        for j in range(0, number2[i]):
            number1[i] = number1[i] + 1
            if(number1[i] > 9):
                number1[i] = 0
                carry = 1
                index = i + 1
                while carry == 1:
                    print("da, e carry")
                    print(index)
                    if(index == length1):
                        number1.append(1)
                    else:
                        number1[index] = number1[index] + 1
                    carry = 0
                    if(number1[index] > 9):
                        number1[index] = 0
                        carry = 1
                    index = index + 1
            displayNumber(number1)
    return number1

def substract(number1, number2):
    length1 = len(number1)
    length2 = len(number2)
    for i in range(length2 - 1, -1, -1):
        for j in range(0, number2[i]):
            number1[i] = number1[i] - 1
            if(number1[i] < 0):
                number1[i] = 9
                carry = 1
                index = i + 1
                while(carry):
                    number1[index] = number1[index] - 1
                    carry = 0
                    if(number1[index] < 0):
                        number1[index] = 9
                        carry = 1
                    index = index + 1
            displayNumber(number1)
    return number1
    
def multiply2x1(number1, digit):
    newNumber = add(makeNumberToVect(number1[1] * digit * 10), makeNumberToVect(number1[0] * digit))
    return newNumber

def multiply(number1, number2):
    if len(number1) == 2:
        if len(number2) == 1:
            newNumber = multiply2x1(number1, number2[0])
        else:
            print("a intrat pe 2x2")
            aux = multiply2x1(number1, number2[1])
            aux.insert(0,0)
            print(aux)
            nr2 = multiply2x1(number1, number2[0])
            print(nr2)
            newNumber = add(aux, nr2)
    else:
        if len(number2) == 2:
            newNumber = multiply2x1(number2, number1[0])
        else:
            newNumber = makeNumberToVect(number1[0] * number2[0])
    displayNumber(newNumber)
    return newNumber

def divide(number1, number2):
    newNumber = []
    newNumber.append(int(number1[1]/number2[0]))
    number1[1] = number1[1] % number2[0]
    newNumber.insert(0, int((number1[1] * 10 + number1[0])/number2[0]))
    number1[0] = (number1[1] * 10 + number1[0]) % number2[0]
    for i in range(len(newNumber), 9):
        newNumber.append(0)
    newNumber.append(number1[0])
    displayNumber(newNumber)
    return newNumber

def VectToNumber(vector):
    theNr = 0
    for i in range (len(vector)-1, -1, -1):
        theNr = theNr*10 + vector[i]
    return theNr

#game loop 
running = True
text = []
#RGB - red, green, blue
screen.fill((189, 163, 131))
ramaAbac()
showinitialAbacus()
showOperators()
while running:
    for event in pygame.event.get(): #parcurgem evenimentele din loop
        if event.type == pygame.QUIT:
            running = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(mouse_x>=1160 and mouse_x<=1300 and mouse_y>=160 and mouse_y<=270):
                print("Plus a fost apasat")
                displayNumber(number1)
                plusStatus = True
            if(mouse_x>=1340 and mouse_x<=1480 and mouse_y>=160 and mouse_y<=270):
                print("Minus a fost apasat")
                displayNumber(number1)
                minusStatus = True
            if(mouse_x>=1160 and mouse_x<=1300 and mouse_y>=310 and mouse_y<=420):
                print("Inmultire a fost apasat")
                displayNumber(number1)
                multiplyStatus = True
            if(mouse_x>=1340 and mouse_x<=1480 and mouse_y>=310 and mouse_y<=420):
                print("Impartire a fost apasat")
                displayNumber(number1)
                divideStatus = True
            if(mouse_x>=1250 and mouse_x<=1390 and mouse_y>=540 and mouse_y<=650):
               print("Egal a fost apasat")
               equalStatus = True
            for i in range(0,3):
                if textBoxes[i].collidepoint(event.pos):
                    equalStatus = False
                    active[i] = True
                    active_index = i
                else:
                    active[i] = False
        if event.type == pygame.KEYDOWN:
            if any(active) and active.index(True) != len(active) - 1:
                if event.unicode.isdigit():
                    if len(user_input[active_index]) < 10:
                        user_input[active_index] += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_input[active_index] = user_input[active_index][:-1]
                if event.key == pygame.K_RETURN:
                    if active[0]:
                        equalStatus = False
                        print("a intrat pe active 0")
                    else:
                        if active[1]:
                            print("a intrat pe active 1")
                else:
                    continue
            else: 
                continue
    for i in range(0,3):
        if active[i]:
            color[i] = color_active
        else:
            if equalStatus:
                color[2] = color_active
                color[0] = color_inactive
                color[1] = color_inactive
            else:
                color[i] = color_inactive

    if(mouse_x>=1150 and mouse_x<=1310 and mouse_y>=150 and mouse_y<=280):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        screen.blit(plusScreen, (1150,150))
        plus = pygame.image.load('plus.png')
        plus = pygame.transform.scale(plus, (140, 110))
        screen.blit(plus, (1160, 160))
    else:
        if(mouse_x>=1330 and mouse_x<=1490 and mouse_y>=150 and mouse_y<=280):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            screen.blit(plusScreen, (1330,150))
            minus = pygame.image.load('minus.png')
            minus = pygame.transform.scale(minus, (140, 110))
            screen.blit(minus, (1340, 160))
        else:
            if(mouse_x>=1150 and mouse_x<=1310 and mouse_y>=300 and mouse_y<=430):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                screen.blit(plusScreen, (1150,300))
                inmultire = pygame.image.load('inmultire.png')
                inmultire = pygame.transform.scale(inmultire, (140, 110))
                screen.blit(inmultire, (1160, 310))
            else:
                if(mouse_x>=1330 and mouse_x<=1490 and mouse_y>=300 and mouse_y<=430):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    screen.blit(plusScreen, (1330,300))
                    impartire = pygame.image.load('impartire.png')
                    impartire = pygame.transform.scale(impartire, (140, 110))
                    screen.blit(impartire, (1340, 310))
                else:
                    if(mouse_x>=1240 and mouse_x<=1400 and mouse_y>=530 and mouse_y<=660):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        screen.blit(plusScreen, (1240,530))
                        egal = pygame.image.load('egal.png')
                        egal = pygame.transform.scale(egal, (140, 110))
                        screen.blit(egal, (1250, 540))
                    else:
                        showOperators()
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if mouse_x>=1150 and mouse_x<=1490:
        if mouse_y >= 72 and mouse_y <= 137:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            if mouse_y >= 450 and mouse_y <= 515:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                if mouse_y >= 680 and mouse_y <= 745:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    createTextBoxes()
    for i in range(0,2):
        text_surface = font.render(user_input[i], True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = textBoxes[i].center)
        screen.blit(text_surface, text_rect)
    if user_input[0]:
        number1 = makeNumber(user_input[0])
        print(number1)
    if user_input[1]:
        number2 = makeNumber(user_input[1])
    if equalStatus:
        color[2] = color_active
        if plusStatus:
            text = add(number1, number2)
            plusStatus = False
        if minusStatus:
            text = substract(number1, number2)
            minusStatus = False
        if multiplyStatus:
            text = multiply(number1,number2)
            multiplyStatus = False
        if divideStatus:
            print("divide")
            text = divide(number1, number2)
            divideStatus = False
        showText = font.render(str(VectToNumber(text)), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = textBoxes[2].center)
        screen.blit(showText, text_rect)
    pygame.display.update()