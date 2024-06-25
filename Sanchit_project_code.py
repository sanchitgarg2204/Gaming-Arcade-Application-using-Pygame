import csv
import pygame
import sys
import random
from math import *
from pygame import mixer
import time
import mysql.connector as msql
from datetime import datetime
import os.path

if os.path.exists('scores.csv'):
    pass
else:
    f=open("scores.csv","a",newline='')
    swriter=csv.writer(f)
    swriter.writerow(["DodgeBall:","Stack:" ,"BalloonShooter:"])
    swriter.writerow([0,0,0])
    swriter.writerow([0,0,0])
    swriter.writerow([0,0,0])
    swriter.writerow([0,0,0])
    swriter.writerow([0,0,0])
    f.close()

try:
    cn=msql.connect(host='localhost',user='root',passwd='sansah22',database='Medal_Of_Honor')
    cur=cn.cursor()
except:
    cn=msql.connect(host='localhost',user='root',passwd='sansah22')
    cur=cn.cursor()
    cur.execute("Create database Medal_Of_Honor")
    cur.execute("Use Medal_Of_Honor")
    cur.execute("Create table UserInfo (UserName varchar(20), DateOfJoining date, UserId varchar(10), Password varchar(10), CoinsLeft int, SecurityPin varchar(4),DodgeScore int, StackScore int, BalloonScore int, AlreadyAdded date)")

