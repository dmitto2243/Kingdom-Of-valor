from gamelib import*

#Myobjects and initial settings
game = Game(800,600,"Kingdom of Valor")
bk = Image("level1bk.jpg",game)
game.setBackground(bk)
bk.resizeTo(800,600)
sabeehah = Image("sabeehah.png", game)
sabeehah.resizeBy(-90)
title = Image("title.png", game)
title.resizeBy(-20)
howtoplay = Image("howtoplay.png", game)
howtoplay.resizeBy(-40)
play = Image("play.png", game)
play.resizeBy(-40)
story = Image("story.png", game)
story.resizeBy(-40)
storyImage = Image("storyimage.png", game)
storyImage.visible = False
howtoplay2 = Image("howtoplay2", game)
howtoplay2.visible = False
back = Image("back.png", game)
back.resizeBy(-90)
back.visible = False
minions = Image("minion.png", game)
mage = Image("mage.png", game)
sabeehah.y = 500
sabeehah.x = 100
howtoplay.y = 500
story.y = 350
play.y = 200
title.y = 100
back.y = 550
back.x = 50
f = Font(black,60,red,"Impact")

#Title Sreen
while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    howtoplay.draw()
    play.draw()
    storyImage.draw()
    story.draw()
    sabeehah.draw()
    howtoplayImage.draw()
    back.draw()
    
    if story.collidedWith(mouse)and mouse.LeftClick:
        howtoplayImage.visible = False
        storyImage.visible = True
        story.visible = False
        back.visible = True
        

    if back.collidedWith(mouse)and mouse.LeftClick:
        storyImage.visible = False
        story.visible = True
        back.visible = False
        howtoplay.visible = True
        howtoplay2.visible = False

    if howtoplay.collidedWith(mouse)and mouse.LeftClick:
        storyImage.visible = False
        howtoplay2.visible = True
        howtoplay.visible = True
        back.visible = True

    game.update(30)
        
game.over = False

#Level 1

while not game.over:
    game.processInput()
    minions = []
    bk.draw()
    sabeehah.draw()
    mage.draw()                
    mage.y = 500
    mage.x = 600
    game.displayTime(10,10,f)
    game.time-=1
    game.displayScore(mouse.x-60,mouse.y+100,f)
    game.drawText("Level 1",300,300)
    sabeehah.move(True)
    sabeehah.moveTo(mouse.x, mouse.y)
    for index in range(4):
        minions.append(Image("minion.png",41,game,1022/41,41))
    for index in range(4):
        minions[index].resizeBy(-75)
    if game.time <= 0:
        game.over = True

