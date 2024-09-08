import json
import os

import requests
from flask import Flask, request
from dotenv import load_dotenv
# 加载 .env 文件
load_dotenv()
from tools import get_keys, get_keywords, get_meme_preview, get_meme_info, make_meme

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("templates/make.html", "r", encoding="utf-8") as fp:
        return fp.read()


@app.route("/memes/keys")
def get_keys_api():
    return list(get_keys())


@app.route("/memes/keywords")
def get_keywords_api():
    return get_keywords()


@app.route("/memes/<key>/info")
def get_meme_api(key):
    return get_meme_info(key)


@app.route("/memes/<key>/preview")
def get_meme_preview_api(key):
    return get_meme_preview(key)


@app.route("/memes/get_img")
def get_img_api():
    qq = request.args.get("qq")
    return requests.get(f"http://q.qlogo.cn/headimg_dl?dst_uin={qq}&spec=640").content


@app.route("/memes/<key>/", methods=["POST"])
def make_meme_api(key):
    images_base64 = request.form.get("images_base64")
    if images_base64:
        images_base64 = json.loads(images_base64)
    else:
        images_base64 = []
    texts = request.form.get("texts_json")
    if texts:
        texts = json.loads(texts)
    else:
        texts = []
    return make_meme(key, texts, images_base64)


if __name__ == '__main__':
    get_keys()
    app.run(os.getenv("HOST"), os.getenv("PORT"))