pygame.init()
mixer.init()
mixer.music.load("paradise.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()
image=pygame.image.load("duck.jpg")
image_small=pygame.transform.scale(image,(50,50))
width = 750
height = 690

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("MEDAL OF HONOR")
clock = pygame.time.Clock()


playerColor = (249, 231, 159)

red = (203, 67, 53)
yellow = (241, 196, 15)
blue = (46, 134, 193)
green = (34, 153, 84)
purple = (136, 78, 160)
orange = (214, 137, 16)
white=(230,230,230)
colors = [red, yellow, blue, green, purple, orange]
# Color Codes
color = [(120, 40, 31), (148, 49, 38), (176, 58, 46), (203, 67, 53), (231, 76, 60), (236, 112, 99),
         (241, 148, 138), (245, 183, 177), (250, 219, 216), (253, 237, 236),
(254, 249, 231), (252, 243, 207), (249, 231, 159), (247, 220, 111), (244, 208, 63), (241, 196, 15), (212, 172, 13)
         , (183, 149, 11), (154, 125, 10), (125, 102, 8),
         (126, 81, 9), (156, 100, 12), (185, 119, 14), (202, 111, 30), (214, 137, 16), (243, 156, 18), (245, 176, 65), 
         (248, 196, 113),(250, 215, 160), (253, 235, 208), (254, 245, 231),(232, 246, 243), (162, 217, 206), (162, 217, 206),
         (115, 198, 182), (69, 179, 157), (22, 160, 133),
         (19, 141, 117), (17, 122, 101), (14, 102, 85),
         (11, 83, 69),
         (21, 67, 96), (26, 82, 118), (31, 97, 141),
        (36, 113, 163), (41, 128, 185), (84, 153, 199),
        (127, 179, 213), (169, 204, 227), (212, 230, 241),
        (234, 242, 248),
         (251, 238, 230), (246, 221, 204), (237, 187, 153),
         (229, 152, 102), (220, 118, 51), (211, 84, 0),
         (186, 74, 0), (160, 64, 0), (135, 54, 0),
         (110, 44, 0)
         ]

colorIndex = 0

brickH = 35
brickW = 400

score = 0
speed = 5
#making buttons
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#HomeScreen

def redrawWindow1():
    font = pygame.font.SysFont("Agency FB", 50)
    text1 = font.render("WELCOME TO MEDAL OF HONOR!", True,red)
    display.fill(background)
    display.blit(text1, (width/2-235, height/2 - 275))
    login.draw(display,(0,0,0))
    register.draw(display,(0,0,0))
    hscores.draw(display,(0,0,0))
    exitButton2.draw(display,(0,0,0))
    
    

#main window
def redrawWindow():
    global name
    global Uid
    t="HI "+ name + " !"
    state=("select * from userinfo where UserId = '{}'".format(Uid))
    cur.execute(state)
    data=cur.fetchall()
    coins="Coins Left: "+str(data[0][4])
    font = pygame.font.SysFont("Agency FB", 50)
    text1 = font.render(t,True,red)
    text2 = font.render("WELCOME TO MEDAL OF HONOR!", True,red)
    text3 = font.render(coins,True,red)
    display.fill(background)
    display.blit(text1, (width/2-100, height/2 - 350))
    display.blit(text2, (width/2-235, height/2 - 280))
    display.blit(text3, (width/2+100, height/2 - 345))
    playdodge.draw(display,(0,0,0))
    playStack.draw(display,(0,0,0))
    playBalloon.draw(display,(0,0,0))
    playPong.draw(display,(0,0,0))
    exitButton.draw(display,(0,0,0))
    myhscores.draw(display,(0,0,0))
    signout.draw(display,(0,0,0))
    money.draw(display,(0,0,0))

def Login():
    global Uid
    global data
    Uid=getdata("UserId:")
    Pwd=getdata("Password:")
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    
    global name
    
    
    if len(data)==0:
        font = pygame.font.Font(None, 45)        
        error1 = pygame.display.set_mode((750,750))
        pygame.display.set_caption("ERROR")
        text1=font.render("ERROR!", True,blue)
        text2=font.render("INVALID USERID", True,blue)
        running = True
        
        while running:
            error1.fill(background)
            back.draw(display,(0,0,0))
            error1.blit(text1,(200,250))
            error1.blit(text2,(200,350))
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    running = False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if back.isOver(pos):
                        main()
                if event.type==pygame.MOUSEMOTION:
                    if back.isOver(pos):
                        back.color=white
                    else:
                        back.color=blue
                pygame.display.update()
    else:
        if data[0][3]!=Pwd:
            font = pygame.font.Font(None, 45)        
            error2 = pygame.display.set_mode((750,750))
            pygame.display.set_caption("ERROR")
            text1=font.render("ERROR!", True,blue)
            text2=font.render("INCORRECT PASSWORD", True,blue)
            running = True
        
            while running:
                error2.fill(background)
                back.draw(display,(0,0,0))
                error2.blit(text1,(200,250))
                error2.blit(text2,(200,350))
                for event in pygame.event.get():
                    pos=pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if back.isOver(pos):
                            main()
                    if event.type==pygame.MOUSEMOTION:
                        if back.isOver(pos):
                            back.color=white
                        else:
                            back.color=blue
                    pygame.display.update()
        else:
            name=data[0][0]
            start()
            
    
def Register():
    Uname=getdata("Username:")
    Uid=getdata("UserId:")
    Pwd=getdata("Password:")
    Pin=getdata("Security Pin:")
    state="select current_date"
    cur.execute(state)
    Doj=cur.fetchall()[0][0]
    state="Insert into userinfo values(%s,%s,%s,%s, %s,%s,%s, %s,%s,%s)"
    val=(Uname,Doj,Uid,Pwd,100,Pin,0,0,0,Doj)
    cur.execute(state,val)
    cn.commit()

def getdata(heading):
    font = pygame.font.Font(None,40)
    text1=font.render(heading, True,blue)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(370, 300, 140, 32)
    
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    done = False
    t=''
    
    while not done:
        display.fill(background)

        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if input_box.collidepoint(event.pos):

                    active = not active
                else:
                    active = False
               
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        t=text
                        return(t)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.QUIT:
                close()

         
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        display.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(display, color, input_box, 2)
        display.blit(text1,(150, 300))

        pygame.display.flip()
        clock.tick(30)
    
def highscores():
    f=open("scores.csv","r",newline='')
    sreader=csv.reader(f)
    l=[]
    for row in sreader:
        l.append(row)
    f.close()
    font = pygame.font.Font(None, 32)        
    scoretable = pygame.display.set_mode((750,750))
    pygame.display.set_caption("HIGHSCORES")
    
    text1=font.render("DODGE BALL: ", True,red)
    text2=font.render("STACK: ", True,red)
    text3=font.render("BALLOON SHOOTER: ", True,red)

    text=font.render("HIGH SCORES ", True,red)

    

    
    running = True
    
    while running:            
        
        scoretable.fill(background)
        
        
        
        y=140
        for i in range(1,len (l)):
            
            str1=l[i][0]
            text4=font.render(str1, True,orange)
            scoretable.blit(text4, (20,y))
            y+=20
        y=290
        for i in range(1,len (l)):
            
            str1=l[i][1]
            text4=font.render(str1, True,orange)
            scoretable.blit(text4, (280,y))
            y+=20
        y=440
        for i in range(1,len (l)):
            
            str1=l[i][2]
            text4=font.render(str1, True,orange)
            scoretable.blit(text4, (450,y))
            y+=20
            
            
            
        
        scoretable.blit(text, (300,10))
        scoretable.blit(text1, (20,100))
        scoretable.blit(text2, (280,250))
        scoretable.blit(text3, (450,400))
        
        
        back.draw(display,(0,0,0))
        
            
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back.isOver(pos):
                    main()
            if event.type==pygame.MOUSEMOTION:
                if back.isOver(pos):
                    back.color=white
                else:
                    back.color=blue
            pygame.display.update()


def myhighscores():
    
    
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()

    font = pygame.font.Font(None, 32)        
    scoretable2 = pygame.display.set_mode((750,750))
    pygame.display.set_caption("MY HIGHSCORES")
    text=font.render("MY HIGH SCORES", True,red)
    bestscores=[]
    names=["DodgeBall: ","Stack: ","Baloon Shooter: "]
    for i in range(6,9):
        str1=str(data[0][i])
        bestscores.append(str1)
    running = True
        
    while running:            
        
        scoretable2.fill(background)
        y=250
        for i in range(0,3):
            
            text1=font.render((names[i]+bestscores[i]), True,orange)
            scoretable2.blit(text1,(20,y))
            y+=100
        scoretable2.blit(text, (300,150))
        back.draw(display,(0,0,0))
        
            
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back.isOver(pos):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if back.isOver(pos):
                    back.color=white
                else:
                    back.color=blue
            pygame.display.update()

def addmoney():
    global Uid
    font = pygame.font.Font(None, 45) 
    bank = pygame.display.set_mode((750,750))
    pygame.display.set_caption("BANK")
    text1=font.render("WELCOME TO MOH BANK!", True,blue)
    text2=font.render("CLICK HERE TO PROCEED:", True,blue)
    
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    text3=font.render(("CURRENT BALANCE: "+str(data[0][4])), True,blue)
    
    running = True
        
    while running:
        
        
        bank.fill(background)
        bank.blit(text1,(200,250))
        bank.blit(text2,(200,350))
        bank.blit(text3,(200,450))
        next1.draw(display,(0,0,0))
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if next1.isOver(pos):
                    check()
            if event.type==pygame.MOUSEMOTION:
                if next1.isOver(pos):
                    next1.color=white
                else:
                    next1.color=blue
            pygame.display.update()

def check():
    global Uid
    font = pygame.font.Font(None, 45)
    
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    
    str1=''
    state="select current_date"
    cur.execute(state)
    today=cur.fetchall()[0][0]
    if data[0][9]!=today:
        Spin=getdata("Security Pin:")
        if Spin==data[0][5]:
            
            state="update userinfo set CoinsLeft = {} where UserId='{}'".format((int(data[0][4])+100),Uid)
            cur.execute(state)
            cn.commit()
            
            state1="update userinfo set AlreadyAdded = current_date where UserId='{}'".format(Uid)
            cur.execute(state1)
            cn.commit()
            str1="Transaction Successful! 100 coins added!"

            state="select * from userinfo where UserId = '{}'".format(Uid)
            cur.execute(state)
            data=cur.fetchall()
            
        else:
            str1="Incorrect Pin!"

    else:
        str1="You have reached the maximum limit for today!"

   
    bank = pygame.display.set_mode((750,750))
    pygame.display.set_caption("BANK")
    text=font.render(str1, True,blue)
    running = True
    while running:
        bank.fill(background)
        bank.blit(text,(10,250))
        next2.draw(display,(0,0,0))
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if next2.isOver(pos):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if next2.isOver(pos):
                    next2.color=white
                else:
                    next2.color=blue
            pygame.display.update()
def start():
    
    run=True
    while run:
        redrawWindow()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if playdodge.isOver(pos):
                    dgameintro()
                if playStack.isOver(pos):
                    sgameintro()
                if playBalloon.isOver(pos):
                    bgameintro()
                if playPong.isOver(pos):
                    pgameintro()
                if exitButton.isOver(pos):
                    close()
                if myhscores.isOver(pos):
                    myhighscores()
                if signout.isOver(pos):
                    main()
                if money.isOver(pos):
                    addmoney()
                
            if event.type==pygame.MOUSEMOTION:
                if playdodge.isOver(pos):
                    playdodge.color=white
                else:
                    playdodge.color=blue
                if playStack.isOver(pos):
                    playStack.color=white
                else:
                    playStack.color=blue
                if playBalloon.isOver(pos):
                    playBalloon.color=white
                else:
                    playBalloon.color=blue
                if playPong.isOver(pos):
                    playPong.color=white
                else:
                    playPong.color=blue
                if exitButton.isOver(pos):
                    exitButton.color=white
                else:
                    exitButton.color=blue
                if myhscores.isOver(pos):
                    myhscores.color=white
                else:
                    myhscores.color=blue
                if signout.isOver(pos):
                    signout.color=white
                else:
                    signout.color=blue
                if money.isOver(pos):
                    money.color=white
                else:
                    money.color=blue
        pygame.display.update()
        
    
#dodgeball game code
class Ball:
    def __init__(self, radius, speed):
        self.r=radius
        self.x = width/2 - self.r
        self.y = height/2 - self.r
        self.color = random.choice(colors)
        self.angle = random.randint(-180, 180)
        self.speed=speed
    
    
    def move(self):
        self.x += self.speed*cos(radians(self.angle))
        self.y += self.speed*sin(radians(self.angle))

        if self.x < self.r or self.x + self.r > width:
            self.angle = 180 - self.angle
        if self.y < self.r or self.y + self.r > height:
            self.angle *= -1

    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

    def collision(self, radius):
        pos = pygame.mouse.get_pos()

        dist = ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5

        if dist <= self.r + radius:
            dgameOver()

class Target:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = self.w

    def generateNewCoord(self):
        self.x = random.randint(self.w, width - self.w)
        self.y = random.randint(self.h, height - self.h)

    def draw(self):
        color = random.choice(colors)

        pygame.draw.rect(display, color, (self.x, self.y, self.w, self.h))

    
def dgameOver():
    loop = True
    
    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Over!", True, (230, 230, 230))
    global new
    
    global Uid
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    old=data[0][6]
    if new>old:
        state="update userinfo set DodgeScore={} where UserID='{}'".format(new,Uid)
        cur.execute(state)
        cn.commit()
    f=open("scores.csv","r",newline='')
    sreader=csv.reader(f)
    l1=[]
    pos=0
    for row in sreader:
        l1.append(row)
                
    f.close()
    
    
    l2=[]
    for i in range(1,len(l1)):
        l2.append(l1[i][0])
    s=str(new)+" : " +name
    
    if s not in l2:        
        l2.append(s)
    for i in range(0,len(l2)):
        for j in range(0,len(l2)-1-i):
            if int(l2[j].split()[0])<int(l2[j+1].split()[0]):
               l2[j],l2[j+1]=l2[j+1],l2[j]

    if len(l2)>5:
        l2.pop()
    
    t=0
    for i in range(1,len(l1)):
        l1[i][pos]=str(l2[t])
        t+=1
    
        
    f=open("scores.csv","w",newline='')
    swriter=csv.writer(f)
    swriter.writerows(l1)
    f.close()
    
    
    while loop:
        display.fill(background)
        restartButton.draw(display,(0,0,0))
        quitButton.draw(display,(0,0,0))
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if restartButton.isOver(pos1):
                    dgameLoop()
                if quitButton.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if restartButton.isOver(pos1):
                    restartButton.color=(230,230,230)
                else:
                    restartButton.color=blue
                if quitButton.isOver(pos1):
                    quitButton.color=(230,230,230)
                else:
                    quitButton.color=blue  

        if score>15 and score<=20:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+5),Uid))
            cn.commit()
        elif score>20:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+15),Uid))
            cn.commit()

        display.blit(text, (width/2-200, height/2 - 100))
        displayScore()
        
        
        
        pygame.display.update()
        clock.tick()
    
    
        
        
    
       

