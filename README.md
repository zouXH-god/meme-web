<div align="center">

# meme-web

_✨ 基于meme-generator-api的网页版表情包生成器 ✨_

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python">
</p>

<img src="/docs/1.png">

</div>

## 表情列表

表情详细信息、表情预览等可以在 [--> 表情列表 <--](https://github.com/MeetWq/meme-generator/wiki/%E8%A1%A8%E6%83%85%E5%88%97%E8%A1%A8) 查看

## 安装、使用、配置

### 本程序基于 `meme-generator` 项目开发，请先部署 `meme-generator` 项目

meme-generator 部署：[--> Wiki <--](https://github.com/MeetWq/meme-generator/wiki)

### 部署 meme-web

- clone 仓库并安装python包
```shell
# clone 
git clone https://github.com/zouXH-god/meme-web.git
# 安装环境
pip install dotenv flask requests
```

- 配置文件 `.env`
修改 `.env` 文件，将 `meme_generator_base_url` 改为你的 `meme-generator` 的部署地址，如：`meme_generator_base_url=http://127.0.0.1:2233`

- 运行程序
执行 `python app.py` 命令启动程序
等待数据加载完毕，浏览器访问 `http://IP:2333` 即可使用

## 鸣谢

本项目基于 [meme-generator](https://github.com/MeetWq/meme-generator) api编写
