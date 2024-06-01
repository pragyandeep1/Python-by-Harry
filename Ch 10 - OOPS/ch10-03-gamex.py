class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveBottom(self):
        pass

r1 = Remote()
p1 = Player()

if(r1.isRightPressed()):
    p1.moveRight()

if(r1.isLeftPressed()):
    p1.moveLeft()

if(r1.isTopPressed()):
    p1.moveTop()

if(r1.isBottomPressed()):
    p1.moveBottom()