def checkCollision(target, d, objTarget):
    pos = pygame.mouse.get_pos()
    dist = ((pos[0] - target[0] - objTarget.w)**2 + (pos[1] - target[1]  - objTarget.h)**2)**0.5

    if dist <= d + objTarget.w:
        return True
    return False


def drawPlayerPointer(pos, r):
    pygame.draw.ellipse(display, playerColor, (pos[0] - r, pos[1] - r, 2*r, 2*r))


def close():
    pygame.quit()
    sys.exit()

def displayScore():
    font = pygame.font.SysFont("Forte", 30)
    scoreText = font.render("Score: " + str(score), True, (230, 230, 230))
    display.blit(scoreText, (10, 10))
    
    global new
    new=score
    
def dgameintro():
    font = pygame.font.SysFont("Forte", 30)
    text1=font.render("WELCOME TO DODGE BALL!",True,(230,230,230))
    text2=font.render("INTRUCTIONS:",True,(230,230,230))
    text3=font.render("Move the cursor/white ball around the screen and dodge the coloured ones.",True,(230,230,230))
    text4=font.render("Collect the squares to increase the points",True,(230,230,230))
    text5=font.render("If the cursor collides with the coloured balls",True,(230,230,230))
    text6=font.render("The GAME is OVER!",True,(230,230,230))
    text7=font.render("Cost = 10 coins",True,(230,230,230))
    text8=font.render("Reward = 5 coins(>15) 15 coins(>20)",True,(230,230,230))
    loop=True
    while loop:
        display.fill(background)
        start1.draw(display,(0,0,0))
        back.draw(display,(0,0,0))
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start1.isOver(pos1):
                    dgameLoop()
                if back.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if start1.isOver(pos1):
                    start1.color=(230,230,230)
                else:
                    start1.color=blue
                if back.isOver(pos1):
                    back.color=(230,230,230)
                else:
                    back.color=blue  

        

        display.blit(text1,(200,100))
        display.blit(text2,(200,150))
        display.blit(text3,(10,300))
        display.blit(text4,(10,320))
        display.blit(text5,(10,340))
        display.blit(text6,(10,360))
        display.blit(text7,(10,380))
        display.blit(text8,(10,400))
        
        pygame.display.update()
        
    

