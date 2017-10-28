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
                    media_list = json.loads(media_list_str)
                    print '111111111111111111111111'
                    for media in media_list['item']:
                        target = recMsg.Content
                        if len(target) is not 8:
                            media_id = None
                        else:
                            if media['name'].find(target) is not -1:
                                media_id = media['media_id']
                            else:
                                media_id = None

                    print '222222222222222222222'
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
