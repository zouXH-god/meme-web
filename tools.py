import base64
import copy
import os

import requests

base_url = os.getenv('meme_generator_base_url')
memes = {}


def get_keys():
    if memes:
        return memes.keys()
    result = requests.get(base_url + '/memes/keys')
    times = 0
    print("正在加载表情包数据...")
    for i, key in enumerate(result.json()):
        print(f"\r正在加载表情：{i}/{len(result.json())} {key}...", end='')
        # times += 1
        # if times > 9:
        #     break
        memes[key] = get_meme(key)
    return memes.keys()


def get_keywords():
    keywords = [meme_data["keywords"] for meme_data in memes.values()]
    return keywords


def get_meme_preview(key):
    if memes[key].get("preview"):
        return memes[key]["preview"]
    result = requests.get(f"{base_url}/memes/{key}/preview").content
    memes[key]["preview"] = result
    return result


def get_meme_info(key):
    info = copy.deepcopy(memes[key])
    if info.get("preview"):
        del info["preview"]
    return info


def get_meme(key):
    result = requests.get(f"{base_url}/memes/{key}/info")
    return result.json()


def make_meme(key, texts, images):
    files = [("images", base64_to_img(image)) for image in images]
    data = {"texts": texts}
    result = requests.post(f"{base_url}/memes/{key}", data=data, files=files)
    return img_to_base64(result.content)


def base64_to_img(base64_str):
    return base64.b64decode(base64_str)


def img_to_base64(img):
    return base64.b64encode(img).decode()