def dgameLoop():
    global score
    global Uid
    score=0
    
    loop = True

    pRadius = 10

    balls = []
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    font = pygame.font.SysFont("Forte", 30)
    if int(data[0][4])<10:
        text1=font.render("INSUFFICIENT BALANCE!",True,(230,230,230))
        loop=True
        while loop:
            display.fill(background)
            money2.draw(display,(0,0,0))
            back.draw(display,(0,0,0))
            pos1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if money2.isOver(pos1):
                        addmoney()
                    if back.isOver(pos1):
                        start()
                if event.type==pygame.MOUSEMOTION:
                    if money2.isOver(pos1):
                        money2.color=(230,230,230)
                    else:
                        money2.color=blue
                    if back.isOver(pos1):
                        back.color=(230,230,230)
                    else:
                        back.color=blue  
                display.blit(text1,(200,100))
                pygame.display.update()
        
    else:
        cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])-10),Uid))
        cn.commit()
            
                        
    for i in range(1):
        newBall = Ball(pRadius + 2,9)
    
        balls.append(newBall)

    target = Target()
    target.generateNewCoord()
    loop=True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
        display.fill(background)

        for i in range(len(balls)):
            balls[i].move()
            
        for i in range(len(balls)):
            balls[i].draw()
            
        for i in range(len(balls)):
            balls[i].collision(pRadius)

        playerPos = pygame.mouse.get_pos()
        drawPlayerPointer((playerPos[0], playerPos[1]), pRadius)

        collide = checkCollision((target.x, target.y), pRadius, target)
        
        if collide:
            score += 1
            target.generateNewCoord()
        elif score == 2 and len(balls) == 1:
            newBall = Ball(pRadius + 2, 13)
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 5 and len(balls) == 2:
            newBall = Ball(pRadius + 2, 14)
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 10 and len(balls) == 3:
            newBall = Ball(pRadius + 2, 15)
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 15 and len(balls) == 4:
            newBall = Ball(pRadius + 2, 16)
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 20 and len(balls) == 5:
            newBall = Ball(pRadius + 2, 18)
            balls.append(newBall)
            target.generateNewCoord()

        target.draw()
        displayScore()
        
        pygame.display.update()
        clock.tick(65)

# Single Brick Class
class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1


# Complete Stack
class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 25
        for i in range(self.initSize):
            newBrick = Brick(width/2 - brickW/2, height - (i + 1)*brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0
        
        y = self.peek().y
        if score > 50:
            speed += 0
        elif score%5 == 0:
            speed += 1
        
        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)
        
    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self):
        global brickW, score
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
        else:
            sgameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH

        brickW = self.stack[self.initSize - 1].w

