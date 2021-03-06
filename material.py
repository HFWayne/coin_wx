# -*- coding: utf-8 -*-
# filename: material.py
import urllib2
import json
import poster.encode
from poster.streaminghttp import register_openers
from basic import Basic


class Material(object):
    def __init__(self):
        register_openers()

    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(postUrl, news)
        print urlResp.read()

    # 上传
    def uplaod(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        fileName = "hello"
        param = {'media': openFile, 'filename': fileName}
        # param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (
        accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print urlResp.read()

    # 下载
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()  # 素材的二进制
            mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "get successful"

    # 删除
    def delete(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        print urlResp.read()

    # 获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=7):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/material"
                   "/batchget_material?access_token=%s" % accessToken)
        postData = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }"
                    % (mediaType, offset, count))
        urlResp = urllib2.urlopen(postUrl, postData)
        return urlResp.read()


if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    #myMaterial.uplaod(accessToken, "./image/SDR00000001.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000002.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000003.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000004.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000005.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000006.jpeg", "image")
    myMaterial.uplaod(accessToken, "./image/SDR00000007.jpg", "image")
