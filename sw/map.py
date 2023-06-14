import random
import math
import io

#部屋ノードクラス
class nod:
    def __init__(self) -> int:
        self.cur_floor = 0
        self.next_floor = self.cur_floor + 1
        self.cur_x = None #左<0 1 2 3 4 5>右
        self.next_route1 = None #次の階層で右に行く：1
        self.next_route2 = None #次の階層に行く：0
        self.next_route3 = None #次の階層で左に行く：-1

#マップ生成
map = [[nod() for i in range(6)] for j in range(12)]
seed = random.randint(10000000,99999999)

def set_route(seed,flo,xx):
    if (flo+xx)&1:
        map[flo][xx].next_toute = 0
    else:
        if xx == 0:
            if seed % 3 == 0:
                map[flo][xx].next_route1 = 1
            elif seed % 3 == 1:
                map[flo][xx].next_route2 = 0
            elif seed % 3 == 2:
                map[flo][xx].next_route1 = 1
                map[flo][xx].next_route2 = 0
        elif xx == 5:
            if seed % 3 == 0:
                map[flo][xx].next_route2 = 0
            elif seed % 3 == 1:
                map[flo][xx].next_route3 = -1
            elif seed % 3 == 2:
                map[flo][xx].next_route2 = 0
                map[flo][xx].next_route3 = -1
        else:
            if seed % 7 == 0:
                map[flo][xx].next_route1 = 1
                map[flo][xx].next_route2 = 0
                map[flo][xx].next_route3 = -1
            elif seed % 7 == 1:
                map[flo][xx].next_route1 = 1
            elif seed % 7 == 2:
                map[flo][xx].next_route2 = 0
            elif seed % 7 == 3:
                map[flo][xx].next_route3 = -1
            elif seed % 7 == 4:
                map[flo][xx].next_route1 = 1
                map[flo][xx].next_route2 = 0
            elif seed % 7 == 5:
                map[flo][xx].next_route2 = 0
                map[flo][xx].next_route3 = -1
            elif seed % 7 == 6:
                map[flo][xx].next_route3 = -1
                map[flo][xx].next_route1 = 1

def gen_map(seed):
    limit = 0
    print(seed)
    while limit < 3:
        x = random.randint(0,5)
        if map[0][x].cur_x == None:
            map[0][x].cur_floor = 0
            map[0][x].cur_x = x
            set_route(seed,0,x)
            limit += 1
    for i in range(11):
        now_floor = i + 1
        for x in range(6):
            map[now_floor][x].cur_floor = now_floor
            if map[i][x].next_route1 == 1:
                map[now_floor][x].cur_x = x + map[i][x].next_route1
                set_route(seed,now_floor,x)
            if map[i][x].next_route2 == 0:
                map[now_floor][x].cur_x = x + map[i][x].next_route2
                set_route(seed,now_floor,x)
            if map[i][x].next_route3 == -1:
                map[now_floor][x].cur_x = x + map[i][x].next_route3
                set_route(seed,now_floor,x)

gen_map(seed)
print()
i = 0
j = 0
print()
while i < 12:
    print("[",end = "")
    while j < 6:
        if map[i][j].cur_x != None:
            print(1,end = "")
        else:
            print(0,end = "")
        print(",",end = "")
        j += 1
    j = 0
    print("\b]")
    i += 1