# Game Over
def sgameOver():
    loop = True
    i=0
    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Over!", True, (230, 230, 230))

    global new
    global Uid
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    old=data[0][7]
    if new>old:
        state="update userinfo set StackScore={} where UserID='{}'".format(new,Uid)
        cur.execute(state)
        cn.commit()
    
    
    f=open("scores.csv","r",newline='')
    sreader=csv.reader(f)
    l1=[]
    pos=0
    for row in sreader:
        l1.append(row)
                
    f.close()


    l2=[]
    for i in range(1,len(l1)):
        l2.append(l1[i][1])
    s=str(new)+" : " +name
    
    if s not in l2:        
        l2.append(s)
    for i in range(0,len(l2)):
        for j in range(0,len(l2)-1-i):
            if int(l2[j].split()[0])<int(l2[j+1].split()[0]):
               l2[j],l2[j+1]=l2[j+1],l2[j]

    if len(l2)>5:
        l2.pop()
    
    t=0
    for i in range(1,len(l1)):
        l1[i][1]=str(l2[t])
        t+=1

        
    f=open("scores.csv","w",newline='')
    swriter=csv.writer(f)
    swriter.writerows(l1)
    f.close()

    
    while loop:
        display.fill(background)
        restartButton.draw(display,(0,0,0))
        quitButton.draw(display,(0,0,0))
        display.blit(text, (width/2-200, height/2 - 100))
        displayScore()
        if(score==0):
            
            display.blit(image_small,(i,125))
            i+=1
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if restartButton.isOver(pos1):
                    sgameLoop()
                if quitButton.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if restartButton.isOver(pos1):
                    restartButton.color=(230,230,230)
                else:
                    restartButton.color=blue
                if quitButton.isOver(pos1):
                    quitButton.color=(230,230,230)
                else:
                    quitButton.color=blue  

        if score>10 and score<=15:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+5),Uid))
            cn.commit()
        elif score>15:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+15),Uid))
            cn.commit()
        
        pygame.display.update()
        clock.tick()
    

def sgameintro():
    font = pygame.font.SysFont("Forte", 30)
    text1=font.render("WELCOME TO STACK!",True,(230,230,230))
    text2=font.render("INTRUCTIONS:",True,(230,230,230))
    text3=font.render("Keep stacking the tiles by placing them exactly on top of each other",True,(230,230,230))
    text4=font.render("Width of tiles keeps reducing as you place the tiles incorrectly",True,(230,230,230))
    text5=font.render("If you miss a tile entirely",True,(230,230,230))
    text6=font.render("The GAME is OVER!",True,(230,230,230))
    text7=font.render("Cost = 10 coins",True,(230,230,230))
    text8=font.render("Reward = 5 coins(>10) 15 coins(>15)",True,(230,230,230))
    loop=True
    while loop:
        display.fill(background)
        start1.draw(display,(0,0,0))
        back.draw(display,(0,0,0))
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start1.isOver(pos1):
                    sgameLoop()
                if back.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if start1.isOver(pos1):
                    start1.color=(230,230,230)
                else:
                    start1.color=blue
                if back.isOver(pos1):
                    back.color=(230,230,230)
                else:
                    back.color=blue  

        

        display.blit(text1,(200,100))
        display.blit(text2,(200,150))
        display.blit(text3,(10,300))
        display.blit(text4,(10,320))
        display.blit(text5,(10,340))
        display.blit(text6,(10,360))
        display.blit(text7,(10,380))
        display.blit(text8,(10,400))
        
        pygame.display.update()

# The Main Game Loop for stack
def sgameLoop():
    global brickW, brickH, score, colorIndex, speed
    loop = True

    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    font = pygame.font.SysFont("Forte", 30)
    if int(data[0][4])<10:
        text1=font.render("INSUFFICIENT BALANCE!",True,(230,230,230))
        loop=True
        while loop:
            display.fill(background)
            money2.draw(display,(0,0,0))
            back.draw(display,(0,0,0))
            pos1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if money2.isOver(pos1):
                        addmoney()
                    if back.isOver(pos1):
                        start()
                if event.type==pygame.MOUSEMOTION:
                    if money2.isOver(pos1):
                        money2.color=(230,230,230)
                    else:
                        money2.color=blue
                    if back.isOver(pos1):
                        back.color=(230,230,230)
                    else:
                        back.color=blue  
                display.blit(text1,(200,100))
                pygame.display.update()
        
    else:
        cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])-10),Uid))
        cn.commit()
    brickH = 12
    brickW = 175
    colorIndex = 0
    speed = 3
    
    score = 0

    stack = Stack()
    stack.addNewBrick()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                stack.pushToStack()
                stack.addNewBrick()
                

        display.fill(background)

        stack.move()
        stack.show()

        displayScore()
        
        pygame.display.update()
        clock.tick(70)



margin = 100
lowerBound = 100

score = 0

# Colors
white = (230, 230, 230)
lightBlue = (174, 214, 241)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (21, 67, 96)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

font = pygame.font.SysFont("Snap ITC", 25)

# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        font = pygame.font.SysFont("Agency FB", 25)
        text1 = font.render(timer, True,white)
        display.blit(text1,(width/2+50,height/2-100))
        time.sleep(1)
        t -= 1
      
    #bgameOver()
  
# Balloon Class
class Balloon:
    def __init__(self, speed):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])

    # Move balloon around the Screen
    def move(self):
        direct = random.choice(self.probPool)

        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10

        self.y += self.speed*sin(radians(self.angle))
        self.x += self.speed*cos(radians(self.angle))

        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height/5:
                self.x -= self.speed*cos(radians(self.angle)) 
            else:
                self.reset()
        if self.y + self.b < 0 or self.y > height + 30:
            self.reset()

    # Show/Draw the balloon  
    def show(self):
        pygame.draw.line(display, darkBlue, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(display, self.color, (self.x + self.a/2 - 5, self.y + self.b - 3, 10, 10))

    # Check if Balloon is bursted
    def burst(self):
        global bscore
        pos = pygame.mouse.get_pos()

        if onBalloon(self.x, self.y, self.a, self.b, pos):
            bscore += 1
            self.reset()

    # Reset the Balloon
    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound 
        self.angle = 90
        self.speed -= 0.002
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])

