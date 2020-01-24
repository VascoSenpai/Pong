import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
LEFTCLICK = (1, 0, 0)
WIDTH = 1440
HEIGHT = 900
BALLSPEED = 8

class Player:
    def __init__(self, surface, initialPosition, keys):
        self.initialPosition = initialPosition
        self.positionY = self.initialPosition[1]
        self.surface = surface
        self.width = 20
        self.height = 200
        self.dy = 0
        self.keys = keys
        self.positive = 0
        self.negative = 0
        self.points = 0

    
    def draw(self):
        pygame.draw.rect(self.surface, WHITE, (self.initialPosition[0], self.positionY,self.width, self.height))
        # pygame.display.update()


    def move(self):
        self.dy = 0
        if HEIGHT - (self.height / 2) > self.positionY:  
            self.dy += self.positive
        if 0 - (self.height / 2) < self.positionY:
            self.dy += self.negative

        self.positionY += self.dy
        self.draw()


class Ball:
    def __init__(self, surface, initialPosition, radius):
        self.surface = surface
        self.initialPosition = initialPosition
        self.radius = radius
        self.speedX = 0
        self.speedY = 0
        self.position = [self.initialPosition[0], self.initialPosition[1]]
        # self.turningPoint = self.initialPosition[1]
        self.dx = 0
        self.dy = 0
        ###
        self.realspeedX = 8
        ###
        
    
    def start(self):
        self.position[0] = self.initialPosition[0]
        self.position[1] = self.initialPosition[1]
        rand = randint(0, 3)
        self.initialspeedX = 2
        self.speedX = self.initialspeedX
        self.speedY = 2
        if rand == 0:
            self.dx = self.speedX
            self.dy = self.speedY
        elif rand == 1:
            self.dx = self.speedX
            self.dy = -self.speedY
        elif rand == 2:
            self.dx = -self.speedX
            self.dy = self.speedY
        elif rand == 3:
            self.dx = -self.speedX
            self.dy = -self.speedY
    

    def draw(self):
        pygame.draw.circle(self.surface, GRAY, self.position, self.radius)
        # pygame.display.update()


    def moveX(self):
        global player1
        global player2
        #pygame.time.delay(1)
        if self.position[0] == (player2.initialPosition[0]-self.radius):
            if self.position[1]+self.radius >= player2.positionY-5 and self.position[1]-self.radius <= (player2.positionY + player2.height+5): 
                self.speedX =  self.realspeedX            
                self.dx = -self.speedX
                # self.turningPoint = self.position[1]

        elif self.position[0] == (player1.initialPosition[0] + player1.width +self.radius):
            if self.position[1]+self.radius >= player1.positionY-5 and self.position[1]-self.radius <= (player1.positionY + player1.height+5):
                self.speedX =  self.realspeedX
                self.dx = self.speedX 

        self.position[0] += int(self.dx)
        # self.draw()


    def moveY(self):
        if self.position[0] == (player2.initialPosition[0]-self.radius):
            if self.position[1]+self.radius >= player2.positionY-5 and self.position[1]-self.radius <= (player2.positionY + player2.height+5):
                self.speedY = randint(1, 6)
                if self.dy > 0:
                    self.dy = self.speedY
                else:
                    self.dy = -self.speedY
        elif self.position[0] == (player1.initialPosition[0] + player1.width +self.radius):
            if self.position[1]+self.radius >= player1.positionY-5 and self.position[1]-self.radius <= (player1.positionY + player1.height+5):
                self.speedY = randint(1, 4)
                if self.dy > 0:
                    self.dy = self.speedY
                else:
                    self.dy = -self.speedY

        
        if self.position[1] >= HEIGHT - self.radius:
            self.dy = -self.speedY
        elif self.position[1] <= 0 + self.radius:
            self.dy = self.speedY
        self.position[1] += self.dy


    def move(self):
        self.moveX()
        self.moveY()
        # self.isDead()
        if self.isDead():
            self.position = [self.initialPosition[0], self.initialPosition[1]]
            self.speedX = 0
            self.speedY = 0
            self.dx = 0
            self.dy = 0
            # self.position = [self.initialPosition[0], self.initialPosition[1]]
            # pygame.draw.circle(self.surface, GRAY, self.initialPosition, self.radius)
            # pygame.time.delay(1)

        self.draw()


    def isDead(self):
        if self.position[0] <= 0:
            player2.points += 1
            
            return True
            
        
        if self.position[0] >= WIDTH:
            player1.points += 1
            return True

        return False



