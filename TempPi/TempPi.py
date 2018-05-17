#!/usr/bin/env python
# -*- coding: cp932 -*-

######################################
# ターゲットURL
# http://13.78.12.117/~webtest/graph/tocsv.pl
#
# 'http://13.78.12.117/~webtest/graph/tocsv.pl?time=2018-05-15%3A10%3A51%3A09&tempA=9.24981431974&tempB=16.9945836766'
# ↑の形式で 日時,パラメータ１,パラメータ２ をGetメソッドでターゲットへ送る
######################################

# 日付と時刻ライブラリ
import datetime
import time

# URL関係ライブラリ
# Python2.7
import urllib

# 温度センサ (i2c接続)#ADT7401
import smbus


# Python3
#import urllib.parse
#import urllib.request


i2c = smbus.SMBus(1)
addr=0x48 #ADT7401



# テスト用
import  random


# ターゲットURL
TargetURL = "http://13.78.12.117/~webtest/graph/tocsv.pl"


def sign13(x):
       return ( -(x & 0b1000000000000) |
                 (x & 0b0111111111111) )


def GetAndPut(url,p1,p2):

    # 現在時間の取得
    now = datetime.datetime.now()
    # print('test_{0:%Y-%m-%d:%H:%M:%S}'.format(now))

    DateAndTime = '{0:%Y-%m-%d:%H:%M:%S}'.format(now)

    # 出力パラメータ
    param = [
        ( "time",DateAndTime),
        ( "tempA", p1),
        ( "tempB", p2),
    ]


    #Python3の場合
    #url += "?{0}".format( urllib.parse.urlencode( param ) )

    #python2.7
    url += "?{0}".format( urllib.urlencode( param ) )


    #Python3の場合
    #with urllib.request.urlopen(url) as o_url:
    #    s = o_url.read()
    #I'm guessing this would output the html source code?
    #print(s)

    #p2.7
    #API実行
    result = None
    try :
        result = urllib.urlopen( url ).read()
    except ValueError :
        print "アクセスに失敗しました。"

# メイン
if __name__ == '__main__':

	#無事起動できるか？　15秒待つ(本当はURLのエラー処理が必要）
    time.sleep(15)


    while True:
        numA = random.uniform(2.0,15.0)
        numB = random.uniform(6.0,18.0)

        data = i2c.read_i2c_block_data(addr, 0)
        raw = (((data[0]) << 8) | (data[1]) ) >> 3
        #print (hex(data[0]));print(hex(data[1]));print(hex(raw));print(bin(raw))
        raw_s = sign13(int(hex(raw),16))
        temp = raw_s * 0.0625
        print (str(temp) +"C")

        GetAndPut(TargetURL,temp,numB)

        time.sleep(1)

