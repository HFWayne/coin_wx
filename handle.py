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
                    media_list_str = myMaterial.batch_get(accessToken, mediaType)
                    mediaId = None
                    print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    print type(media_list_str)
                    media_list = json.loads(media_list_str)
                    print media_list
                    for media in media_list['item']:
                        print media

                    if mediaId is not None:
                        mediaId = recMsg.MediaId
                        replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                        return replyMsg.send()
                    else:
                        content = "查询无结果!"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()

                if recMsg.MsgType == 'image':
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
