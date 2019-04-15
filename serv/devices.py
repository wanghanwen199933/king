from bson import ObjectId
from flask import Blueprint,jsonify,send_file,request
from setting import MONGODB,COVER_PATH,MUSIC_PATH,RET
import os

devices = Blueprint("devices",__name__)

@devices.route("/scan_qr",methods=["POST"])
def scan_qr():
    # 1.扫码的二维码存在于数据库中 Devices 数据表中
    # 2.扫描的二维码不在数据库中
    # 3.神秘代码
    device_key = request.form.to_dict() # {"device_key":341252346}
    res = MONGODB.devices.find_one(device_key)
    if res:# 1.扫码的二维码存在于数据库中 Devices 数据表中
        RET["CODE"] = 0
        RET["MSG"] = "扫描二维码成功"
        RET["DATA"] = device_key

    else: # 2.扫描的二维码不在数据库中
        RET["CODE"] = 1
        RET["MSG"] = "滚犊子"
        RET["DATA"] = {}

    return jsonify(RET)


# 目前只完成部分功能
@devices.route("/bind_toy",methods=["POST"])
def bind_toy():
    #1.创建玩具 - 填写玩具基本信息
    toy_info = request.form.to_dict()
    toy_info["avatar"] = "toy.jpg"
    # 2.告诉玩具你的绑定用户是谁
    toy_info["bind_user"] = toy_info.pop("user_id")
    toy_info["friend_list"] = []

    toy = MONGODB.toys.insert_one(toy_info)

    # 3.告诉用户你的绑定玩具是谁
    # user = MONGODB.users.find_one({"_id":ObjectId(toy_info["bind_user"])})
    # user.get("bind_toys").append(str(toy.inserted_id))
    # MONGODB.users.update_one({"_id":ObjectId(toy_info["bind_user"])},{"$set":user})
    MONGODB.users.update_one({"_id": ObjectId(toy_info["bind_user"])},
                             {"$push": {"bind_toys":str(toy.inserted_id)}})

    RET["CODE"] = 0
    RET["MSG"] = "绑定完成"
    RET["DATA"] = {}

    return jsonify(RET)


@devices.route("/toy_list",methods=["POST"])
def toy_list():
    _id = request.form.get("_id")
    toy_li = list(MONGODB.toys.find({"bind_user":_id}))
    for index,toy in enumerate(toy_li):
        toy_li[index]["_id"] = str(toy.get("_id"))


    RET["CODE"] = 0
    RET["MSG"] = "玩具列表"
    RET["DATA"] = toy_li

    return jsonify(RET)

