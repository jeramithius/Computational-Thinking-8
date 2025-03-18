###############################################
### SETUP ###
import codesters
from codesters import StageClass

import codesters.sprites
stage = StageClass()
###############################################

stage.set_background("fall")

q1 = codesters.Square(100, 100, 200, 'lightblue')
q2 = codesters.Square(-100, 100, 200, 'green')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'blue')

mySprite = codesters.Sprite("pineappletransparent.png",-100,100)
mySprite.set_size(0.67)

mySprite = codesters.Sprite("F22.png",-100,-100)
mySprite.set_size(0.2)

mySprite = codesters.Sprite("pokebowlnew.png",100,100)
mySprite.set_size(0.67)

mySprite = codesters.Sprite("dogtransparent.png",100,-100)
mySprite.set_size(0.3)

message1 = codesters.Text("Jack Cluett",0,220,"black")
message1 = codesters.Text("what is goodie",0,-220,"black")
