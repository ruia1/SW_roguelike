import requests
import json

def test():
    url = "https://yutorize.2-d.jp/ytsheet/sw2.5/?id=JrSPbj&mode=json"
    r=requests.get(url)
    return r.content

r = test()
t = json.loads(r)

aexp = 0
for i in range(int(t["historyNum"])+1):
    K = "history"+str(i)+"Exp"
    try:
        aexp += int(t[K])
    except KeyError:
        pass

#ゆとシート2のmode=jsonについて：
#json形式でキャラクターシートが閲覧できます。一次元データであり、すべて単一のキーで値を取得できます。
#また、整数値が期待される値もすべて文字列として格納されているため、型変換の必要があります。
#https://yutorize.2-d.jp/?ytsheet2-json

#左からPC名、PL名、累積経験点、所持金
print(t["playerName"],t["characterName"],aexp,t["money"])