balloons = []
noBalloon = 10
for i in range(noBalloon):
    obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
    balloons.append(obj)

def onBalloon(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False

# show the location of Mouse
def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = lightGreen
    for i in range(noBalloon):
        if onBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
            color = red
    pygame.draw.ellipse(display, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4)

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))

def showScore():
    scoreText = font.render("Balloons Bursted : " + str(bscore), True, white)
    display.blit(scoreText, (150, height - lowerBound + 50))
    global new
    new=bscore

def bgameintro():
    font = pygame.font.SysFont("Forte", 30)
    text1=font.render("WELCOME TO BALLOON SHOOTER!",True,(230,230,230))
    text2=font.render("INTRUCTIONS:",True,(230,230,230))
    text3=font.render("Move the cursor around the screen and click on the balloons.",True,(230,230,230))
    text4=font.render("There is a timer of 30 seconds.",True,(230,230,230))
    text5=font.render("Shoot as many balloons as you can.",True,(230,230,230))
    text6=font.render("Cost = 10 coins",True,(230,230,230))
    text7=font.render("Reward = 5 coins(>15) 15 coins(>20)",True,(230,230,230))
    loop=True
    while loop:
        display.fill(background)
        start1.draw(display,(0,0,0))
        back.draw(display,(0,0,0))
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start1.isOver(pos1):
                    bgame()
                if back.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if start1.isOver(pos1):
                    start1.color=(230,230,230)
                else:
                    start1.color=blue
                if back.isOver(pos1):
                    back.color=(230,230,230)
                else:
                    back.color=blue  

        

        display.blit(text1,(200,100))
        display.blit(text2,(200,150))
        display.blit(text3,(10,300))
        display.blit(text4,(10,320))
        display.blit(text5,(10,340))
        display.blit(text6,(10,360))
        display.blit(text7,(10,380))
        
        pygame.display.update()
        
def bgame():
    global bscore
    global Uid
    bscore=0
    loop = True
    clock = pygame.time.Clock()

    counter, text = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 50)

    if int(data[0][4])<10:
        text1=font.render("INSUFFICIENT BALANCE!",True,(230,230,230))
        loop=True
        while loop:
            display.fill(background)
            money2.draw(display,(0,0,0))
            back.draw(display,(0,0,0))
            pos1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if money2.isOver(pos1):
                        addmoney()
                    if back.isOver(pos1):
                        start()
                if event.type==pygame.MOUSEMOTION:
                    if money2.isOver(pos1):
                        money2.color=(230,230,230)
                    else:
                        money2.color=blue
                    if back.isOver(pos1):
                        back.color=(230,230,230)
                    else:
                        back.color=blue  
                display.blit(text1,(200,100))
                pygame.display.update()
        
    else:
        cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])-10),Uid))
        cn.commit()
            
    loop=True    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'time up!'
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noBalloon):
                    balloons[i].burst()

        display.fill(lightBlue)
        
        for i in range(noBalloon):
            balloons[i].show()

        pointer()
        
        for i in range(noBalloon):
            balloons[i].move()

        display.blit(font.render(text, True, (0, 0, 0)), (600,100))
        lowerPlatform()
        showScore()
        if text=='time up!':
            bgameOver()
        pygame.display.update()
        clock.tick(60)

def bgameOver():
    loop = True
    i=0
    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Over!", True, (230, 230, 230))

    global new
    global Uid
    state="select * from userinfo where UserId = '{}'".format(Uid)
    cur.execute(state)
    data=cur.fetchall()
    old=data[0][8]
    if new>old:
        state="update userinfo set  BalloonScore={} where UserID='{}'".format(new,Uid)
        cur.execute(state)
        cn.commit()
    
    
    f=open("scores.csv","r",newline='')
    sreader=csv.reader(f)
    l1=[]
    pos=0
    for row in sreader:
        l1.append(row)
                
    f.close()


    l2=[]
    for i in range(1,len(l1)):
        l2.append(l1[i][2])
    s=str(new)+" : " +name
    
    if s not in l2:        
        l2.append(s)
    for i in range(0,len(l2)):
        for j in range(0,len(l2)-1-i):
            if int(l2[j].split()[0])<int(l2[j+1].split()[0]):
               l2[j],l2[j+1]=l2[j+1],l2[j]

    if len(l2)>5:
        l2.pop()
    
    t=0
    for i in range(1,len(l1)):
        l1[i][2]=str(l2[t])
        t+=1

        
    f=open("scores.csv","w",newline='')
    swriter=csv.writer(f)
    swriter.writerows(l1)
    f.close()

    
    while loop:
        display.fill(background)
        restartButton.draw(display,(0,0,0))
        quitButton.draw(display,(0,0,0))
        display.blit(text, (width/2-200, height/2 - 100))
        showScore()
        
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if restartButton.isOver(pos1):
                    bgame()
                if quitButton.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if restartButton.isOver(pos1):
                    restartButton.color=(230,230,230)
                else:
                    restartButton.color=blue
                if quitButton.isOver(pos1):
                    quitButton.color=(230,230,230)
                else:
                    quitButton.color=blue  

        if new>15 and new<=20:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+5),Uid))
            cn.commit()
        elif new>20:
            cur.execute("update userinfo set CoinsLeft = {} where UserId = '{}'".format((int(data[0][4])+15),Uid))
            cn.commit()
        
        pygame.display.update()
        clock.tick()
    


background = (27, 38, 49)
white = (236, 240, 241)
red = (203, 67, 53)
blue = (52, 152, 219)
yellow = (244, 208, 63)

top = white
bottom = white
left = white
right = white

