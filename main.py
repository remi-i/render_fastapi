from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

random_number = random.random()
print("Random float number:", random_number)

# 1から10までのランダムな整数を生成
random_integer = random.randint(1, 10)
print("Random integer:", random_integer)

# リストからランダムに1つの要素を選択
fruits = ['apple', 'banana', 'cherry', 'date']
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)

# リストの要素をランダムに並び替え
cards = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
random.shuffle(cards)
print("Shuffled cards:", cards)

# 1から20までの整数から重複なしで3つの要素を抽出
random_numbers = random.sample(range(1, 21), 3)
print("Random numbers:", random_numbers)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}