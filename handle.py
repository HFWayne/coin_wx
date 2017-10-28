# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
from basic import Basic
from material import Material
import json


class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                print recMsg.MsgType
                if recMsg.MsgType == 'text':
                    myMaterial = Material()
                    accessToken = Basic().get_access_token()
                    mediaType = "image"
                    #media_list_str = myMaterial.batch_get(accessToken, mediaType)
                    media_list_str = """{"item":[{"media_id":"XbWgtjJzzVVRvAKCelclRVYhorrTWqnevSuupBeOji8","name":".\/image\/SDR00000007.jpg","update_time":1509197388,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt7aA8UicAjmMvpdZSjU3cuCV6hWNmNkqI5k0hADpupQNg9dY12TuYLGNw\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRVd4YLKxhnSVwPESYyrAtpU","name":".\/image\/SDR00000006.jpeg","update_time":1509197387,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt7y8mT3yrTeKHWlJib99OaobNyznPRylevBVIibabYdugmxFS5hRl1zn1A\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRfoGbJXC1XpDjU0yRfA2R-o","name":".\/image\/SDR00000005.jpeg","update_time":1509197386,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt7zL0RllkOFXrfTyLpnJ2adnZhuiaiakxQhYwgW36butGibfTLTOc7Bicpkg\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRVpqcX3SrHM1C2v_kP2BOfE","name":".\/image\/SDR00000004.jpeg","update_time":1509197385,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt705uRzZRZv1mjXfJrQoxMx5HNRuExwRc5hZTUibdzzJKkJmaoiboicCPBA\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRYEd0zOvibwRJecY8wgF3ys","name":".\/image\/SDR00000003.jpeg","update_time":1509197384,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt7bp6kicl9pciayZ16z5pC1hXNXB5QsQvKqc2ZjMIlfkKrLqYrdnT9tfWw\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRUdFNpEQCnyOZB5KZgIvCfM","name":".\/image\/SDR00000002.jpeg","update_time":1509197383,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt79BB8LBg5Yd2TdtlMsd19oXiabB3xaBbyQeKUcrGribcshFzoZBKbzq3Q\/0?wx_fmt=jpeg"},{"media_id":"XbWgtjJzzVVRvAKCelclRa9sNwrlbu3FfPe44PmOSfI","name":".\/image\/SDR00000001.jpeg","update_time":1509197236,"url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/CxLDZshQqGJYOUCne1IGiccbk9MB7Mmt7a7LIQnIMSAtzRTt2pMgbXuam9ok0zDSic3zGAKjF5D2Miadje0bOCYhg\/0?wx_fmt=jpeg"}],"total_count":7,"item_count":7}"""
                    media_list = json.loads(media_list_str)
                    print media_list
                    if 'errcode' in media_list:
                        print media_list['errmsg']
                        replyMsg = reply.TextMsg(toUser, fromUser, "查询失败!")
                        return replyMsg.send()
                    print '2222222222'
                    for media in media_list['item']:
                        print media
                        target = recMsg.Content
                        print target
                        print type(target)
                        if len(target) is not 8:
                            media_id = None
                        else:
                            if media['name'].find(target) is not -1:
                                media_id = media['media_id']
                                print media_id
                                break
                            else:
                                media_id = None

                    print media_id
                    if media_id is not None:
                        replyMsg = reply.ImageMsg(toUser, fromUser, media_id)
                        return replyMsg.send()
                    else:
                        content = "查询无结果!"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                elif recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            elif isinstance(recMsg, receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event == 'CLICK':
                    if recMsg.EventKey == "SearchSDR":
                        content = """请输入DRS编码!
示例:00000001"""
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    else:
                        reply.Msg().send()

            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment
