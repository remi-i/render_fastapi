from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

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

    return {"result": omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>ホームページTOP</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>岩田です。</p>
            <p>FastAPIの課題で作成したページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)