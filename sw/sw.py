import random
import os
def makeTree(length):
    pass

class sw:
    def __init__(self):
        self.ver = "2.5"
    
    def enemy_data(name):
        pass

    def party_data(n):
        pass

    class rogue:
        def __init__(self, seed = None):
            self.N_STAGE = None #面
            self.N_FLOOR = None #階層
            self.N_BRANCH = None #分岐番号
            self.N_PLAYER = None #冒険者人数
            self.S_PLAYER_LEVEL = None #冒険者レベル合計
            self.A_PLAYER_LEVEL = None #冒険者レベル平均
            self.A_PLAYER_AEXP = None #冒険者平均累計経験点
            self.SEED = seed
            self.stage = self.stage()

        class stage:
            def __init__(self,seed = None):
                self.SEED = seed
                if self.SEED:
                    self.SEED = random.randint(10000000,99999999)
                pass
        
    class enemy:
        def __init__(self):
            pass

                







game = sw.rogue()
print(game.N_STAGE)