margin = 4

scoreLeft = 0
scoreRight = 0
maxScore = 10

font = pygame.font.SysFont("Small Fonts", 30)
largeFont = pygame.font.SysFont("Small Fonts", 60)

# Draw the Boundary of Board
def boundary():
    global top, bottom, left, right
    pygame.draw.rect(display, left, (0, 0, margin, height))
    pygame.draw.rect(display, top, (0, 0, width, margin))
    pygame.draw.rect(display, right, (width-margin, 0, margin, height))
    pygame.draw.rect(display, bottom, (0, height - margin, width, margin))

    l = 25
    
    pygame.draw.rect(display, white, (width/2-margin/2, 10, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 60, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 110, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 160, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 210, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 260, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 310, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 360, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 410, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 460, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 510, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 560, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 610, margin, l))
    pygame.draw.rect(display, white, (width/2-margin/2, 660, margin, l))
    
    
# Paddle Class 
class Paddle:
    def __init__(self, position):
        self.w = 10
        self.h = self.w*8
        self.paddleSpeed = 9
            
        if position == -1:
            self.x = 1.5*margin
        else:
            self.x = width - 1.5*margin - self.w
            
        self.y = height/2 - self.h/2

    # Show the Paddle
    def show(self):
        pygame.draw.rect(display, white, (self.x, self.y, self.w, self.h))

    # Move the Paddle
    def move(self, ydir):
        self.y += self.paddleSpeed*ydir
        if self.y < 0:
            self.y -= self.paddleSpeed*ydir
        elif self.y + self.h> height:
            self.y -= self.paddleSpeed*ydir


leftPaddle = Paddle(-1)
rightPaddle = Paddle(1)

# Ball Class
class pBall:
    def __init__(self, color):
        self.r = 20
        self.x = width/2 - self.r/2
        self.y = height/2 -self.r/2
        self.color = color
        self.angle = random.randint(-75, 75)
        if random.randint(0, 1):
            self.angle += 180
        
        self.speed = 10

    # Show the Ball
    def show(self):
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.r, self.r))

    # Move the Ball
    def move(self):
        global scoreLeft, scoreRight
        self.x += self.speed*cos(radians(self.angle))
        self.y += self.speed*sin(radians(self.angle))
        if self.x + self.r > width - margin:
            scoreLeft += 1
            self.angle = 180 - self.angle
        if self.x < margin:
            scoreRight += 1
            self.angle = 180 - self.angle
        if self.y < margin:
            self.angle = - self.angle
        if self.y + self.r  >=height - margin:
            self.angle = - self.angle

    # Check and Reflect the Ball when it hits the padddle
    def checkForPaddle(self):
        if self.x < width/2:
            if leftPaddle.x < self.x < leftPaddle.x + leftPaddle.w:
                if leftPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                    self.angle = -45
                if leftPaddle.y + 10 < self.y < leftPaddle.y + 20 or leftPaddle.y + 10 < self.y + self.r< leftPaddle.y + 20:
                    self.angle = -30
                if leftPaddle.y + 20 < self.y < leftPaddle.y + 30 or leftPaddle.y + 20 < self.y + self.r< leftPaddle.y + 30:
                    self.angle = -15
                if leftPaddle.y + 30 < self.y < leftPaddle.y + 40 or leftPaddle.y + 30 < self.y + self.r< leftPaddle.y + 40:
                    self.angle = -10
                if leftPaddle.y + 40 < self.y < leftPaddle.y + 50 or leftPaddle.y + 40 < self.y + self.r< leftPaddle.y + 50:
                    self.angle = 10
                if leftPaddle.y + 50 < self.y < leftPaddle.y + 60 or leftPaddle.y + 50 < self.y + self.r< leftPaddle.y + 60:
                    self.angle = 15
                if leftPaddle.y + 60 < self.y < leftPaddle.y + 70 or leftPaddle.y + 60 < self.y + self.r< leftPaddle.y + 70:
                    self.angle = 30
                if leftPaddle.y + 70 < self.y < leftPaddle.y + 80 or leftPaddle.y + 70 < self.y + self.r< leftPaddle.y + 80:
                    self.angle = 45
        else:
            if rightPaddle.x + rightPaddle.w > self.x  + self.r > rightPaddle.x:
                if rightPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                    self.angle = -135
                if rightPaddle.y + 10 < self.y < rightPaddle.y + 20 or rightPaddle.y + 10 < self.y + self.r< rightPaddle.y + 20:
                    self.angle = -150
                if rightPaddle.y + 20 < self.y < rightPaddle.y + 30 or rightPaddle.y + 20 < self.y + self.r< rightPaddle.y + 30:
                    self.angle = -165
                if rightPaddle.y + 30 < self.y < rightPaddle.y + 40 or rightPaddle.y + 30 < self.y + self.r< rightPaddle.y + 40:
                    self.angle = 170
                if rightPaddle.y + 40 < self.y < rightPaddle.y + 50 or rightPaddle.y + 40 < self.y + self.r< rightPaddle.y + 50:
                    self.angle = 190
                if rightPaddle.y + 50 < self.y < rightPaddle.y + 60 or rightPaddle.y + 50 < self.y + self.r< rightPaddle.y + 60:
                    self.angle = 165
                if rightPaddle.y + 60 < self.y < rightPaddle.y + 70 or rightPaddle.y + 60 < self.y + self.r< rightPaddle.y + 70:
                    self.angle = 150
                if rightPaddle.y + 70 < self.y < rightPaddle.y + 80 or rightPaddle.y + 70 < self.y + self.r< rightPaddle.y + 80:
                     self.angle = 135

