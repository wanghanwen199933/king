# 喜马拉雅URL
XMLY_URL = "https://www.ximalaya.com/revision/play/album?albumId=%s&pageNum=%s&sort=-1&pageSize=30"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}


# 数据库配置
import pymongo
conn = pymongo.MongoClient("127.0.0.1",27017)
MONGODB = conn["VistaToy"]


# 目录配置
MUSIC_PATH = "Music"
COVER_PATH = "Cover"
QRCODE_PATH = "QRcode"



# App通讯协议
RET = {
    "CODE":0,
    "MSG":"",
    "DATA":{}
}

#联图二维码
LT_URL = "http://qr.topscan.com/api.php?text=%s"