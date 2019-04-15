from flask import Blueprint,jsonify,send_file
from setting import MONGODB,COVER_PATH,MUSIC_PATH
import os

gsa = Blueprint("gsa",__name__)

@gsa.route("/get_cover/<filename>")
def get_cover(filename):
    cover_file = os.path.join(COVER_PATH,filename)

    return send_file(cover_file)

@gsa.route("/get_music/<filename>")
def get_music(filename):
    music_file = os.path.join(MUSIC_PATH,filename)

    return send_file(music_file)