#field 15*10 w 48
class Field:
    def __init__(self):
        self.blocks=[[Block() for x in range(15)]for y in range(10)]
    

    def plant(self,x,y,crop):
        block=self.blocks[y][x]
        if block.state=="empty":
            block.state="planted"
            block.crop=crop

    def water(self,x,y):
        self.blocks[y][x].watered=True

    def update(self):
        for x in range(15):
            for y in range(10):
                block=self.blocks[y][x]
                if block.state=="planted":
                    block.growth+=1



class Block:
    def __init__(self):
        self.state="empty"
        self.crop=None
        self.growth=0
        self.watered=False