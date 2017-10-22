# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob
cl = LINETCR.LINE()
print u"""Login START"""
cl.login(qr=True)
cl.loginResult()
print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
print u"login成功"
i = 0
c_text = """[Text]"""


while True:
    try:
        for posts in cl.activity(1)["result"]["posts"]:
            if posts["postInfo"]["liked"] is False:
                cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],"AUTO LIKE BY SATRIA \n\n⏩line.me/ti/p/~satria_hk")
                print u"liked" + str(i)
                i += 1
    except Exception as e:
            print e
