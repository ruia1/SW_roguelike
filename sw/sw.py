import random, json, requests
import os

class sw:
    enemy_data = None
    party_data = None

    def __init__(self) -> None:
        self.VER = "2.5"
    
    def enemy_data(self, name) -> "enemy":
        if enemy_data == None:
            enemy_data = sw.enemy.setup()
        return self.enemy_data[name]
    
    def party_data(self, lv,n) -> "party":
        if self.enemy_data == None:
            sw.enemy.setup()
        return self.enemy_data[lv][n]

    class treasurer:
        def __init__(self, playerName = None, characterName = None, level = None, aexp = None, money = None, URL = None) -> None:
            self.url = URL
            if URL != None:
                self.read_ytsheet(URL)
            if playerName != None: self.playerName = playerName
            if characterName != None: self.characterName = characterName
            if level != None: self.level = level
            if aexp != None: self.aexp = aexp
            if money != None: self.money = money

        
        def read_ytsheet(self, URL) -> None:
            if not "https://yutorize.2-d.jp/ytsheet/sw2.5/?id=" in URL:
                raise ValueError("URL is not correct. This supports only ytsheet.")
            if "mode=json" in URL:
                URL = URL + "&mode=json"
            data = json.loads(requests.get(URL).content, parse_int = True)
            self.playerName = data["playerName"]
            self.characterName = data["characterName"]
            self.level = int(data["level"])
            #self.money = int(data["money"]) #moneyのデータが"自動"になっていたりするので対処法を考え中です
            return True
        
    class enemy:
        def __init__(self, name=None) -> None:
            self.name = name

        def setup(self) -> None:
            pass #enemy_data, party_dataの読み込みをする関数　の予定
    
    class party:
        def __init__(self,treasures, partyLevel=None, ) -> None:
            self.partyLevel = partyLevel
            self.treasures = self.treasures

#rogueクラスを内部クラスにするかswクラスを継承して使うのかはまだ考え中

class sw_rogue(sw):
        def __init__(self, seed = None) -> None:
            super().__init__()
            self.N_STAGE = None #面
            self.N_FLOOR = None #階層
            self.N_BRANCH = None #分岐番号
            self.N_PLAYER = None #冒険者人数
            self.S_PLAYER_LEVEL = None #冒険者レベル合計
            self.A_PLAYER_LEVEL = None #冒険者レベル平均
            self.A_PLAYER_AEXP = None #冒険者平均累計経験点
            self.generate_seed(seed)
            self.STAGE = self.stage(self.SEED)
        
        def generate_seed(self, seed) -> None:
            self.SEED = seed
            if self.SEED == None:
                self.SEED = random.randint(10000000,99999999)

        class stage:
            def __init__(self,seed = None) -> None:
                self.generate()
                pass

            def generate():
                pass

            class room:
                def __init__(self, type=None) -> None:
                    self.type = type
                class enemy:
                    def __init__(self) -> None:
                        pass
                class elite:
                    def __init__(self) -> None:
                        pass
                class search:
                    def __init__(self) -> None:
                        pass
                class q:
                    def __init__(self) -> None:
                        pass
                class rest:
                    def __init__(self) -> None:
                        pass
                class shop:
                    def __init__(self) -> None:
                        pass
                class boss:
                    def __init__(self) -> None:
                        pass
                        
                






if __name__ == '__main__':
    game = sw_rogue()
    url = "https://yutorize.2-d.jp/ytsheet/sw2.5/?id=JrSPbj&mode=json"
    pl1 = game.treasurer(URL = url)
    print(game.VER,pl1.characterName)