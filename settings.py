import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

#settings.pyの相対パスを取得し.envを指定し読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TKN = os.environ.get("TOKEN")