# Show the Score
def pshowScore():
    leftScoreText = font.render("Score : " + str(scoreLeft), True, red)
    rightScoreText = font.render("Score : " + str(scoreRight), True, blue)

    display.blit(leftScoreText, (3*margin, 3*margin))
    display.blit(rightScoreText, (width/2 + 3*margin, 3*margin))

def pgameintro():
    font = pygame.font.SysFont("Forte", 30)
    text1=font.render("WELCOME TO 2-PLAYER PONG!",True,(230,230,230))
    text2=font.render("INTRUCTIONS:",True,(230,230,230))
    text3=font.render("This is a 2-player pong match",True,(230,230,230))
    text4=font.render("If a player misses the ball once, the opponent gains a point",True,(230,230,230))
    text5=font.render("If any of the player reaches the score '10',",True,(230,230,230))
    text6=font.render("The GAME is OVER!",True,(230,230,230))
    text7=font.render("Cost = FREE",True,(230,230,230))
    
    loop=True
    while loop:
        display.fill(background)
        start1.draw(display,(0,0,0))
        back.draw(display,(0,0,0))
        pos1=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start1.isOver(pos1):
                    pgame()
                if back.isOver(pos1):
                    start()
            if event.type==pygame.MOUSEMOTION:
                if start1.isOver(pos1):
                    start1.color=(230,230,230)
                else:
                    start1.color=blue
                if back.isOver(pos1):
                    back.color=(230,230,230)
                else:
                    back.color=blue  

        

        display.blit(text1,(200,100))
        display.blit(text2,(200,150))
        display.blit(text3,(10,300))
        display.blit(text4,(10,320))
        display.blit(text5,(10,340))
        display.blit(text6,(10,360))
        display.blit(text7,(10,380))
        
        pygame.display.update()

# Game Over
def gameOver():
    
    if scoreLeft == maxScore or scoreRight == maxScore:
        while True:
            restartButton.draw(display,(0,0,0))
            quitButton.draw(display,(0,0,0))
            pose=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_r:
                        reset()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if restartButton.isOver(pose):
                        pgame()
                    if quitButton.isOver(pose):
                        start()
                if event.type==pygame.MOUSEMOTION:
                    if restartButton.isOver(pose):
                        restartButton.color=(230,230,230)
                    else:
                        restartButton.color=blue
                    if quitButton.isOver(pose):
                        quitButton.color=(230,230,230)
                    else:
                        quitButton.color=blue 
            if scoreLeft == maxScore:
                playerWins = largeFont.render("Left Player Wins!", True, red)
            elif scoreRight == maxScore:
                playerWins = largeFont.render("Right Player Wins!", True, blue)

            display.blit(playerWins, (width/2 - 150, height/2-50))
            pygame.display.update()
            clock.tick()
def reset():
    global scoreLeft, scoreRight
    scoreLeft = 0
    scoreRight = 0
    


def pgame():
    loop = True
    reset()
    leftChange = 0
    rightChange = 0
    ball = pBall(yellow)
    
    while loop:
        display.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_w:
                    leftChange = -1
                if event.key == pygame.K_s:
                    leftChange = 1
                if event.key == pygame.K_UP:
                    rightChange = -1
                if event.key == pygame.K_DOWN:
                    rightChange = 1
            if event.type == pygame.KEYUP:
                leftChange = 0
                rightChange = 0

        leftPaddle.move(leftChange)
        rightPaddle.move(rightChange)
        ball.move()
        ball.checkForPaddle() 
        
        
        pshowScore()

        ball.show()
        leftPaddle.show()
        rightPaddle.show()

        boundary()

        gameOver()
        
        pygame.display.update()
        clock.tick(60)



#buttons
login=button(blue,150,200,450,75,"Login")
register=button(blue,150,300,450,75,"Register")
exitButton2=button(blue,150,500,450,75,"Exit Arcade")
hscores=button(blue,150,400,450,75,"High Scores")
playdodge=button(blue,100,140,550,70,"Play Dodgeball")
playStack=button(blue,100,230,550,70,"Play Stack")
playBalloon=button(blue,100,320,550,70,"Play BalloonShooter")
playPong=button(blue,100,410,550,70,"Play 2-PlayerPong")
exitButton=button(blue,50,500,275,70,"Exit")
signout=button(blue,50,590,275,70,"Sign Out")

myhscores=button(blue,350,500,350,70,"High Scores")
money=button(blue,350,590,350,70,"Add Coins")
restartButton=button(blue,375,50,200,60,"Restart")
quitButton=button(blue,425,500,150,60,"Quit")
next1=button(blue,100,600,550,60,"NEXT")
next2=button(blue,100,600,550,60,"NEXT")
back=button(blue,100,600,550,60,"BACK")
start1=button(blue,100,500,550,60,"START")
money2=button(blue,100,500,550,60,"Add Coins")


#main program
def main():
    run=True
    while run:

        redrawWindow1()
        
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if login.isOver(pos):
                    Login()
                if register.isOver(pos):
                    Register()
                if hscores.isOver(pos):
                    highscores()
                if exitButton2.isOver(pos):
                    close()
                
                
            if event.type==pygame.MOUSEMOTION:
                if login.isOver(pos):
                    login.color=white
                else:
                    login.color=blue
                if register.isOver(pos):
                    register.color=white
                else:
                    register.color=blue
                if hscores.isOver(pos):
                    hscores.color=white
                else:
                    hscores.color=blue
                if exitButton2.isOver(pos):
                    exitButton2.color=white
                else:
                    exitButton2.color=blue

        pygame.display.update()
main()






            
