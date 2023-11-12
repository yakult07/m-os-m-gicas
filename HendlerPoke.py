


from utils import move_and_click, get_loot


class HandlerPoke:
    def __init__(self):
        self.count = 0
        self.list_poke = [(29,702),(31,756),(30,814),(30,864),(32,920),(28,978)]
        self.heald = (28,978)
    def check_poke_lenght(self):
        self.count = self.count % len(self.list_poke) # garabte 0-5

    def headling(self):
        self.count += 1
        self.check_poke_lenght()
        move_and_click(self.list_poke[5], 'right')   

    def next(self):
        self.count += 1
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')
        
    def previous(self):
        self.count -= 1
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')





    
            


           
    

