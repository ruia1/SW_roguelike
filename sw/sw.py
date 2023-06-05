import random, json, requests
import os

class sw: #import enemy, party
    enemy_data = None #dict
    party_data = None #list(lv * n)
    boss_data = None #list(lv * n)

    def __init__(self) -> None:
        self.VER = "2.5"
    
    def enemy_data(self, name) -> "enemy":
        if enemy_data == None:
            enemy_data = enemy.setup()
        return self.enemy_data[name]
    
    def party_data(self, lv,n) -> "party":
        if self.party_data == None:
            enemy.setup()
        return self.party_data[lv][n]

class treasurer: #import None
    #URLが入力されていればそちらを優先する。

    def __init__(self, player_name = None, treasurer_name = None, level = None, aexp = None, money = None, URL = None) -> None:
        self.url = URL
        if URL != None:
            self.read_ytsheet(URL)
        if player_name != None: self.player_name = player_name
        if treasurer_name != None: self.treasurer_name = treasurer_name
        if level != None: self.level = level
        if aexp != None: self.aexp = aexp
        if money != None: self.money = money

    
    def read_ytsheet(self, URL) -> None:
        if not "https://yutorize.2-d.jp/ytsheet/sw2.5/?id=" in URL:
            raise ValueError("URL is not correct. This supports only ytsheet.")
        if "mode=json" in URL:
            URL = URL + "&mode=json"
        data = json.loads(requests.get(URL).content)
        self.player_name = data["playerName"]
        self.treasurer_name = data["characterName"]
        self.level = int(data["level"])
        #self.money = int(data["money"]) #moneyのデータが"自動"になっていたりするので対処法を考え中です
        return True

class parts:
    def __init__(self,name = None, range = None, attribute = None, accuracy = None, rate = None, magic_power = None, DEF = None, HP = None, MP = None, skill1 = None, skill2 = None, skill3 = None) -> None:
        self.name = name
        self.range = range #range:射程
        self.attribute = attribute #attribute:属性
        self.accuracy = accuracy #accuracy:命中
        self.rate = rate #rate:打撃点（固定値）
        self.magic_power = magic_power #magic_power:魔力
        self.DEF = DEF #DEF:防護点
        self.HP = HP
        self.MP = MP
        self.skills = [] #skill:特殊能力
        for skill in [skill1, skill2, skill3]:
            if skill != None: self.skills.append(skill)

class enemy: #import None
    def __init__(self, name=None, level = None, N_parts = None, preemptive = None, popularity = None, weak_num = None, weak = None, tough = None, robust = None, **kwargs) -> None:
        self.name = name
        self.level = level
        self.N_parts = N_parts #N_parts:パーツ数
        self.preenptive = preemptive #preemptive:先制値
        self.popularity = popularity #popularity:知名度
        self.weak_num = weak_num #weak_num:弱点値
        self.weak = weak #weak:弱点
        self.tough = tough #tough:生命抵抗力
        self.robust = robust #robust:精神抵抗力
        self.parts = kwargs #kwargs:パーツ(type:class)

    def setup(self) -> None:
        pass #enemy_data, party_dataの読み込みをする関数　の予定

class party: #import treasures
    def __init__(self,treasures, party_level = None) -> None:
        self.party_level = party_level
        self.treasures = treasures

#rogueクラスを内部クラスにするかswクラスを継承して使うのかはまだ考え中

class swRogue(sw): #import random, sw, stage
    def __init__(self, seed = None) -> None:
        super().__init__()
        self.N_STAGE = None #面
        self.N_FLOOR = None #階層
        self.N_BRANCH = None #分岐番号
        self.N_TRASURER = None #冒険者人数
        self.S_TRASURER_LEVEL = None #冒険者レベル合計
        self.A_TRASURER_LEVEL = None #冒険者レベル平均
        self.A_TRASURER_AEXP = None #冒険者平均累計経験点
        self.earn = 0 #ゲーム中に稼いだ額
        self.exp = 0 #ゲーム中に稼いだ経験値
        self.generateSeed(seed)
        self.STAGE = stage(self.SEED)
    
    def generateSeed(self, seed) -> None:
        self.SEED = seed
        if self.SEED == None:
            self.SEED = random.randint(10000000,99999999)
    
    def regesterTreasurerStatus(self, *args):
        self.N_treasurer = len(args)
        level = 0
        exp = 0
        for i in args:
            level += args.level
            exp += args.aexp//500
        self.S_TRASURER_LEVEL = level
        self.A_TRASURER_LEVEL = level//self.N_treasurer
        self.A_TRASURER_AEXP = exp//self.N_treasurer

    def addMoneyExp(self, money, exp):
        self.earn += money
        self.exp += exp

class stage: #import room
    def __init__(self, seed) -> None:
        self.generate(seed)

    def generate(self, seed) -> None:
        pass #こーたくんが実装するとこ
    #配列rooms:アクティブな部屋の座標が一覧になった配列データも生成する

    def enter(self, x, y, swRogue):
        type = self.stage[y][x][0]
        room = room(type, x, y, swRogue)

class room: #import None
    def __init__(self, type, x, y, swRogue) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.seed = swRogue.SEED
        roomSeed = (swRogue.SEED * x * (y+10))%(10**8)
        random.seed(roomSeed)
        
    class enemy:
        def __init__(self, x, y, roomSeed) -> None:
            pass

    class elite:
        def __init__(self, x, y, roomSeed) -> None:
            pass

    class search:
        def __init__(self, x, y, seed) -> None:
            pass

    class q:
        def __init__(self, x, y, seed) -> None:
            pass

    class rest:
        def __init__(self, x, y, seed) -> None:
            pass

    class shop:
        def __init__(self, x, y, seed) -> None:
            pass

    class boss:
        def __init__(self, x, y, seed) -> None:
            pass


if __name__ == '__main__':
    game = swRogue()
    url = "https://yutorize.2-d.jp/ytsheet/sw2.5/?id=JrSPbj&mode=json"
    pl1 = treasurer(URL = url)
    print(game.VER, pl1.treasurer_name)