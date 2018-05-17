#!/usr/bin/env python
# -*- coding: cp932 -*-

######################################
# �^�[�Q�b�gURL
# http://13.78.12.117/~webtest/graph/tocsv.pl
#
# 'http://13.78.12.117/~webtest/graph/tocsv.pl?time=2018-05-15%3A10%3A51%3A09&tempA=9.24981431974&tempB=16.9945836766'
# ���̌`���� ����,�p�����[�^�P,�p�����[�^�Q ��Get���\�b�h�Ń^�[�Q�b�g�֑���
######################################

# ���t�Ǝ������C�u����
import datetime
import time

# URL�֌W���C�u����
# Python2.7
import urllib

# ���x�Z���T (i2c�ڑ�)#ADT7401
import smbus


# Python3
#import urllib.parse
#import urllib.request


i2c = smbus.SMBus(1)
addr=0x48 #ADT7401



# �e�X�g�p
import  random


# �^�[�Q�b�gURL
TargetURL = "http://13.78.12.117/~webtest/graph/tocsv.pl"


def sign13(x):
       return ( -(x & 0b1000000000000) |
                 (x & 0b0111111111111) )


def GetAndPut(url,p1,p2):

    # ���ݎ��Ԃ̎擾
    now = datetime.datetime.now()
    # print('test_{0:%Y-%m-%d:%H:%M:%S}'.format(now))

    DateAndTime = '{0:%Y-%m-%d:%H:%M:%S}'.format(now)

    # �o�̓p�����[�^
    param = [
        ( "time",DateAndTime),
        ( "tempA", p1),
        ( "tempB", p2),
    ]


    #Python3�̏ꍇ
    #url += "?{0}".format( urllib.parse.urlencode( param ) )

    #python2.7
    url += "?{0}".format( urllib.urlencode( param ) )


    #Python3�̏ꍇ
    #with urllib.request.urlopen(url) as o_url:
    #    s = o_url.read()
    #I'm guessing this would output the html source code?
    #print(s)

    #p2.7
    #API���s
    result = None
    try :
        result = urllib.urlopen( url ).read()
    except ValueError :
        print "�A�N�Z�X�Ɏ��s���܂����B"

# ���C��
if __name__ == '__main__':

	#�����N���ł��邩�H�@15�b�҂�(�{����URL�̃G���[�������K�v�j
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

