import configparser
from forum.settings import BASE_DIR
import os

config = configparser.ConfigParser()    #实例化配置解析器
config_path = os.path.join(os.path.dirname(os.getcwd()),"forum_auxiliary/config.ini")   #conf.ini文件的路径
print(config_path)
config.read(config_path)    #读取config.ini路径
DEBUG = config["default"].getboolean("debug")
MEDIA_BASE_URL = config["default"]["media_base_url"]