class Button:
    pygame.font.init()
    def __init__(self, surface, coordinates, width, height, text, font = pygame.font.Font('FFFFORWA.TTF', 32)):
        self.surface =surface
        self.position = coordinates
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.outsideColor = WHITE
        self.insideColorOut = BLACK
        self.insideColorIn = GRAY


    def isMouseOn(self):
        global mouse
        try:
            mouseX = mouse[0]
            mouseY = mouse[1]
            positionX = self.position[0]
            positionY = self.position[1]

            if mouseX >= positionX and mouseX <= positionX + self.width:
                if mouseY >= positionY and mouseY <= positionY + self.height:
                    return True
        except:
            pass
        return False

    def draw(self):
        # Outside Box
        pygame.draw.rect(self.surface, self.outsideColor, (self.position[0], self.position[1], self.width, self.height))

        # Inside Box
        if self.isMouseOn():
            pygame.draw.rect(self.surface, self.insideColorIn, (self.position[0] + 10, self.position[1] + 10, self.width - 20, self.height - 20))
        else:
            pygame.draw.rect(self.surface, self.insideColorOut, (self.position[0] + 10, self.position[1] + 10, self.width - 20, self.height - 20))

        #Text
        # pygame.font.init()
        #font = pygame.font.Font('FFFFORWA.TTF', 32)
        textsurface = self.font.render(self.text, False, self.outsideColor)
        self.surface.blit(textsurface, (self.position[0] + 30, self.position[1] + 25))
        pygame.display.update()




def clear(surface):
    surface.fill(BLACK)


def checkKeys():
    global player1
    global player2
    global ball
    global mouse
    global mouseClick

    playerSpeed = 6

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if event.type == pygame.KEYDOWN:

            if keys[119] == 1:
                player1.negative = -playerSpeed
            if keys[115] == 1:
                player1.positive = playerSpeed

            if keys[273] == 1:
                player2.negative = -playerSpeed
            if keys[274] == 1:
                player2.positive = playerSpeed

            if keys[32] == 1 and ball.speedX == 0:
                ball.start()
                
           
        if event.type == pygame.KEYUP:

            if keys[119] == 0: 
                player1.negative = 0
            if keys[115] == 0:
                player1.positive = 0
            if keys[273] == 0:
                player2.negative = 0
            if keys[274] == 0:
                player2.positive = 0


def showScore(surface):
    pygame.font.init()
    font = pygame.font.Font('FFFFORWA.TTF', 60)
    if player1.points < 10:
        textsurface = font.render(' ' + str(player1.points), False, (255, 255, 255))
    else:
        textsurface = font.render(str(player1.points), False, (255, 255, 255))
    surface.blit(textsurface, (WIDTH // 2 - 120, 30))

    textsurface = font.render(str(player2.points), False, (255, 255, 255))
    surface.blit(textsurface, (WIDTH // 2 + 40, 30))
    textsurface = font.render('-', False, (255, 255, 255))
    surface.blit(textsurface, (WIDTH // 2 - 20, 30))
    pass


def menu(surface):
    global mouseClick
    global start
    startButton = Button(surface, (WIDTH // 2 - 100, 100), 200, 100, text = 'START')
    startButton.draw()

    if mouseClick == LEFTCLICK and startButton.isMouseOn():
        start = True


def home(surface):
    pygame.draw.rect(surface, WHITE, (WIDTH-90, 0 + 55, 40, 40))
    pygame.draw.polygon(surface, WHITE, ((WIDTH-69, 40), (WIDTH-90, 55), (WIDTH-50, 55)))
    pygame.display.update()


def main():

    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    global start

    global player1
    global player2
    global ball

    player1 = Player(surface, (20, 300), (119, 115))
    player2 = Player(surface, (WIDTH - 40, 300), (273, 274))

    ball = Ball(surface, (WIDTH // 2, HEIGHT // 2), 12)
    #homeButton = Button(surface, (WIDTH // 2 - 35, HEIGHT - 100), 70, 70, '')

    #ball.draw()

    #player1.draw()
    #player2.draw()
    running = True
    start = False
    
    ###
    
    ###
    while running:
        
        while not start:
            surface.fill(BLACK)
            checkKeys()
            menu(surface)
        
        clear(surface)
        checkKeys()
        player2.move()
        # checkKeys()
        player1.move()
        showScore(surface)
        ball.move()
        #homeButton.draw()
        # home(surface)
        '''
        if mouseClick == LEFTCLICK and homeButton.isMouseOn():
            start = False

        '''
        pygame.display.update()
        pygame.time.delay(1)
    



main()
