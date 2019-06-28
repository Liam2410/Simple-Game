import pygame
import random
import time
import math

class Game:
    
    #creat window
    windowHeight = 600
    windowWidth = 800
    
    crashed = False
    intro = True
    gameDisplay = None
    clock = pygame.time.Clock()

    #color
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    gray = (127,127,127)
    blue_green = (0,255,170)
    sky_blue = (0,255,255)
    forest_green = (0,100,0)
    dark_red = (175,0,0)
    dark_red2 = (200,0,0)
    dark_green = (0,200,0)
    dark_blue = (0,0,150)
    light_gray = (195,195,195)
    lightseagreen = (32,178,170)
    steelblue1 = (99,184,255)
    steelblue3 = (79,148,205)
    
    #x,y,z,choice_number
    x = 0
    y = 0
    z = 0
    choice_lost_number = 0
    op = None
    level = 0
    place = 0
    check = -1
    random_num = 0
    time_answer = 10
    x_time = 0
    clock = pygame.time.Clock()
        
    def runGame(self):
        pygame.init()
        pygame.display.set_caption('Brain Game')
        self.gameDisplay = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.gameDisplay.fill(self.blue_green)
        self.introGame()
        self.gameQuit()
        pygame.display.update()
        

    def introGame(self):
        while (self.intro):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameQuit()
            #draw text: Brain Game
            self.drawText("Brain Game", self.windowWidth/2, self.windowHeight/2, 65, self.white)

            #draw Go button
            self.button("LET'S GO",350,350,100,50,self.blue,self.dark_green,15,self.chooseDifficulty)
            pygame.display.update()


    def chooseDifficulty(self):
        
        while (self.intro):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameQuit()
            #draw text: Choose Difficulty
            self.gameDisplay.fill(self.sky_blue)
            self.drawText("Choose Level", self.windowWidth/2, 100, 65, self.white)
            
            #draw choice of player
            self.choice("Easy",0,250,100,50,self.green,self.dark_green,15,1)
            self.choice("Normal",350,250,100,50,self.blue,self.dark_blue,15,2)
            self.choice("Hard",700,250,100,50,self.red,self.dark_red,15,3)
            if self.level != 0:
                self.gameLoop()
            
            pygame.display.update()
            
    
    def gameLoop(self):

        self.intro = False
        
        self.createValue()
        
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
            

            self.gameDisplay.fill(self.lightseagreen)

            self.drawQuestion()

            self.drawAnswer()

            self.checkAnswer()

            self.countTime()

            pygame.display.update()

            self.clock.tick(60)


    def createValue(self):
        
        self.choice_lost_num = random.randint(1,3)
        
        self.op = random.choice(['+','-','*','/'])
        
        self.place = random.randint(1,4)
        
        self.random_num = random.randint(1,10)

        #Easy
        if self.level == 1:
            
            if self.op == '+':
                self.z = random.randint(10,20)
                self.x = random.randint(1,self.z-1)
                self.y = random.randint(1,self.z-1)
                
            elif self.op == '-':
                self.x = random.randint(10,20)
                self.y = random.randint(1,self.x-1)
                self.z = random.randint(1,self.x-1)
                
            elif self.op == '*':
                self.z = random.randint(10,20)
                self.x = random.randint(1,self.z-1)
                self.y = random.randint(1,self.z-1)
                while(self.z % self.x != 0 or self.z % self.y != 0):
                    self.x = random.randint(1,self.z-1)
                    self.y = random.randint(1,self.z-1)

            else:
                self.x = random.randint(10,20)
                while(self.isPrime(self.x)):
                    self.x = random.randint(10,20)
                self.y = random.randint(1,self.x-1)
                self.z = random.randint(1,self.x-1)
                while(self.x % self.y != 0 or self.x % self.z != 0):
                    self.y = random.randint(1,self.x-1)
                    self.z = random.randint(1,self.x-1)
                    
        #Normal
        elif self.level == 2:
            
            if self.op == '+':
                self.z = random.randint(20,50)
                self.x = random.randint(10,self.z-1)
                self.y = random.randint(10,self.z-1)

            elif self.op == '-':
                self.x = random.randint(20,50)
                self.y = random.randint(10,self.x-1)
                self.z = random.randint(10,self.x-1)

            elif self.op == '*':
                
                self.z = random.randint(15,35)
                self.x = random.randint(5, self.z - 1)
                self.y = random.randint(5, self.z - 1)
                
                if self.choice_lost_num == 1:
                    self.y = random.randint(2,5)
                    while(self.isPrime(self.z)):
                        self.z = random.randint(15,35)
                    while(self.z % self.y != 0):
                        self.y +=  1
                elif self.choice_lost_num == 2:
                    self.x = random.randint(2,5)
                    while(self.isPrime(self.z)):
                        self.z = random.randint(15,35)
                    while(self.z % self.x != 0):
                        self.x += 1

            else:
                
                self.z = random.randint(15,35)
                self.x = random.randint(5, self.z - 1)
                self.y = random.randint(5, self.z - 1)
                
                if self.choice_lost_num == 2:
                    self.z = random.randint(2, 5)
                    while(self.isPrime(self.x)):
                        self.x = random.randint(15,35)
                    while self.x % self.z != 0:
                        self.z += 1

                elif self.choice_lost_num == 3:
                    self.y = random.randint(2, 5)
                    while(self.isPrime(self.x)):
                        self.x = random.randint(15,35)
                    while self.x % self.y != 0:
                        self.y += 1
            
        #Hard
        elif self.level == 3:

            if self.op == '+':
                self.z = random.randint(70,100)
                self.x = random.randint(50,self.z-1)
                self.y = random.randint(50,self.z-1)

            elif self.op == '-':
                self.x = random.randint(70,100)
                self.y = random.randint(50,self.x-1)
                self.z = random.randint(50,self.x-1)

            elif self.op == '*':
                self.z = random.randint(50,90)
                self.x = random.randint(10, self.z - 1)
                self.y = random.randint(10, self.z - 1)
                
                if self.choice_lost_num == 1:
                    self.y = random.randint(2,5)
                    while(self.isPrime(self.z)):
                        self.z = random.randint(50,90)
                    while(self.z % self.y != 0):
                        self.y +=  1
                elif self.choice_lost_num == 2:
                    self.x = random.randint(2,5)
                    while(self.isPrime(self.z)):
                        self.z = random.randint(50,90)
                    while(self.z % self.x != 0):
                        self.x += 1

            else:
                self.z = random.randint(50,90)
                self.x = random.randint(10, self.z - 1)
                self.y = random.randint(10, self.z - 1)
                
                if self.choice_lost_num == 2:
                    self.z = random.randint(2, 5)
                    while(self.isPrime(self.x)):
                        self.x = random.randint(50,90)
                    while self.x % self.z != 0:
                        self.z += 1
                elif self.choice_lost_num == 3:
                    self.y = random.randint(2, 5)
                    while(self.isPrime(self.x)):
                        self.x = random.randint(50,90)
                    while self.x % self.y != 0:
                        self.y += 1
                    

    def isPrime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
        

    def drawQuestion(self):
        
        if self.choice_lost_num == 1:

            self.drawText("___", 200, 100, 65, self.white)

            self.drawText(str(self.op), 300, 100, 65, self.white)
            
            self.drawText(str(self.y), 400, 100, 65, self.white)
            
            self.drawText(" = ", 500, 100, 65, self.white)

            self.drawText(str(self.z), 600, 100, 65, self.white)

        elif self.choice_lost_num == 2:
            
            self.drawText(str(self.x), 200, 100, 65, self.white)
            
            self.drawText(str(self.op), 300, 100, 65, self.white)

            self.drawText("___", 400, 100, 65, self.white)

            self.drawText(" = ", 500, 100, 65, self.white)

            self.drawText(str(self.z), 600, 100, 65, self.white)
            
            
        elif self.choice_lost_num == 3:
            
            self.drawText(str(self.x), 200, 100, 65, self.white)

            self.drawText(str(self.op), 300, 100, 65, self.white)
            
            self.drawText(str(self.y), 400, 100, 65, self.white)

            self.drawText(" = ", 500, 100, 65, self.white)

            self.drawText("___", 600, 100, 65, self.white)


    def drawAnswer(self):

        Q = Calculate(self.x, self.y, self.z, self.choice_lost_num, self.op)
        
        if self.place == 1:
            self.chooseAnwser(str(Q.result()), 100, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 1)
            self.chooseAnwser(str(Q.result()+self.random_num), 600, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()-self.random_num), 100, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()+self.random_num+2), 600, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
        elif self.place == 2:
            self.chooseAnwser(str(Q.result()-self.random_num), 100, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()), 600, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 1)
            self.chooseAnwser(str(Q.result()+self.random_num+4), 100, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()+self.random_num), 600, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
        elif self.place == 3:
            self.chooseAnwser(str(Q.result()+self.random_num+1), 100, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()-self.random_num), 600, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()), 100, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 1)
            self.chooseAnwser(str(Q.result()+self.random_num), 600, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
        else:
            self.chooseAnwser(str(Q.result()+self.random_num), 100, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()-self.random_num), 600, 350, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()+self.random_num+10), 100, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 0)
            self.chooseAnwser(str(Q.result()), 600, 500, 100, 75, self.steelblue1, self.steelblue3, 45, 1)
            
            

    def countTime(self):
        x_increase = (self.windowWidth/self.time_answer)/60
        self.x_time += x_increase
        pygame.draw.rect(self.gameDisplay, self.dark_red2, (0,590,self.x_time,10))
        
        if self.x_time >= self.windowWidth:
            self.textTimeUp()
        pygame.display.update()
        

    def checkAnswer(self):
        if self.check == 1:
            self.textRight()
            self.createValue()
            self.check = -1
            self.x_time = 0

        elif self.check == 0:
            self.textWrong()
        

    def textRight(self):
        self.drawText("Right", self.windowWidth/2, self.windowHeight/2, 65, self.white)
        pygame.display.update()
        time.sleep(0.75)
        

    def textWrong(self):
        self.drawText("Wrong", self.windowWidth/2, self.windowHeight/2, 65, self.white)
        pygame.display.update()
        time.sleep(0.75)
        self.gameQuit()
        

    def textTimeUp(self):
        self.drawText("Time's up", self.windowWidth/2, self.windowHeight/2, 65, self.white)
        pygame.display.update()
        time.sleep(0.75)
        self.gameQuit()


    def gameQuit(self):
        pygame.quit()
        quit()
        
            
    def drawText(self, text, x, y, size, color):
        largeText = pygame.font.Font('FreeSansBold.ttf',size)
        TextSurf, TextRect = self.textObj(text, largeText, color)
        TextRect.center = ((x, y))
        self.gameDisplay.blit(TextSurf, TextRect)
        

    def chooseAnwser(self, msg, x, y, w, h, orc, irc, sizeMsg, check_number):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, irc,(x,y,w,h))
            
            if click[0] == 1:
                self.check = check_number;
        else:
             pygame.draw.rect(self.gameDisplay, orc,(x,y,w,h))
             
        smallText = pygame.font.Font("FreeSansBold.ttf",sizeMsg)
        textSurf, textRect = self.textObj(msg, smallText, self.black)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(textSurf, textRect)


    def choice(self, msg, x, y, w, h, orc, irc, sizeMsg, num):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, irc,(x,y,w,h))
            
            if click[0] == 1:
                self.level = num;
        else:
             pygame.draw.rect(self.gameDisplay, orc,(x,y,w,h))
             
        smallText = pygame.font.Font("FreeSansBold.ttf",sizeMsg)
        textSurf, textRect = self.textObj(msg, smallText, self.black)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(textSurf, textRect)

        
            
    def button(self, msg, x, y, w, h, orc, irc, sizeMsg, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, irc,(x,y,w,h))
            
            if click[0] == 1 and action != None:
                action()
        else:
             pygame.draw.rect(self.gameDisplay, orc,(x,y,w,h))
             
        smallText = pygame.font.Font("FreeSansBold.ttf",sizeMsg)
        textSurf, textRect = self.textObj(msg, smallText, self.black)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(textSurf, textRect)


    def textObj(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()    

    
class Calculate:
    
    x = 0
    y = 0
    z = 0
    choice_lost_num = 0
    op = None

    def __init__(self, x, y, z, choice_lost_num, op):
        self.x = x
        self.y = y
        self.z = z
        self.choice_lost_num = choice_lost_num
        self.op = op


    def result(self):
        if self.op == '+':
            return self.sum()
        elif self.op == '-':
            return self.sub()
        elif self.op == '*':
            return self.mul()
        else:
            return self.div()
        

    def sum(self):
        if self.choice_lost_num == 1:
            return self.find_x(self.y, self.z, '+')
        elif self.choice_lost_num == 2:
            return self.find_y(self.x, self.z, '+')
        else:
            return self.find_z(self.x, self.y, '+')


    def sub(self):
        if self.choice_lost_num == 1:
            return self.find_x(self.y, self.z, '-')
        elif self.choice_lost_num == 2:
            return self.find_y(self.x, self.z, '-')
        else:
            return self.find_z(self.x, self.y, '-')


    def mul(self):
        if self.choice_lost_num == 1:
            return self.find_x(self.y, self.z, '*')
        elif self.choice_lost_num == 2:
            return self.find_y(self.x, self.z, '*')
        else:
            return self.find_z(self.x, self.y, '*')
            
                
    def div(self):
        if self.choice_lost_num == 1:
            return self.find_x(self.y, self.z, '/')
        elif self.choice_lost_num == 2:
            return self.find_y(self.x, self.z, '/')
        else:
            return self.find_z(self.x, self.y, '/')

            
    def find_x(self, y, z, op):
        self.x = 1
        if(op == '+'):
            self.x = z - y
            return self.x
        elif(op == '-'):
            self.x = z + y
            return self.x
        elif(op == '*'):
            while self.x * y != z:
                self.x += 1
            return self.x
        else:
            self.x = z * y
            return self.x


    def find_y(self, x, z, op):
        self.y = 1
        if(op == '+'):
            self.y = z - x
            return self.y
        elif(op == '-'):
            self.y = x - z
            return self.y
        elif(op == '*'):
            while x * self.y != z:
                self.y += 1
            return self.y
        else:
            while x / self.y != z:
                self.y += 1
            return self.y


    def find_z(self, x, y, op):
        self.z = 1
        if(op == '+'):
            self.z = x + y
            return self.z
        elif(op == '-'):
            self.z = x - y
            return self.z
        elif(op == '*'):
            self.z = x * y
            return self.z
        else:
            while x / y != self.z:
                self.z += 1
            return self.z



def start():
    theGame = Game()
    theGame.runGame()
    
if __name__ == "__main__":
    start()
